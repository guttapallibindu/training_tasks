try :
    a = int(input("Enter a number : "))
except ValueError:
    print("enter a number")
else:
    print("square of the number is : ", a * a)

try :
    nume = int(input("enter numerator value : "))
    deno = int(input("enter denominator value : "))
    
    result = nume / deno
    print(result)
except ZeroDivisionError:
    print("we cannot divide a number with zero")
except ValueError :
    print("enter a valid number")
finally:
    print("excuted")

#=====================================================================

#file handling with exception
#opening a file and writing 
with open('employees.txt','w') as file :
    file.write("ID,Name,Department,salary\n")
    file.write("121,John,IT,50000\n")
    file.write("122,Bindu,data,18000\n")
    file.write("123,james,Finance,700000\n")
    
#try block for the error handling
try :
    with open('employees.txt', 'r') as file:
        for line in file:
            print(line.strip())
            
#error handling for except
except FileNotFoundError:
    print("Error:File not found")
    
#appending a value into the text file 
with open('employees.txt', 'a') as file:
    file.write("124,mike,marketing,50000\n")

print("New employee added sucessfully.")