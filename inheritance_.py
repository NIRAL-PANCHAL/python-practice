<<<<<<< HEAD
class person:
    def __init__(self, fname, lname): #constructor created
        self.fname = fname
        self.lname = lname
    
    def printname(self): #function created
        print(self.fname,self.lname)
class student(person): #child class / inherit class
    def __init__(self, fname, lname): 
        person.__init__(self, fname, lname)
x = student("alex ", "pandey") #assign the value
x.printname() #calling function
=======
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
>>>>>>> 544c20b467a340f126740c171a3cdec332af755f
