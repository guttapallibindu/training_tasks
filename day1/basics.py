name = input("enter ur name:") #here name is a variable in which user name will be stored

print(f"{name}, welcome !")
#=======================================================================

userid = "1234" #userid is an integer and its tyoe is string
mynumber = int(userid) #userid is converted into integer type using int function and stored in a variable mynumber
print(f"{mynumber}")
#=====================================================================

boolean = True #declaring a variable and assigning its vakue as true 
print(type(boolean)) #printing the type of the variable boolean '''

#====================================================================
a =10  > 20 #compairng the values
print(type(a)) #will print the type of the varibale a
print(a) #print the boolean value of variable a 


#=================================================================

b = 0.25 > 2 #compairng the values
print(type(b)) #will print the type of the varibale b
print(b) #print the boolean value of variable b

c = a and b #perfroming a logical AND BETWEEN 2 variables
print(c)

d = 10 - 25 #performing a logical operation 
print(bool(d)) #converting d into a boolean 
print(type(d)) #will print the type of d , which is it primarily 

e = True if 10 > 5 else False 
print(e)


#=================================================================

emp_name = input("employee_name:" ) #storing name of a person in emp_name
emp_id = int(input("employee id :")) #converting emp id into integer type and storing it in emp_id
emp_job = input("job role :") #storing emp job role in emp_job
emp_pay = int(input("emp basic pay:")) #converting pay to int and storing it in emp_pay


allowance = emp_pay * (0.05 if emp_job == "manager" else 0.08 if emp_job == "developer" else 0.10 if emp_job =="analyst" else 0)
payable_salary = emp_pay + allowance
print(payable_salary)





