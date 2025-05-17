#fibonacci series using recurssion 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 
def fibonacci_series(range_limit):
    for i in range(range_limit):
        print(fibonacci(i), end=" ")
 
fibonacci_series(10) 


#highest number using lambda

biggest = lambda a, b, c: a if a > b and a > c else (b if b > c else c) 
print("Biggest:", biggest(12, 45, 23))  # Output: 45