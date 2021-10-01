#!/bin/python3
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import sys
import argparse
import pandas as pd
from os import path, name, system
from tabulate import tabulate
import numpy as np

# Defining Colour Schemas
NONE='\033[00m'
BLACK='\033[01;30m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
BLUE='\033[0;34m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
BLINK='\033[5m'
UNDERLINE='\033[4m'

# Clear Screen
def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

# Fun Banner With Essential Information
def showBanner(emailid,excel,sl,mess):
	banner=f"""
⣿⠿⣛⣯⣭⣭⣭⣭⣭⣭⣥⣶⣶⣶⣶⣶⣮⣭⣭⣭⣭⣭⡛⢻⣿⣿⣿⣿⣿⣿⣿
⡇⣾⣿⣿⣿⣿⣿⠿⢛⣯⣭⣭⣷⣶⣶⣶⣶⣶⣶⣶⣶⣬⣭⢸⣿⣿⣿⣿⣿⣿⣿
⡇⣶⣶⣶⣶⣶⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿ Sit Back And Enjoy As I Send The Emails 
⡇⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⡿⢋⣩⠭⠭⡙⢋⣭⠶⠒⠒⢍⡘⠻⣿⣿⣿⣿⣿⣿ 
⡇⣿⣿⣿⣿⣿⢸⣿⣿⡿⣋⣴⣯⡴⠚⠉⡡⠤⢄⣉⣅⡤⠄⢀⢺⡌⣻⣿⣿⣿⣿ 
⡇⣿⣿⣿⣿⣿⢸⣿⡏⡆⣿⣿⣉⣐⢴⣿⠈⠈⢀⠟⡿⠷⠄⢠⢎⢰⣿⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⣿⢸⣿⣿⣿⡫⣽⣒⣤⠬⠬⠤⠭⠭⢭⣓⣒⡏⣾⣿⣿⣿⣿⣿ Email ID : {emailid} 
⡇⣿⣿⣿⣿⣿⢸⡿⢸⣿⣿⣿⣿⣷⣾⣾⣭⣭⣭⣭⣭⣵⣵⡴⡇⠉⠹⣿⣿⣿⣿ Password : xxxxxxxxxxxxx 
⡇⣿⣿⣿⣿⣿⢸⠠⠄⠉⠉⠛⠛⠛⠛⠛⠊⠉⠉⠉⠉⠁⠄⠄⠄⠠⢤⡸⣿⣿⣿ Excel Sheet To Read Data From : {excel}
⢇⡻⠿⣿⣿⣿⠘⣠⣤⣤⣀⡚⠿⢦⣄⡀⠤⠤⠤⣤⣤⣤⣤⣤⣤⣄⣘⠳⣭⢻⣿ Subject Line : {sl}
⣎⢿⣿⣶⣬⣭⣀⠛⢿⣿⣿⣿⣷⣶⣬⣙⡳⠟⢗⣈⠻⠛⠛⠛⠛⢿⣿⣿⣦⢸⣿ File To Read Message From : {mess}
⣿⣆⢿⣿⣿⣿⣽⣛⣲⠤⠤⢤⣤⣤⣤⣀⡙⣿⣿⣿⠇⣤⣤⣤⡶⢰⣿⣿⠃⣼⣿
⣿⣿⣆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⡖⣸⣿⡟⣠⣶⣶⡖⣠⣿⡿⣡⣾⣿⣿
⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣽⣛⣛⡻⣿⠇⣿⣿⠃⣿⣟⡭⠁⣿⣯⣄⢻⣿⣿⣿
⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣷⣭⣙⠗⣸⣿⡇⣾⣮⣙⡛⣸⣿⣿⣿
	"""
	print(f"{GREEN}{banner}{NONE}")

# Read the message to send from a given text file
def readMessage(filename):
	if(path.isfile(filename)):
		f = open(filename, "r")
		return f.read()
	else :
		print(f"{RED}[-] No Such File Exists !{NONE}")
		sys.exit(-2)

# Take password as an input without echoing it to the screen
def askPass(emailid):
	while (True):
		try:
			p = getpass.getpass(prompt=f'[+] Enter Password For {emailid} : ', stream=None)
		except Exception as error:
			print('[-] ERROR : ', error)
			sys.exit(-1)
		if (p!=""):
			return p

# Get the Headers from the Excel sheet which you want to include in your message
def getHeader(cnames):
	arg=list()
	i=0

	print(f"\n{PURPLE}[+] Enter The Number Corresponding to The Column You'll Need : {NONE}")
	for col in cnames :
		print(f"{CYAN}{i}->{col} ")
		i=i+1
	print(f"{YELLOW}[+] Leave Blank To Exit {NONE}")

	while True :
		try :
			pos=input(">> ")
			if (pos==""):
				break
			arg.append(cnames[int(pos)])
		except ValueError as E :
			print(f"{RED}[-] Error : {E}{NONE}")

	print(f"\n{CYAN}[+] The Selected Arguments Are : {NONE}")
	for name in arg :
		print(f"{GREEN}[+] {name}{NONE}")
	return arg

# Get Datafram from excel sheet
def parseExcel(excelfile):

	data=dict()
	headerlist=list()
	try :
		df = pd.read_excel(excelfile,sheet_name=0)
	except Exception as e :
		print("[+] Error : ",e)
		sys.exit(-3)
	df.dropna(how='all', axis=1, inplace=True)
	return df

