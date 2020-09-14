class Work:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return("{}.{}@email.com".format(self.fname, self.lname))

    @email.setter
    def email(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

wk_obj =  Work("Ambarish", "Pandharikar")
print(wk_obj.fname)
print(wk_obj.lname)
print(wk_obj.email)
wk_obj.email = "Chaitali Nistane"
print(wk_obj.fname)
print(wk_obj.lname)
print(wk_obj.email)
del wk_obj.email
print(wk_obj.fname)
print(wk_obj.lname)
print(wk_obj.email)
