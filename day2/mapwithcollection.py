'''#squaring of numbers 
numbers = [1,2,3,4,5]

squared_numbers = list(map(lambda x: x**2, numbers))

print("squared numbers :",squared_numbers)'''
'''
#for marks and grade mapping
marks = [65,75,98,77,83]

grades = list(map(lambda x: 'a' if x >= 90 and x <= 100 else 'b' if x >= 80 and x < 90 else 'c' if x >=70 and x < 80 
                  else 'd' if x >=60 and x < 70 else 'e' if x >=50 and x < 60 else 'f', marks)) 
print("grades",grades)'''




# map with set 
text_data = {"Bindu", "Python ", "java", "oops"}

word_lengths = set(map(len, text_data)) #using length function to et size of the words 

print("Word Lengths:", word_lengths)

