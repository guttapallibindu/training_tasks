class Employee:
    company_name = "Southern info tech"
    def __init__(self,name,emp_id , department,salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Company     :{Employee.company_name}")
        print(f"Name        :{self.name}")
        print(f"emp_id      :{self.emp_id}")
        print(f"department  :{self.department}")
        print(f"salary      :{self.salary}")
        print("-" * 30)

#method with return type and no parameter
    def annual_salary(self):
        return self.salary * 12
    
#method without return type and with parameter   
    def apply_increment(self,percentage):
        increment =self.salary * (percentage / 100)
        self.salary += increment

#method with return type and with no parameter
    def is_high_earner(self):
        return self.salary > 70000
    
    @staticmethod
    def welcome_message():
        print("welcome to Southern Infotech")

#creating employee objects
emp1 = Employee("john","emp624","Intern",25000)
emp2 = Employee("mike","emp626","HR",75000)
emp3 = Employee("suan","emp685","Finance",50000)

emp1.display_details()
emp2.display_details()
emp3.display_details()

emp1.apply_increment(5)


emp1.is_high_earner()
emp2.is_high_earner()
emp3.is_high_earner()

print(f"is {emp1.name} a highe earner ? {'yes' if emp1.is_high_earner() else 'no'}")
Employee.welcome_message()
