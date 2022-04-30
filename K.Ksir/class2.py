
#initialization can be done with some values by default.
#This is like geting out of the box setup.
#constructor is the function that executes by default.
#it is defied as __init__

class student:
    def __init__(self):
        print("new student has arrived ")
    def setName(self,param_name):
        self.fullname = param_name
    def getName(self):
        return self.fullname
    def setSubject(self,param_subject):
        self.subject = param_subject

stud = student()
stud.setName("sam")
stud.setSubject("Python")
print(stud.getName())