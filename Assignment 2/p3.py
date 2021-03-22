'''
    Here we could initialize with 0,1 as well. But that is like hardcoding for first two values.
    This is a better alternative to that.
'''
int_1=-1
int_2=1
list1=[]
n=input("Enter the number, to get first N elements of Fibonnaci sequence:\n")
for i in range(n):
    temp=int_1+int_2
    list1.append(temp)    
    int_1=int_2
    int_2=temp    
for i in list1:
    print i,
    print " ",
