# over wriding
#Use to redefine implementation in child class.
#specially suitable in parent stubs

class student:
    def __init__(self,paramName):
        self.fullName = paramName
        print("%s got admission"% self.fullName )
    def assignBatch(self,paramBatch):
        self.batch = paramBatch
    def introduce(self):
        print("Hi I am %s from %d batch"%(self.fullName, self.batch))

class intern(student):
    def __init__(self, paramName):
        super().__init__(paramName)
    def setProject(self,paramProject):
        self.project = paramProject
    def introduce(self):
        print("Hi I am %s from %d batch and I have %s project"%(self.fullName,self.batch,self.project))



i = intern("Suresh")
i.assignBatch(1)
i.setProject("fintech")

i.introduce()