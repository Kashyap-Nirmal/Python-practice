fileObj=open("myfile.txt","w")
print("File opened for writing.")
fileObj.write("First line\n")
fileObj.write("second line\n")
fileObj.write("third line\n")
print("Data is written on file.")
fileObj.close()