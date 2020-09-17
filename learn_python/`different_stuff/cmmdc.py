#Cmmdc

def give_a_number():
   n=int(input("Introdu un numar natural:"))
   return n

def cmmdc(a,b):
  while (a!=b):
    if a>b:
       a=a-b           
    else:
       b=b-a           
  return a
 
def function():    
  a=give_a_number()
  b=give_a_number()
  d=cmmdc(a,b)
  print ("cmmdc("+str(a)+","+str(b)+")="+str(d))

function()

