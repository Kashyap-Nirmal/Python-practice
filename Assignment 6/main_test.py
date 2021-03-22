'''
List of all the function names used for the tasks mentioned in Python-Project are as below:

Task 9:
get_email_list_with_no_wave_info()

Task 10:
rename_spam_list()

Task 11:
write_content_ordered_names()

Task 12:
order_email_id_()

Task 13:
plot_group()

'''

from timeit import default_timer as timer
timestart=timer()
#--------------------------------------------------------------------Q9 START -------------------------------------------------------------------------
print("."*211,end="")
print("Task 9")
import os
strName="email-"
temp=""
count_no_wave_info=0
def get_email_list_with_no_wave_info():
    '''
        Flag here indicates the presence of wave information. 
        flag=0 => No wave information.
    '''
    #KN31
    global temp
    global count_no_wave_info
    for i in os.listdir():            
        if(strName in i or "spam" in i):          
            flag=0    
            file_object=open(i,"r")        
            for j in file_object.read().split():            
                if(flag==0 and j!='wave' and j!='wave,'):
                    continue            
                else:
                    flag=1                
            if(flag==0):
                temp=i
                count_no_wave_info+=1
                print("\nThe email Ids whose files do not have any 'wave' information is :\n",temp,"\n")
                break
            file_object.close()
    return temp
    
get_email_list_with_no_wave_info()            
#--------------------------------------------------------------------Q9 OVER  -------------------------------------------------------------------------
#--------------------------------------------------------------------Q10 START-------------------------------------------------------------------------
print("."*211,end="")
print("Task 10")
spam_list=[]
if(temp!=""):
    spam_list.append(temp)
email_list=[]
def get_email_list():
    '''
        This function is used to bifurcate spam and non spam email list.
    '''
    #AK10
    for i in os.listdir():
        if(i!=temp and strName in i): 
            file_object = open(i,'r')        
            list1=file_object.readline().split()
            for ele in range(len(list1)):
                if ('@daiict.ac.in' in list1[ele]):
                    email_list.append(i)
                    break
                elif(ele==len(list1)-1):
                    spam_list.append(i)
            file_object.close()   
        #If spam file already exists i.e. if spam files were renamed previously.
        elif("spam" in i and i!=temp):
            spam_list.append(i)
    email_list.sort()
    spam_list.sort()
    print("\nEmail list is as shown :\n",email_list,"\n")   
    print("Spam mail list is as shown :\n",spam_list,"\n")

def rename_spam_list():
    '''
        This function is used to rename the email files which are marked as spam.
    '''
    #AK10
    get_email_list()
    for i in spam_list:
        file_object = open(i,'r')
        lines= file_object.read().split('\n')
        file_object.close()
        b = ['This email has been categorized as spam.']
        for j in range(len(lines)):
            b.append(lines[j])
        file_object = open(i,'w')
        b = map(lambda x:x+'\n',b)
        file_object.writelines(b)
        file_object.close()    
    for i in range(1,min(6,len(spam_list)+1)):
        '''
            os.rename() gives error if we try to rename new file with already existing file name.
            i.e. if 'spam1.txt' exist and we try to rename other file as 'spam1.txt' it gives error.
            So previously categorized spam files needs to be deleted.             
        '''
        if 'spam'+str(i)+'.txt' in os.listdir() and len(spam_list)>5:                    
            os.remove("spam"+str(i)+".txt")  
            spam_list.pop()
        os.rename(spam_list[i-1],'spam'+str(i)+'.txt')
        print("File '%12s' is categorized spam and is renamed as 'spam" %(spam_list[i-1]) +str(i)+"'.txt'",end="\n")
        
