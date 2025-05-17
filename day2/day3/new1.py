class Student:
    def __init__(self, student_id, name, course, marks):
        self.__student_id = student_id
        self.__name = name
        self.__course = course
        self.__marks = marks

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Course: {self.__course}, Marks: {self.__marks}"
    







        

    