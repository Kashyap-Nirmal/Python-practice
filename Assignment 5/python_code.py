fileRead=open("myfile.txt","r")
data1=""
data=fileRead.read()
data.split("\n")
fileRead.close()
if(data.find("second line")):
 data1=data.replace("second line","sorry! The content of this line has been changed!")
 print("\nOlder file contents:")
 print(data) 
 fileWrite=open("myfile.txt","w")
 fileWrite.write(data1)  
 fileWrite.close()
 fileRead=open("myfile.txt","r")
 print("\nUpdated file contents:")
 print(fileRead.read())
else:
 print("! String not found !") 