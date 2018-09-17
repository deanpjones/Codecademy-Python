# -------------------------------------------------------------
# CLASS: NAME
class Name():
    #constructor
    def __init__(self, fname, lname):
        self.first = fname.strip().title()                  #clean up (whitespace, capitalize name)
        self.last = lname.strip().title()                   #clean up (whitespace, capitalize name)
        self.fullname = self.first + " " + self.last
    #string representation
    def __repr__(self):
        return 'Name: {} {}'.format(self.first, self.last)
# TEST
# p = Name('Dean', 'Jones')           #Name: Dean Jones
# p.first                             #'Dean'
# p.last                              #'Jones'
# p.fullname                          #'Dean Jones'
