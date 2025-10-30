#bess class
class software_developer:
    def __init__(self,exp_level):
        self.exp =exp_level
    def cal_salart(self):
        base_salary = 10000
        actual_salary =10000 *self.exp
        print(actual_salary)
##Redundent case
class Intern(software_developer):
   #def __init__(self,exp_level):
     #  self.exp =exp_level
   #def cal_salart(self)
    #   base_salary = 10000
      # actual_salary =10000 *self.exp
      pass
class Junior(software_developer):
    #def __init__(self,exp_level):
     #   self.exp =exp_level
    #def cal_salart(self)
      #  base_salary = 10000
       # actual_salary =10000 *self.exp
       pass
class Mid_level(software_developer):
    #def __init__(self,exp_level):
     #   self.exp =exp_level
    #def cal_salart(self)
     #   base_salary = 10000
      #  actual_salary =10000 *self.exp
      pass
class Senior(software_developer):
    #def __init__(self,exp_level):
     #   self.exp =exp_level
    #def cal_salart(self)
     #   base_salary = 10000
      #  actual_salary =10000 *self.exp
      pass
intern_obj = Intern(1)
junior_obj = Junior(2)
mid_level = Mid_level(3)
senior_obj = Senior(4)

intern_obj.cal_salart()
junior_obj.cal_salart()
mid_level.cal_salart()
senior_obj.cal_salart()