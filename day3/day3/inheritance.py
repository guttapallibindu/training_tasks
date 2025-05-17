'''class BankAccount :
    def __init__(self,account_number,holder_name,balance):
        self.accountnumber = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += ampunt
        print(f"Deposited {amount}.New balance is {self.balance}")

    def withdraw(self)'''

class Person: #parent class
    def __init__(self, name, age): #parameters name and age 
        self.name = name
        self.age = age

    def display(self): #display function 
        return f"\nname: {self.name}, age: {self.age}"


class Student(Person): #inheriting parent classs to the child class
    def __init__(self, name, age, student_id, grade): #extra attributes are student_id and grade
        super().__init__(name, age) #calling using super class
        self.student_id = student_id
        self.grade = grade

    def display_student_info(self):
        return f"{self.display()}, Student ID: {self.student_id}, Grade: {self.grade}"

#object creation
student1 = Student("John Doe", 20, "345", "A\n")
student2 = Student("Bindu",21,"624","B\n")
student3 = Student("Mike",20,"456","A+\n")

#displaying the student info 
print(student1.display_student_info())
print(student2.display_student_info())
print(student3.display_student_info())