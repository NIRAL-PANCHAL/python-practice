class person:
    def __init__(self, fname, lname):
            self.fname = fname
            self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduatationyear = year

    def welcome(self):
        print("HELLO SIR MY NAME IS {} {} AND MY GRADUATION YEAR IS {}".format(self.fname,self.lname, self.graduatationyear))
x = student("niral", "panchal", 2021)
x.welcome()   
x.printname()    
    