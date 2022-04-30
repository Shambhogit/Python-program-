#Adding Runtime properties.
#a new property is instance specific.


class student:
    def __init__(self,param_name,param_subject):
        print("new student has arrived ")
        self.fullname = param_name
        self.subject = param_subject
    def getName(self):
        return self.fullname
    def getSubject(self):
        return self.subject

stud = student("sam","Python")
print(stud.getName())
print(stud.getSubject())
stud.course = "MultyStack"
print(stud.course)