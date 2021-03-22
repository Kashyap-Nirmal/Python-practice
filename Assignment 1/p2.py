ans=0
i=int(input("Input first number:"))
j=int(input("Input second number:"))
k=int(input("Input third number:"))
if(i>j):
    if(i<k):
        ans=i    
    else:
        ans=k
else:
    if(j<k):
        ans=j
    else:
        ans=k
print"The second largest number is ",ans