input1='''You have received first email from abc@gmail.com, You have received second email from def@gmail.com, You have received third email from pqr@gmail.com, You have received 
fourth email from qwert@gmail.com, You have received fifth email from spam@gmail.com'''
#List1 contains all space seperated elements
list1=input1.split()
#List2 contains all space seperated unique elements
list2=[]
#count contains frequency of each unique elements
count=[]
#bigram contains all bigram elements
bigram=[]
#bigram2 contains all unique bigram elements
bigram2=[]
#count contains frequency of each unique bigram lements
bigram_count=[]
cnt=-1
frequency=0
for i in list1:
    if(i not in list2):
        list2.append(i)
for i in list2:
    frequency=0
    for j in list1:
        if(i==j):
            frequency+=1      
    count.append(frequency)
res = "\n".join("{}\t->{}".format(x, y) for x, y in zip(list2, count))
print(res)
bigram_temp=""
cnt=0
for i in list1:
    cnt+=1
    if(cnt==1):
        bigram_temp+=i
    else:        
        bigram_temp+=" "+i    
    if(cnt%1==0 and cnt!=1):
        bigram.append(bigram_temp)
        bigram_temp=i
print"\nBigrams:"
for i in bigram:
    if(i not in bigram2):
        bigram2.append(i)
for i in bigram2:
    frequency=0
    for j in bigram:
        if(i==j):
            frequency+=1      
    bigram_count.append(frequency)
res = "\n".join("{}\t->{}".format(x, y) for x, y in zip(bigram2, bigram_count))
print(res)
