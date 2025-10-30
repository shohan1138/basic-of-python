##if name and  phone and email not empty then it print success
name = 'fadd'
phone = '34524235233'
size_phone =len(phone)
email ='awd'
size_name =len(name)

if(name=='' or phone=='' or email ==''):
    print("the name field can not be empty")
else:
     #print("success")
    #nested conditional statement:
    if (size_name<3): 
        # accept only name wih 3 letters or more
       print("failed")
    elif(size_phone!=11):
        print("the phone length must be 11")
    else:
        print("success")
       
##Assignmet for AND operaor
