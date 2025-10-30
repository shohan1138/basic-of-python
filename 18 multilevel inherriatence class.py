class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id = emp_id
    def display_info(self):
        print("yhe name of employee:",self.name)
        print("the id of the employee",self.emp_id)
class Manager(Employee):
    def diplay_department(self,dep_name):
         print("the name of department",dep_name)
         
class Developer(Manager):
    def diplay_expertise(self,lang_name):
         print("the name of department",lang_name)

        
manager =Manager('salman','1001')
dev =Developer('mainul','2002')

manager.display_info()
manager.diplay_department("Engineering")
dev.display_info()
dev.diplay_department("Engineering")
dev.diplay_expertise("python")