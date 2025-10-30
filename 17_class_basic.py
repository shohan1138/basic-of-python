class Student:
    #name=''
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def info(self):
        return self.name,self.id
       # print("this is a student constructor")
name ='tasin' 
id=101
student1 =Student(name,id)
name1,id1 =student1.info()
print(name1,id1)

#student1 =Student(name,id)
#print(student1.name)
#student1.name='shohan'
#print(student1.name)

#student2 =Student()
#print(student2.name) #madke space cause it called before setting so it print empty space
#student2.name='Tashin'
#print(student2.name)

