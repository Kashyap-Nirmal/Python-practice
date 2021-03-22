data=[(202021001, "S-I", 85), (202021002, "S-I",80), (202021003, "S-I", 45), (202021004, "S-I",52),(202021005,"S-I", 63),
(202021001, "S-II", 88), (202021002, "S-II",79), (202021003, "S-II", 50), (202021004, "S-II",70),(202021005, "S-II", 60),
(202021001, "S-III", 80), (202021002, "S-III",74), (202021003, "S-III", 57), (202021004, "S-III",48),(202021005, "S-III", 75),]
Marks={}
Marks_Total={}
total=0
print("-"*50)
print("| Student ID\t| Section \t| Marks Obtained |")
print("-"*50)
for i in data:    
    Marks[str(i[0])+"\t"+i[1]]=i[2]    
    print("| ",str(i[0]),"\t|\t{:<6}".format(i[1])," |\t{:<7}".format(Marks[str(i[0])+"\t"+i[1]])," |")
print("-"*50)
print("\n")
print("-"*34)
print("| Student ID\t| Marks Obtained |")
print("-"*34)
for i in data:        
    id=i[0]
    if(id in Marks_Total):
        Marks_Total[id]+=i[2]
    else:
        Marks_Total[id]=i[2]            
for i in Marks_Total:
    print("| ",i,"\t|\t{:<9}|".format(Marks_Total[i]))
print("-"*34)
Keymax = max(Marks_Total, key=Marks_Total.get) 
print("\nMaximum marks",Marks_Total[Keymax]," are secured by ",Keymax)