import re
flag=0
id=input("Enter student id.\n")
if(re.match("\d+",id)):
    name=input("Enter student name.\n")
    if(re.match("[a-zA-Z]+",name)):    
        fees=input("Enter fees.\n")
        if(re.match("^\d+(\.\d\d?)?$",fees)):    
            email=id+"@daiict.ac.in"
            flag=1
        else:
            print("Invalid fee amount.")
    else:
        print("Invalid student name.")
else:
    print("Invalid student id.")
if(flag==1):
    email=id+"@daiict.ac.in"
    print("{:<12} | ".format("ID"),id)
    print("{:<12} | ".format("Name"),name)
    print("{:<12} | ".format("Fees amount"),fees)
    print("{:<12} | ".format("Email ID"),email)
#\d+\.{0,1}\d{1,2}