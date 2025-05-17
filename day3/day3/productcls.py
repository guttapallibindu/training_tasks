class student:
    clg_name = "VIT"
    #constructor
    def __init__(self, sid , sname , sgrade ):
        self.sid = sid 
        self.sname = sname
        self.sgrade = sgrade
        
        #method to display student details 
    def display(self):
        print(f"student ID: {self.sid}")
        print(f"student name: {self.sname}")
        print(f"student grade: {self.sgrade}")

#main function
def main():
    print("student details :")
    
    s1 = student(201, "John",'A')
    s2 = student(202, "Mike",'B')

    s1.display()
    s2.display()

if __name__ == "__main__":
    main()




            
        