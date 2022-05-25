class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def myfunction(self):
        print("HELLO EVERYONE MY NAME IS {} {}".format(self.fname,self.lname))
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("niral" , "panchal")
x.myfunction()        
        