'''class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def __str__(self):
        return f"{self.name} scored {self.marks} marks"
    
    def __len__(self):
        return len(self.name )
    
    def __add__(self, other):
        return self.marks + other.marks
    
s1 = student("Bindu", 80)
s2 = student("John", 65)

print(s1)
print(len(s1))
print(s1 + s2)'''

class Book:
    def __init__(self,title , author):
        self.title = title
        self.author = author 
    def __str__(self):
        return f"{self.title} was written by {self.author}"
    
    def __len__(self):
        return len(self.title)
    
b1 = Book("title1", "john")
b2 = Book("title2", "mike")

print(b1)
print(len(b1))
print('-' * 5)

print(b2)
print(len(b2))

    
