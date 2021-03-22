fileObj=open("story.txt","r")
def fileCount():
    data=fileObj.read()
    list1=data.split()
    list2=data.split("\n")
    print("Total lines:",len(list2))
    print("Total words:",len(list1))
fileCount()