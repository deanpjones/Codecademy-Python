from Book import *
from Name import *

# -------------------------------------------------------------
# CLASS: FICTION
class Fiction(Book):
    # constructor
    def __init__(self, title, isbn, author):
        Book.__init__(self, title, isbn)                #same as calling (super())(explicit)
        #assert isinstance(author, str), 'The Author argument needs to be a string (str).'
        assert isinstance(author, Name), 'The Author argument needs to be a Name object (Name).'
        self.author = author.fullname
    # string representation
    def __repr__(self):
        return '{title} by {author}'.format(title=self.title, author=self.author)
    # hash
    def __hash__(self):
        return hash((self.title, self.isbn, self.author))
    # method get_author()
    def get_author(self):
        return 'Author: {}'.format(self.author)
    # method (print all book info)
    def print_info(self):
        s = ''
        s += Book.__repr__(self).replace('Book', 'Book: Non-Fiction')       #get Book object string (update to Non-Fiction in header)
        s += '\n  Author: {}'.format(self.author)                           #append Author (to end of string)
        print(s)

# TEST
# #fic = Fiction('Harry Potter', ISBN(9780545010221), 'Dean Jones')
# fic = Fiction('Harry Potter', ISBN(9780545010221), Name('Dean', 'Jones'))
# fic                         # Harry Potter by Dean Jones
# fic.get_author()            #'Author: Dean Jones'
# fic.author                  #'Dean Jones'
# fic.print_info()
# # Book: Non-Fiction
# #   Title: Harry Potter
# #   ISBN: 978-0-54-501022-1
# #   Ratings: []
# #   Author: Dean Jones
# fic2 = Fiction('Harry Potter', ISBN(9780545010221), 'Dean Jones')
# # AssertionError: The Author argument needs to be a Name object (Name).
