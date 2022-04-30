#inheriting one class from another.
#it has a parent child relation.
#add parent class in () for child.
#Child class can directly use parent methods
class student:
    def __init__(self):
        print("new student has arrived ")
    def setName(self,param_name):
        self.fullname = param_name
    def getName(self):
        return self.fullname
    def setSubject(self,param_subject):
        self.subject = param_subject

class intern(student):
    def __init__(self,project):
        self.project = project
    def introduce(self):
        print("hi I am " + self.fullname + " my subject is " + self.subject + " and I am working on " + self.project)


i = intern("ERP")
i.setName("Rahul")
i.setSubject("Python")
i.introduce()