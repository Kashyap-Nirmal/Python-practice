fileObj=open("myfile1.txt","r")
data=fileObj.read()
fileObj.close()
list1=data.split()
print("\nOlder file contents:")
print(data) 
j=0
fileObj=open("myfile2.txt","w")
for i in list1:
 temp=i+"\n"
 fileObj.write(temp) 
fileObj.close()
fileRead=open("myfile2.txt","r")
print("\nNew file contents:")
print(fileRead.read())