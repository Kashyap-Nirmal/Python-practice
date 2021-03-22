'''
List of all the function names used for the tasks mentioned in Python-Project are as below:

Task 3:
write_content()

Task 4:
get_student_list()

Task 5:
set_email_list_with_non_spam_email_id()

Task 6:
set_email_list_with_spam_email_id()

Task 7:
set_email_list_with_no_wave_info()
'''

from timeit import default_timer as timer
#--------------------------------------------------------------------Q3 START -------------------------------------------------------------------------
timestart=timer()

print("."*211,end="")
print("Task 3")
file_object = open("About-DAIICT.txt","r")
list1 = file_object.read().splitlines()
file_object.close()
files = {
    0 : "History",
    1 : "Environment",
    2 : "Recognition",
    3 : "Accreditation"
}
def write_content():
    '''
        All the files mentioned in task 3, will be generated through this function.
    '''
    #AK10
    for i in range(len(files)):
        file_name = files[i]+".txt"    
        file_object = open(files[i]+'.txt','w')
        if(i!=3):
            #The loop will run from index of occurence of keyword1 to index of occurence of keyword2
            for j in range(list1.index(files[i])+1,list1.index(files[i+1])):        
                if list1[j]!="":
                    file_object.write(list1[j]+"\n")  
            file_object.close()
        else:
            #The loop will run from index of occurence of keyword i.e. Accreditation till the end
            for j in range(list1.index(files[i])+1,len(list1)):        
                if list1[j]!="":
                    file_object.write(list1[j]+"\n")  
            file_object.close()
        print("\nContents of ",files[i],".txt has been created successfully.",end="")       
    print("\n")

write_content()
#--------------------------------------------------------------------Q3 OVER  -------------------------------------------------------------------------
#--------------------------------------------------------------------Q4 START -------------------------------------------------------------------------
print("."*211,end="")
print("Task 4")
def get_student_list():
    '''
        Names of all the students will be fetched from "student_name_list.txt". 
    '''
    file_object = open("student_name_list.txt","r")
    student_name_list = file_object.read().splitlines()
    print("\nName of students:",student_name_list,"\n")
    file_object.close()
get_student_list()
#--------------------------------------------------------------------Q4 OVER  -------------------------------------------------------------------------
#--------------------------------------------------------------------Q5 START -------------------------------------------------------------------------
print("."*211,end="")
print("Task 5")
import random
import datetime

available=dict.fromkeys(range(1,21),0);
random_email_list=random.sample(range(1,20), 15)

