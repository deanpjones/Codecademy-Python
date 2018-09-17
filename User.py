from Name import *
from Email import *

# -------------------------------------------------------------
# CLASS: USER
class User:
    # constructor
    def __init__(self, name, email):
        assert isinstance(name, Name), 'Argument must be a (Name) object'           #validation
        self.name = name
        assert isinstance(email, Email), 'Argument must be an (Email) object.'      #validation (just test for (Email) object)
        self.email = email
        self.books = {}
        #self.average_rating = self.get_average_rating()
    # string representation
    def __repr__(self):
        return '\nUser\n  {0}\n  {1}\n  Number of books read: {3}\nBooks: {2}\n'.format(self.name, self.email, self.books, len(self.books))
    # equal operator (x == y)
    def __eq__(self, other):
        return str(self.name) == str(other.name) and str(self.email) == str(other.email)
    # method get_email() (I was going to omit this as I felt it was redundant) (use self.email.address)
    def get_email(self):
        return self.email.address
    # method (change email)
    def change_email(self, new_email):
        self.email.change_email(new_email)
    # def change_email(self, new_email):
    #     assert '@' in new_email, 'Email must contain an @ symbol.'  #validation
    #     if new_email == '':                                         #test (email isn't blank)
    #         print('The email cannot be blank, try again.')          #NOTE, this never fires (because AssertionError) happens first
    #     elif str(new_email) == str(self.email.address):             #test (email isn't the same as existing)
    #         print('This email is already updated.')
    #     else:
    #         self.email.address = new_email
    #         print('{} email has been updated'.format(self.get_email()))
    # method read_book()
    def read_book(self, b, rating='None'):
        self.books[b] = rating
        print('\n{} was added to the dictionary, with a rating: {}'.format(b.title, rating))
    # method get_average_rating() (User)
    def get_average_rating(self):
        if len(self.books) == 0:    #if NO BOOKS (yet read)
            return 'There are NO RATINGS (User) to average.'
        elif len(self.books) > 0:
            #return sum([v for k,v in self.books.items()]) / len(self.books)
            #modify (to handle RATING = 'None')(it will ignore in calc)
            rating_list = [v for k,v in self.books.items() if v != 'None' and v != None]
            r = sum(rating_list) / len(rating_list)
            return format(r, '.1f')

# TEST
# u = User(Name('Dean', 'Jones'), Email('djones@email.com'))
# b1 = Book('Harry Potter', ISBN(9780545010221))
# b2 = Book('Python: The Hard Way', ISBN(9780134692883))
# b3 = Book('FairyTaleLand', ISBN(9780134691111))
# u.get_average_rating()              #'There are NO RATINGS to average.'
# u.read_book(b1, 2)
# u.read_book(b2, 3)
# u.read_book(b3, None)
# u.books[b1]                         #return 2 (rating for b1 book)
# u.get_average_rating()              #2.5 (average rating for USER for all the books THEY READ)
# u.get_email()                       #'alan@turing.com'
# u.change_email('dj@email.com')      #EMAIL CLASS:  removed (email.username, email.domain)(because it wasn't auto updating here)

# # -------------------------------------------------------------
# # CLASS: USER (OLD, changed for DICTIONARY on BOOKS object)
# class User_old:
#     # constructor
#     def __init__(self, name, email, books):
#         assert isinstance(name, Name), 'Argument must be a (Name) object'           #validation
#         self.name = name
#         assert isinstance(email, Email), 'Argument must be an (Email) object.'      #validation (just test for (Email) object)
#         self.email = email
#         self.books = books
#     # string representation
#     def __repr__(self):
#         return '\nUser\n  {0}\n  {1}\n  Number of books read: {3}\nBooks: {2}'.format(self.name, self.email, self.books, len(self.books))
#     # equal operator (x == y)
#     def __eq__(self, other):
#         return str(self.name) == str(other.name) and str(self.email) == str(other.email)
#     # method get_email() (I ommitted using this as I felt it was redundant) (use self.email)
#     # method (change email)
#     def change_email(self, new_email):
#         assert '@' in new_email, 'Email must contain an @ symbol.'  #validation
#         if new_email == '':                                         #test (email isn't blank)
#             print('The email cannot be blank, try again.')          #NOTE, this never fires (because AssertionError) happens first
#         elif str(new_email) == str(self.email):                     #test (email isn't the same as existing)
#             print('This email is already updated.')
#         else:
#             self.email = new_email
#             print('{} email has been updated'.format(self.name))
# TEST
# u1 = User_old(Name('Dean', 'Jones'), Email('djones@email.com'), [Book('Harry Potter', ISBN(9780545010221)), Book('Python 3: The Hard Way', ISBN(9780134692883))])
# u1 = User_old(Name('Dean', 'Jones'), 'djones@email.com', [Book('book1'), Book('book2'), Book('book3')])
# #AssertionError: Must be an (Email) object.
# u1 = User_old(Name('Dean', 'Jones'), Email('djonesemail.com'), [Book('book1'), Book('book2'), Book('book3')])
# #AssertionError: Email must contain an @ symbol.
# u1.change_email('')                     #AssertionError: Email must contain an @ symbol.
# u1.change_email('djones@email.com')     #This email is already updated.
# u1.change_email('dean@hotmail.com')     #Dean Jones email has been updated
# # TEST (TWO USER OBJECTS)(EQUALITY)
# u3 = User_old(Name('Dean', 'Jones'), Email('djones@email.com'), [Book('book1'), Book('book2'), Book('book3')])
# u4 = User_old(Name('Dean', 'Jones'), Email('djones@email.com'), [Book('bk4'), Book('bk5'), Book('bk6')])
# u3 == u4                #True
# #change email (njones)
# u4 = User_old(Name('Dean', 'Jones'), Email('njones@email.com'), [Book('bk4'), Book('bk5'), Book('bk6')])
# u3 == u4            #False
# #change name (ean)
# u4 = User_old(Name('ean', 'Jones'), Email('djones@email.com'), [Book('bk4'), Book('bk5'), Book('bk6')])
# u3 == u4        #False
