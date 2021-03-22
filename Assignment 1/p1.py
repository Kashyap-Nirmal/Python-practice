i=1
print "1 Addition"
print "2 Subtraction"
print "3 Multiplication"
print "4 Division"
print "0 To Exit"
while i!=0 :	
    i=int(input("Enter the choice : "))
    if(i>0 and i<5):
        operandA=int(input("Enter 1st input. "))
        operandB=int(input("Enter 2nd input. "))  
    if(i==1):
        print "%d + %d = %d" %(operandA,operandB,operandA+operandB)        
    elif(i==2):
        print "%d - %d = %d" %(operandA,operandB,operandA-operandB)        
    elif(i==3):
        print "%d * %s = %d" %(operandA,operandB,operandA*operandB)        
    elif(i==4):
        print "%d / %d = %d" %(operandA,operandB,operandA/operandB)
    elif(i==0):
        break        
    else:
        print "Invalid choice."     
