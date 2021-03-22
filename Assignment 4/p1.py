c=0
a=-1
b=1
list_fib=[]
n=int(input("Enter the number:\n"))
def fib_n():  
 global a,b,c
 if((a+b)>n):
  for i in list_fib:
   print(i, end ="  ")  
 else:
  c=a+b
  a=b
  b=c
  list_fib.append(c)
  fib_n()           
fib_n()         