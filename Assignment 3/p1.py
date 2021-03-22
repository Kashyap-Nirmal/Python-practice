Student_details = {1001: "Ram", 1004: "Shyam", 1005: "Kamal", 1003: "John"}
print("\ni) Print details of Students")
for i in Student_details:
    print(i,"\t->\t",Student_details[i])
print("\nii) Print ids of Students")
print(Student_details.keys())
print("\niii) Print Students name in ascending order")
print(sorted([(v,k) for k,v in Student_details.items()]))
print("\niv) Delete the details of student id = 1005 and print updated dictionary")
if(1005 in Student_details):
    del Student_details[1005]
    print("Deleted key '1005'")
    print("\nUpdated dictionary")
    print(Student_details)    
else:
    print("Key '1005' does not exist")
print("\nv) Update the name of student id = 1003 to 'Kishan' and print updated dictionary.")
print("\nOlder dictionary")
print(Student_details)    
if(1003 in Student_details):
    Student_details[1003]="Kishan"
else:
    print("Key '1003' does not exist")
print("\nUpdated dictionary")
print(Student_details)
print("\nvi) Check whether details of students with id 1002 exists in the dictionary.")
print("1002 exsit in dictionary : ",1002 in Student_details)