def random_date():    
    #-----generate random date
    start_date = datetime.date(1947, 1, 1)
    end_date = datetime.date(2021, 11, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    date_value=random_date.strftime("%B") + " "+random_date.strftime("%d") +", "+ random_date.strftime("%Y")
    return date_value;
    
def random_time(): 
    #---gen random time for file
    return str(random.randint(1,23))+":"+ str(random.randint(10,59))
    
def random_email():    
    #--gen email address from list of names
    file_object=open("student_name_list.txt",'r');
    student_name=file_object.read().splitlines();
    student_email=student_name[random.randint(0,len(student_name)-1)].replace(" ","_").lower()+"@daiict.ac.in";
    file_object.close()
    return student_email;
    
def contain_wave(value_wave):  
    #return one of wave line
    file_object=open(files[0]+".txt","r");
    data_History_with=file_object.read().splitlines();
    wave_list=[];
    for ele in data_History_with:
        if (value_wave in ele):
            wave_list.append(ele);
    file_object.close()
    return wave_list;

def random_8_line():  
    #---code for generate random 8 line
    content_file=[];
    list_of_wave=["first wave","second wave","third wave","fourth wave"]
    wave_list=contain_wave(random.choice(list_of_wave));
    random_file=random.sample(range(1,5),4);    
    for i in range(1,5):      
        random_file.append(random.randint(1,4));    
    for ele in random_file:
        if ele == 4:
            content_file.append(wave_list[random.randint(0,len(wave_list)-1)]);
        else :
            file_object=open(files[ele]+".txt","r")
            file_line_list= file_object.read().splitlines();
            content_file.append(file_line_list[random.randint(0,len(file_line_list)-1)]);
            file_object.close();
    return content_file;

def random_first_line():  
    # --code for first line
    #Received at 17:23 hrs on October 7, 2018 from fname_lname@daiict.ac.in 
    first_line="Received at "+random_time()+" hrs on "+random_date()+" from "+random_email();
    return first_line;

def set_email_list_with_non_spam_email_id():    
    '''
        All email files mentioned in task 5, will be generated through this function.
    '''
    #AD53
    for ele in random_email_list:
        available[ele]=1;
        name="email-"+str(ele)+".txt";
        file_object=open(name,'w')
        content_data=random_8_line();
        random.shuffle(content_data)  #this function re-arrange all element in list randomly         
        #ADD two line in file 
        file_object.write(random_first_line() + "\n");
        file_object.write("\n");
        for ele in content_data:
            file_object.write(ele + "\n");
        file_object.close();        
    email_list_sorted=random_email_list
    email_list_sorted.sort()
    print("\nThe email files which needs to be randomly generated in task number 5, with the prefix 'email-' are as shown : \n",email_list_sorted,"\n")
    
set_email_list_with_non_spam_email_id()  
#--------------------------------------------------------------------Q5 OVER  -------------------------------------------------------------------------
#--------------------------------------------------------------------Q6 START -------------------------------------------------------------------------
print("."*211,end="")
print("Task 6")
def unused_name():
    unused=[];
    for ele in available:
       if available[ele] == 0:
           unused.append(ele);
    return unused;
    
def random_first_line_6():  
    #random first line for non daiict domain
    #Received at 17:23 hrs on October 7, 2018 from fname_lname@daiict.ac.in 
    email_ids =[ "name1@gmail.com", "A_X_y@yahoo.co.in", "nm123@rediff.com", "nam_4_e@160.com"];
    first_line="Received at "+random_time()+" hrs on "+random_date()+" from "+email_ids[random.randint(0,len(email_ids)-1)];
    return first_line;

def set_email_list_with_spam_email_id():  
    '''
        Email files with spam email id will be generated through this function.
    '''
    #AD53
    unused_4_ele=random.sample(unused_name(),4) ;  #unused 4 file    
    for ele in unused_4_ele:
        available[ele]=1;
        name="email-"+str(ele)+".txt";
        file_object=open(name,'w')
        content_data=random_8_line();
        random.shuffle(content_data)  #this function re-arrange all element in list randomly 
        file_object.write(random_first_line_6() + "\n");
        file_object.write("\n");
        #ADD two line in file     
        for ele in content_data:
            file_object.write(ele + "\n");
        file_object.close();        
    print("\nThe email files which needs to be randomly generated in task number 6, with the prefix 'email-' are as shown : \n",unused_4_ele,"\n")
    
set_email_list_with_spam_email_id()
#--------------------------------------------------------------------Q6 OVER  -------------------------------------------------------------------------
#--------------------------------------------------------------------Q7 START -------------------------------------------------------------------------
print("."*211,end="")
print("Task 7")
def random_first_line_7():
    #Received at 17:23 hrs on October 7, 2018 from fname_lname@daiict.ac.in     
    first_line="Received at "+random_time()+" hrs on "+random_date()+" from pc_503@daiict.ac.in";
    return first_line;

def not_contain_wave():  
    #list which contain non-wave info
    file_object=open(files[0]+".txt","r");
    data_History_with=file_object.read().splitlines();
    wave_list=[];
    for ele in data_History_with:
        if ("first wave" not in ele and "second wave" not in ele and "third wave" not in ele and "fourth wave" not in ele):
            wave_list.append(ele);
    file_object.close()
    return wave_list;

def random_8_line_for_7(): 
    content_file=[];
    wave_list=not_contain_wave();
    random_file=random.sample(range(1,5),4);
    for i in range(1,5):
        random_file.append(random.randint(1,4));
    for ele in random_file:
        if ele == 4:
            content_file.append(wave_list[random.randint(0,len(wave_list)-1)]);
        else :
            file_object=open(files[ele]+".txt","r")
            file_line_list= file_object.read().splitlines();
            content_file.append(file_line_list[random.randint(0,len(file_line_list)-1)]);
            file_object.close();
    return content_file;

def set_email_list_with_no_wave_info():
    '''
        An email file which is to be generated with no wave information, will be generated through this function.
    '''
    #AD53
    unused_ele=unused_name();  #unused 1 file
    for ele in unused_ele:
        available[ele]=1;
        name="email-"+str(ele)+".txt";
        file_object=open(name,'w')
        content_data=random_8_line_for_7();
        random.shuffle(content_data)  #this function re-arrange all element in list randomly 
        file_object.write(random_first_line_7() + "\n");
        file_object.write("\n");
        #ADD two line in file         
        for ele in content_data:
            file_object.write(ele + "\n");
        file_object.close();        
    print("\nThe email file which needs to be randomly generated in task number 7, with the prefix 'email-' is as shown : \n",unused_ele,"\n")
    
set_email_list_with_no_wave_info()
#--------------------------------------------------------------------Q7 OVER  -------------------------------------------------------------------------
timeend=timer()
total_time=timeend-timestart
print("."*211,end="")
print("Running time : ",total_time,"s")