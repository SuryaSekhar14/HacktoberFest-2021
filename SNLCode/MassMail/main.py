import smtplib
from email.message import EmailMessage
import pandas as pd
import codecs
excelink=input("Enter the excel link : ")
df = pd.read_excel(open(excelink,'rb')) # can also index sheet by name or fetch all sheets
dftemp=pd.ExcelFile(excelink)
print(dftemp.sheet_names)
print(df.columns)
column=input("Enter the Column Name: ")
mylist = df[column].tolist()

print(mylist)
#taking the email as the input
emailid=input("Enter the Email ID: ")
emailpasswd=input("Enter the Email Password: ")

#taking the subject as the input
subjectemail=input("Enter the Subject of the email: ")

msg = EmailMessage()
msg['Subject']=subjectemail
msg['from'] = emailid
msg['to'] = mylist

#enter the html here but make sure it is in one line
path=input("Enter the path for the email html : ")
file=codecs.open(path,"r")
htmlcode=file.read()
msg.add_alternative(htmlcode,subtype='html')

print("Your messages will be sent now! If you want to stop please stop now")
n=input("Press enter to confirm or hit CTRL+C")

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
  smtp.login(emailid,emailpasswd)
  smtp.send_message(msg)
print("message sent successfully")
