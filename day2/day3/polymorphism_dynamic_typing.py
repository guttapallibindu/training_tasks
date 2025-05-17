class Trainer :
    def get_role(self):
        print("\nTrainer teaches\n")
class student :
    def get_role(self):
        print("\nstudent learns new skills\n")
class admin:
    def get_role(self):
        print("\nadmin manages the system \n")


def show_role(person):
    person.get_role()

choice = input("enter your choice :")
if choice == "Trainer":
    show_role(Trainer())
elif choice == "student":
    show_role(student())
elif choice == "admin":
    show_role(admin())

        