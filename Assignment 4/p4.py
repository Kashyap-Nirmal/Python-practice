n=int(input("Enter number:\n"))    
d=n
temp=0
l=len(str(n))
def armstrong():
    global d,temp
    if d>0:
        r=d%10
        temp+=r**l
        d=int(d/10)         
        armstrong()       
armstrong()
if(n==temp):
    print("Armstrong number.")
else:
    print("Not an Armstrong number.")