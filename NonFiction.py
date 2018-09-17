from Book import *

# -------------------------------------------------------------
# CLASS: NON-FICTION
class NonFiction(Book):
    # constructor
    def __init__(self, title, isbn, subject, level):
        #Book.__init__(self, title, isbn)                #same as calling (super())(explicit)
        super().__init__(title, isbn)                    #(implicit)
        assert isinstance(subject, str), 'The Subject argument needs to be a string (str).'
        self.subject = subject
        assert isinstance(level, str), 'The Level argument needs to be a string (str).'
        self.level = level
    # string representation
    def __repr__(self):
        s = self.level
        # test (to fix grammer)('a' versus 'an')(if self.level starts with a vowel)
        if s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or s[0] == 'o' or s[0] == 'u':
            return '{title}, an {level} manual on {subject}'.format(title=self.title, subject=self.subject, level=self.level)
        else:
            return '{title}, a {level} manual on {subject}'.format(title=self.title, subject=self.subject, level=self.level)
    # hash
    def __hash__(self):
        return hash((self.title, self.isbn, self.subject, self.level))
    # method get_subject()
    def get_subject(self):
        return 'Subject: {}'.format(self.subject)
    # method get_level()
    def get_level(self):
        return 'Level: {}'.format(self.level)

# TEST
# nf = NonFiction('Harry Potter', ISBN(9780545010221), 'Ancient Magic', 'authentic')
# nf                      #Harry Potter, an authentic manual on Ancient Magic
# nf2 = NonFiction('Python 3: The Hard Way', ISBN(9780545010221), 'Programming', 'complex')
# nf2                     #Python 3: The Hard Way, a complex manual on Programming
# nf.subject              #'Ancient Magic'
# nf.level                #'authentic'
# nf.get_subject()        #'Subject: Ancient Magic'
# nf.get_level()          #'Level: authentic'
