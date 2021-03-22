print("Enter the data for the list.")
print("Enter 'Done' for exiting")
print("")
data='a'
list1=[]
while(data!='done'):
    data=raw_input()
    data_List=data.split('.')
    #Base case
    if data.lower()=='done':
        break
    #For integers
    elif data.isdigit():
        list1.append(float(data))
    #For float, the number should have digits on both side of '.'
    elif len(data_List)==2 and data_List[0].isdigit() and data_List[1].isdigit():
        list1.append(float(data))
    #For strings and other invalid inputs
    else:
        print "! Invalid input !"            
list1.sort()
print "\nList with valid input is : [",
for i in list1:
    print i,
    print ", ",
print "]"
print "The largest element is ",max(list1)
print "The smallest element is ",min(list1)
