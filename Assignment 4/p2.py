findKey=int(input("Enter the element to search:\n"))
input_list=[10,9,6,5,3,1,2]
list1=[]
list1=list(input_list)
list1.sort()
i=0
j=len(input_list)
k=int((i+j)/2)
flag=0
def binary_search_rec():
 global i,j,k,flag 
 if(j==i or j-i==1 and flag==0):
  if(findKey==list1[i]):
   flag=1
   for l in range(len(list1)):
    if(input_list[l]==findKey):
     print("Index in original array is : ",l)
  else:
   print("Not found")
 elif(flag!=1):
  k=int((i+j)/2)
  if(findKey>list1[k]):
   i=k         
  elif(findKey<list1[k]):
   j=k      
  elif(findKey==list1[k]):   
   for l in range(len(list1)):
    if(input_list[l]==findKey):
     print("Index in original array is : ",l)
     flag=1
  binary_search_rec()    

def binary_search():
 global i,j,k,flag
 i=0
 j=len(input_list)
 k=int((i+j)/2)
 flag=0
 while j-i!=1  and j!=i and flag==0: 
  k=int((i+j)/2)
  if(findKey>list1[k]):
   i=k         
  elif(findKey<list1[k]):
   j=k      
  elif(findKey==list1[k]):   
   flag=1
   for l in range(len(list1)):
    if(input_list[l]==findKey):
     print("Index in original array is : ",l)
   break 
print("Recursive")
binary_search_rec()
print("Iterative ")
binary_search() 
if(flag==0 and j==i or j-i==1):
  print("Not found")   