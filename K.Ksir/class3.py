#making use of constructor to shorten the class.
#Accept parameters in constructor.
#setting default value.


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