rename_spam_list()       
#--------------------------------------------------------------------Q10 OVER -------------------------------------------------------------------------
#--------------------------------------------------------------------Q11 START-------------------------------------------------------------------------
print("")
print("."*211,end="")
print("Task 11")
temp_time=""
dict_datetime_string={}
dict_name_datetime={}
from datetime import datetime
def get_date_time_email_lists(email_list1):
    '''
        This function is used to fetch the list of email with their corresponding date-time.
    '''
    #KN31
    
    #This dictionary contains date time in string format
    dict_datetime_string={}
    #This dictionary contains date time objects
    dict_name_datetime={}
    for i in email_list1:        
        file_object=open(i,"r")        
        list1=file_object.readline().split()
        ele=0
        date_string=""        
        for j in range(4):
            #Date is fetched here.
            if('on' in list1[ele]):
                #Time fetched is appended here.
                date_string=list1[ele+1]+" "+list1[ele+2]+" "+list1[ele+3]+" "+temp_time.split()[0]                
                #We are fetching next 3 elements. Thus the increment of 4 is used.
                ele+=4                                                                           
            #Suppose the fname_lname contains 'at', for avoiding the confusion of time/email below condition is used.
            #'@daiict.ac.in' not in list1[ele] condition is used.
            #For eg. 'nimmi_patel@daiict.ac.in' will be detected here otherwise.                                            
            #Time is fetched here.
            elif('at' in list1[ele] and '@daiict.ac.in' not in list1[ele]):                                
                temp_time=list1[ele+1]+" "+list1[ele+2]
                #We are fetching next 2 elements. Thus the increment of 3 is used.
                ele+=3            
            #Email is fetched here.                
            elif('from' in list1[ele] and'@daiict.ac.in' in list1[ele+1]):
                #The date time in string format is converted to date time object.
                date_object = datetime.strptime(date_string, "%B %d, %Y %H:%M")
                dict_name_datetime[date_object]=list1[ele+1]
                dict_datetime_string[date_string]=list1[ele+1]
            else:
                ele+=1                
        file_object.close()                 
    print("\nThe original data which will be sorted is as below:")
    print("-"*61)
    print("| %24s | %30s |" %("Date Time","Email Id"))
    print("-"*61)
    for i in dict_datetime_string:        
        print("| %24s | %30s |" %(i,dict_datetime_string[i]))
    print("-"*61)    
    sorted_dict=sorted([[k,v] for k,v in dict_name_datetime.items()],reverse=True)            
    return sorted_dict

#Here the flag value indicates if repetition of email id is allowed or not.     
def write_content_ordered_names(file_name,email_list1,flag):
    '''
        The emails will be written to ordered_names files through this function.
    '''
    #KN31
    
    sorted_dict=get_date_time_email_lists(email_list1)       
    #Set is used for avoiding duplication of emails for the task 12
    temp_set=set()    
    print("\nThe sorted data which will be written to the file is as below:")
    print("-"*56)
    print("| %19s | %30s |" %("Date Time","Email ID"))
    print("-"*56)            
    file_object=open(file_name,"w")            
    for i in range(len(sorted_dict)):                
        if flag==0 and sorted_dict[i][1] in temp_set:
            continue
        else:
            temp_set.add(sorted_dict[i][1])             
        file_object.write(sorted_dict[i][1]+"\n")
        print("! %18s | %30s |" %(sorted_dict[i][0],sorted_dict[i][1]))
    print("-"*56)
    print("\nContent of the file",file_name," written successfully.","\n")
    file_object.close()
    for i in range(5):
        if(str(i) in file_name):
            datavalue[str(i)]=len(temp_set)
            
#Here Flag=1 means with repetition.    
write_content_ordered_names("ordered_names.txt",email_list,1)
#--------------------------------------------------------------------Q11 OVER -------------------------------------------------------------------------
#--------------------------------------------------------------------Q12 START-------------------------------------------------------------------------
print("."*211,end="")
print("Task 12")
#This dictionary contains the counts of the #files containing "first wave" or so.
datavalue={"1":0,"2":0,"3":0,"4":0,"no.of Spam":0}
#This dictionary contains the list of files, which are bifurcated as "first wave" files and so on.
ordered_list_waves={1:[],2:[],3:[],4:[]}

def divide_groups(strName1):
    '''
        This function will bifurcate the files as files which contain "first wave" or "second wave" and so on.
    '''
    #KN31
    
    for i in os.listdir():    
        if (strName1 in i):   
            file_object=open(i,"r")
            for j in file_object.read().splitlines():
                if "first wave" in j:
                    ordered_list_waves[1].append(i)
                    break;
                elif "second wave" in j:
                    ordered_list_waves[2].append(i)
                    break;
                elif "third wave" in j:
                    ordered_list_waves[3].append(i)
                    break;
                elif "fourth wave" in j:
                    ordered_list_waves[4].append(i)
                    break;            
    #We already have the spam list fetched in task 10.                
    datavalue["no.of Spam"]=len(spam_list)

def order_email_id_():
    '''
        This function will bifurcate the files containing "first wave" and write their email ids to "ordered_list_waves1.txt" and so on.
    '''
    #KN31    
    
    #Here Flag=0 means no repetition.
    flag=0
    divide_groups("email")            
    for i in ordered_list_waves:                       
        write_content_ordered_names("ordered_names_wave"+str(i)+".txt",ordered_list_waves[i],flag)    
       
order_email_id_()
#--------------------------------------------------------------------Q12 OVER -------------------------------------------------------------------------
#--------------------------------------------------------------------Q13 START-------------------------------------------------------------------------
#import matplotlib.pyplot as plt 

def plot_groups():
    keys = datavalue.keys()
    values = datavalue.values()    
    print(values)
    #plt.bar(keys, values)
    
plot_groups()

#--------------------------------------------------------------------Q13 OVER -------------------------------------------------------------------------
timeend=timer()
total_time=timeend-timestart
print("")
print("."*211,end="")
print("Running time : ",total_time,"s")

#For some reason matplotlib is not running in cmd. Thus plot was generated using Spyder IDE.