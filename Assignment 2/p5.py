#Here split for email is assumed to be done on '@'.
input1='''You have received first email from abc@gmail.com, You have received second email from def@gmail.com, You have received third email from pqr@gmail.com, You have received 
fourth email from qwert@gmail.com, You have received fifth email from spam@gmail.com'''
list1=input1.split()
email=[]
for i in list1:
    if(i.find('@')!=-1):
        if(i.find(',')!=-1):            
            temp=i.split(',')            
            for j in temp:
                #This needs to be done for the case when email@gmail.com,email1@gmail.com kind of case occurs
                if(j.find('@')!=-1):
                    email.append(j)
        elif(i.find('\'')!=-1):
            temp=i.split('\'')            
            for j in temp:
                if(j.find('@')!=-1):
                    email.append(j)
        else:
            email.append(i)
max=''
flag=False
cnt=-1
index_pqr=0
print "-------------------------------------------------------"
print "Old list:\n"
for i in email:   
    print i
print "-------------------------------------------------------"
print "Operations performed on List :\n"
for i in email:   
    cnt+=1
    if(len(i)>len(max)):
        max=i
    if(flag==False and i!="daiict@gmail.com"):
        flag=True
        email.append("daiict@gmail.com")
        if(len("daiict@gmail.com")>len(max)):
            max="daiict@gmail.com"            
        print 'Added "daiict@gmail.com"'
    if(i=="spam@gmail.com"):
        email.pop(cnt)    
        print 'Removed "spam@gmail.com"'
    if(i=="pqr@gmail.com"):
        index_pqr=cnt
print "-------------------------------------------------------"        
print "Updated  list:\n"        
for i in email:   
    print i
print "-------------------------------------------------------"
print "Email ID with Max length : ",max
print "pqr@gmail.com is at index : ",index_pqr
print "-------------------------------------------------------"