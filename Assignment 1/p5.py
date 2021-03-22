bill_amount=0
i=8
print"Enter your choice"
print "---------------------------------------"
print "| No | Name         |Qty  | Price     |"
print "--------------------------------------|"
print "| 1  | Notebook     | 01  |   Rs.57   |"
print "| 2  | Notebooks    | 06  |   Rs.270  |"
print "| 3  | Box of pen   | 01  |   Rs.80   |"
print "| 4  | Notebooks    | 12  |   Rs.540  |"
print "| 5  | Pen          | 01  |   Rs.120  |"
print "| 6  | Folder       | 01  |   Rs.100  |"
print "| 7  | File         | 01  |   Rs.50   |"
print "| 0  | To Exit      | --  |      -    |"
print "--------------------------------------|"
while i!=0:
    i=int(input())
    if(i==1):
        bill_amount+=57        
    elif(i==2):
        bill_amount+=270
    elif(i==3):
        bill_amount+=80
    elif(i==4):
        bill_amount+=540
    elif(i==5):
        bill_amount+=120
    elif(i==6):
        bill_amount+=100
    elif(i==7):
        bill_amount+=50
    elif(i==0):
        break
    else:
        print "Invalid choice."    
if(bill_amount<500):
    dr=1
    discount_price=0.99*bill_amount
elif(bill_amount>500 and bill_amount<1000):
    dr=2
    discount_price=0.98*bill_amount
elif(bill_amount>1000):
    dr=5
    discount_price=0.95*bill_amount
print "|----------------------------------"
print "| Total bill amount  | Rs.",bill_amount
print "| Discount rate      | ",dr,"%"
print "| Discounted price   | Rs.",discount_price
print "-----------------------------------"