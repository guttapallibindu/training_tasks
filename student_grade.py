
stud_id = int(input("student_id:")) #takes student id as input and stores in stud_id
sub1_mark = int(input("marks in sub1 :")) #takes input as sub1_mark of subject 1 mark
sub2_mark = int(input("marks in sub2 :")) #takes input as sub1_mark of subject 2 mark
sub3_mark = int(input("marks in sub3 :")) #takes input as sub1_mark of subject 3 mark

avg_mark = (sub1_mark + sub2_mark + sub3_mark)/3 #caluclates the average mark of the three subject marks

if sub1_mark and sub2_mark and sub3_mark >= 40: # if the mark in every subject is greater than 40 
    result = "Pass" #student is pass as avg_mark is > 40
    
    if avg_mark >= 80: #for students who have avg_mark > 80
        grade = "A+"
        
    if avg_mark > 60 and avg_mark < 79 : #for students who have avg_mark > 60 and < 79
        grade = "A"
        
    if avg_mark > 40 and avg_mark < 59: #for students who have avg_mark > 60 and < 79
        Grade = "B"
        
else: #if a student does not have mark > 40 in any one of the subject
    result = "Fail"
    print("need Improvement")
    
print(f"student_id: {stud_id},average_mark: {avg_mark},Result :{result},Grade:{grade}") 