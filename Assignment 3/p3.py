input1='''You have received first email from abc@gmail.com, You have received second email from def@gmail.com, You have received third email from pqr@gmail.com, You have received 
fourth email from qwert@gmail.com, You have received fifth email from spam@gmail.com'''
#List1 contains all space seperated elements
list1=input1.split()
setA=set(input1.split())
#count contains frequency of each unique elements
count={}
#bigram contains all bigram elements
bigram=[]
#count contains frequency of each unique bigram lements
bigram_count={} 
frequency=0
for i in setA:
    frequency=0
    for j in list1:
        if(i==j):
            frequency+=1      
    count[i]=frequency
padding_size = 15
res = "\n".join("| {:<22}|   {}   |".format(x, y) for x, y in zip(setA, count.values()))
print("-"*33)
print("| {:<22}| Count |".format("Word"))
print("-"*33)
print(res)
print("-"*33)
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
print("-"*33)
print("| {:<30}|".format("Bigrams:"))
print("-"*33)
print("| {:<22}| Count |".format("Word"))
setBigram=set(bigram)
for i in setBigram:
    frequency=0
    for j in bigram:
        if(i==j):
            frequency+=1      
    bigram_count[i]=frequency
res = "\n".join("| {:<22}|   {}   |".format(x, y) for x, y in zip(setBigram, bigram_count.values()))
print("-"*33)
print(res)
print("-"*33)