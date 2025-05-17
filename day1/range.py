
for i in range(40,10,-1):
    print(i,end = ",")
for i in range(10,40,1):
    print(i,end = "\n")
for i in range(10,40,2):
    print(i,end = ",")

#range of numbers
for i in range(1,40) :
    print(i,end =",")


# ascending and descending order of number 
for i,j in zip(range(10, 40),range(40,10)):
    print(i,j)
    
#caluclating factorial
    
fact = 1 #assigning 1 to the value fact
for i in range(1,11): #taking numbers from range of 1 to 10
    fact *= i #multiplying the values
    print(f"{i}! = {fact}")