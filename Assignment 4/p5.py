import re
sample_input='''You have received first email from abc@daiict.ac.in at 11:00 am on 1st October, You have
received second email from def@gmail.com at 1:30 pm on 2nd October, You have received third
email from pqr@gmail.com at 10:30 am on 3rd October, You have received fourth email from qwert@gmail.com at 11:00 am on 4th October
, You have received fifth email from spam@gmail.com at 1:00 pm on 5th October'''
print("\na. Fetch all the email ids from the given text using the 'findall' function in regular expressions.")
print(re.findall(r'[a-zA-Z]*@[.a-zA-Z]*',sample_input))
print("\nb. Change the domain name as daiict.ac.in from all the email ids from given input using 'sub' function.")
print(re.findall(r'[a-zA-Z]*@daiict.ac.in',re.sub('@gmail.com ','@daiict.ac.in ',sample_input)))
print("\nc. Search the email id 'spam@gmail.com' from given input text")
print(re.search(r'spam@gmail.com',sample_input))
print("\nd. Fetch all time and date of all email ids.\n")
list1=re.findall(r'[a-zA-Z]*@gmail.com|[0-9]+:[0-9]+ [a,p]m|[0-9]+[st,nd,rd,th]+ [a-zA-Z]*',sample_input)
i=0
print("-"*47)
while i<=len(list1)-3:
    print("| {:<16}".format(list1[i]),"| {:<8}".format(list1[i+1]),"| ",list1[i+2]," |")
    i=i+3
print("-"*47)