# Arrange the headers in the order they'll be appended to in the message
def orderList(mess, headerlist) :
	formatlist=list()
	i=0
	print(f"\n{PURPLE}[+] Your Message : \n{CYAN}{mess}{NONE}")
	if len(headerlist) != 0 :
		print(f"\n{YELLOW}[+] Available Headers : {NONE}")
		for header in headerlist : 
			print(f"{PURPLE}{i}->{header}{NONE}") 
			i=i+1
		print(f"\n{CYAN}[+] Enter The Indexes In The Order You Want Them To Be In The Message :{NONE}")
		
		for i in range(len(headerlist)) :
			try :
				#pos=int(input(f"-> "))
				pos=input(f"-> ")
				if pos=="" :
					print(f"\n{YELLOW}[+] Prserving Order !{NONE}")
					return headerlist
				else :
					pos=int(pos)

				formatlist.append(headerlist[pos])
			except ValueError :
				print(f"{RED}[+] Value Error{NONE}")
				sys.exit(-1)
			except IndexError as e :
				print(f"{RED}[+] Error : \n{e}{NONE}")
				sys.exit(-2)
		
		print(f"\n{CYAN}[+] The Order Of Headers As Selected :{NONE}")
		for i in range(len(formatlist)) :
			print(f"{YELLOW}[{i}]> {formatlist[i]}{NONE}")

	return formatlist

# Show table of values to be included 
def showtable(df,headerlist):
	headerstouse=dict()
	for header in headerlist:
		headerstouse[header]=df[header].tolist()
	table=tabulate(headerstouse,headers="keys",tablefmt="pretty")
	print(f"\n{PURPLE}[+] Data To Send : {NONE}")
	print(f"{CYAN}{table}{NONE}")
	return headerstouse

def selectEmailColumn(headers) :
	i=0
	print(f"{PURPLE}[+] Headers (Yes, Again) : {NONE} ")
	for i in range(len(headers)) :
		print(f"{YELLOW}{i}->{headers[i]}{NONE}")
		i=i+1	

	for i in range(len(headers)) :
		if "email" in (headers[i].lower()) :
			choice=input(f"{CYAN}\n[+] Is ({i}:{headers[i]}) The Column For Emails ? : [Y/n] ")
			if choice=="" or choice.lower()[0] == "y" :
				return i
	try :
		index=int(input(f"\n{PURPLE}[+] Enter The Column Containing Email IDs : {NONE}"))
		return index
	except :
		sys.exit(-3)

def genmessage(message, elementlist):
	i=0
	fmt=""
#	try :
	for j in range(len(message)):
		if message[j]=="{" and message[j+1]=="}" :
			fmt=fmt+elementlist[i]
			i=i+1
		elif message[j-1]=="{" and message[j]=="}" :
			pass
		else :
			fmt=fmt+message[j]
	return fmt
#	except Exception as e :
#		print(f"{RED}[-] Error : {e}{NONE}")
#		sys.exit(-4)


def sendmail(email, passwd, excel, subject, mess, df, orderedlist, index) :
	emailids = list(df[list(df.columns.values)[index]])
	
	for i in range(len(emailids)) :
        message = MIMEMultipart()
        message['From'] = email 
        message['Subject'] = subject
		print(f"{YELLOW}[+] Sending Email To : {emailids[i]}{NONE}")
		message['To']=emailids[i]
		valuelist=list()
		for header in orderedlist :
			valuelist.append(list(df[header])[i])
		message.attach(MIMEText((genmessage(mess,valuelist)), 'plain'))
		try :
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(email, passwd) #login with mail_id and password
			text = message.as_string()
			session.sendmail(email, emailids[i], text)
			session.quit()
			print(f"{GREEN}[+] Email Sent !{NONE}")
		except Exception as e: 
			print(f"{RED}[-] Could Not Send Email !\n[-] Error : {e}")
			choice=input(f"[*] Continue ? [y/N] : {NONE}" ).lower()
			if choice=="y" :
				continue
			else :
				print(f"{RED}[-] Exiting{NONE}")
				sys.exit(-1)

def main():
	parser = argparse.ArgumentParser(description=f"{RED}{BOLD}[+] Automated Mailer :{GREEN}{BOLD} @whokilleddb{NONE}") 
	parser.add_argument('-e', metavar='Email ID', required=True, help="Email ID to use for mailing")
	parser.add_argument('-s', metavar='Excel Sheet', required=True, help="Path To Excel Sheet") 
	parser.add_argument('-sl', metavar='Subject Line', required=True, help="Subject Line Of Email")
	parser.add_argument('-m', metavar='Message To Send', required=True, help="File Containing Message To Send")  
	args = parser.parse_args()
	message=readMessage(args.m)
	passwd=askPass(args.e)
	df=parseExcel(args.s)
	print(f"{PURPLE}[+] Parsed Data : \n{CYAN}{df}{NONE}")
	headerlist=getHeader(list(df.columns.values))
	orderedlist=orderList(message,headerlist)
	showtable(df,orderedlist)
	index=selectEmailColumn(list(df.columns.values))
	clear()
	showBanner(args.e,args.s,args.sl,args.m)
	sendmail(args.e,passwd,args.s,args.sl,message,df,orderedlist,index)

if __name__ == '__main__':
	main()
