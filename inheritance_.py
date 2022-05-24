class person: #base class
    def __init__(self, fname, lname): #create constructor
        self.fname = fname
        self.lname = lname
    
    def printname(self): #create function
        print(self.fname,self.lname)
class student(person): #inherit base class
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname) 
x = student("alex ", "pandey")
x.printname()
