class Emp:
    def __init__(self, name, id, sl, role):
        self.name = name
        self.id = id
        self.sl = sl
        self.role = role

    def fac(self):
        if self.id>1000 and self.id<1050:
            return self.name + " " + "teaches" + " " + "english"
        elif self.id>=1050 and self.id<1100:
            return self.name + " " + "teaches" + " " + "physics"
        elif self.id>=1100 and self.id<1150:
            return self.name + " teaches " + "Maths"

    def inc(self):
        z = int((self.sl/10))
        return "The increment for " + self.name + " this year should be: " + str(z)

    def rol(self):
        return self.name + " " + "is a " + self.role

    def info(self):
        return "The employee\'s name is " + self.name + ". " + self.fac() + ". " + self.inc() + ". " + self.rol()

Harry = Emp("Harry", 1030, 60000, "Teacher")
Larry = Emp("Larry", 1070, 30000, "Lab Assistant")
Marry = Emp("Marry", 1120, 50000, "librarian")

print(Larry.inc())
print(Harry.fac())
print(Marry.rol())
print(Harry.info())


