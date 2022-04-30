"""
Classes are user defined types.
#collection of variables represented together as a structure or definition.
#Functions called methods
"""

class table:
    def setType(self,materialType):
        self.materialType = materialType
    def getType(self):
        return self.materialType

tbl = table()
tbl.setType("wood")

print(tbl.getType())