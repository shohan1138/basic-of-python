class Employee:
    def __init__(self,name,emp_id):
        self.name =name
        self.emp_id =emp_id
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Id: {self.emp_id}")

class Accountant(Employee):
    pass
emp1 =Employee("John Doe",1001)
acc1 =Accountant("Harlien",2001)

print("--- Employee ---")
emp1.display_info()

print("\n--- Accountant ---")
acc1.display_info()


        
        