class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
x = student("alex ", "pandey")
x.printname()