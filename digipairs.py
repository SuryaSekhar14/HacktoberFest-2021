def large(n):
  n = str(n)
  i = 9 
  while (i>=0):
    if(str(i) in n):
      return i
    i -= 1

def small(n):
  n = str(n) 
  i = 0 
  while(i<=9):
    if(str(i) in n):
      return i
    i += 1

def pairs(n):
  if(n>=3):
    return 2
  if(n==2):
    return 1
  return 0    
    
T = int(input())
n = list(map(int,input().split()))
bs=[]
for i in n:
  l = large(i)
  s = small(i)
  val = str(11*l + 7*s)
  if(len(val)>2):
    val = val[-2:]
  bs.append(val)

freq_odd = [0]*10
freq_even = [0]*10
for i in range(len(bs)):
  msd = int(bs[i][0])
  if(i%2==0):
    freq_even[msd]+=1
  else:
    freq_odd[msd] +=1
    
count = [0]*10

for i in range(10):
  if(freq_even[i]<=1 and freq_odd[i]<=1):
    continue
  count[i] += int(pairs(freq_even[i])+pairs(freq_odd[i]))
  count[i] = min(2,count[i])

print(sum(count))


  
  
  