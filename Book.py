from Isbn import *

# -------------------------------------------------------------
# CLASS: BOOK
class Book:
    # constructor
    def __init__(self, title, isbn):
        assert isinstance(title, str), 'The Title argument needs to be a string (str).'
        self.title = title
        assert isinstance(isbn, ISBN), 'The ISBN argument needs to be an ISBN object (ISBN).'
        self.isbn = isbn
        self.ratings = []
    # string representation (good string for KEY in Tome Rater object)
    def __repr__(self):
        return '<Book: {}>'.format(self.isbn)
    # def __repr__(self):
    #     return '\n  Book\n    Title: {}\n    {}\n    Ratings: {}'.format(self.title, self.isbn, self.ratings)
    # equality (x == y)
    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn
    # less than (<)(mylist.sort())
    def __lt__(self, other):
        return self.title < other.title
    # hash (so we can use this object)(as a dictionary KEY)
    # NOTE, (ISBN object needs __hash__ method too)
    def __hash__(self):
        return hash((self.title, self.isbn))
        #b = Book('Harry Potter', ISBN(9780545010221))     #create object (to test)
        #hash(b)                     #6734503495428416798 (<-- if this returns a number, you can use BOOK object as KEY in dictionary)
        #dict = {}
        #dict[b] = 'my test for hash BOOK object (that has NESTED ISBN object)'
        #dict[b]                    #'my test for hash BOOK object (that has NESTED ISBN object)'
    # method get_title()
    def get_title(self):
        return 'Title: {}'.format(self.title)
    # method get_isbn() (I was going to omit this as I felt it was redundant) (use self.isbn)(uses ISBN object __repr__)
    def get_isbn(self):
        return self.isbn
    # method set_isbn() (see ISBN object for method)
    def set_isbn(self, new_isbn):
        self.isbn.set_isbn(new_isbn)
    # def set_isbn(self, new_isbn):
    #     assert isinstance(new_isbn, ISBN), 'The ISBN argument needs to be an ISBN object (ISBN).'
    #     if new_isbn == self.isbn:                                 #test (ISBN isn't the same as existing)
    #         print('This ISBN is already updated.')
    #     else:
    #         self.isbn = new_isbn
    #         print('{} has been updated'.format(self.isbn))
    # method add_rating()
    def add_rating(self, rating):
        if rating == 'None':
            self.ratings.append(rating)
            print('A rating ({}) was added to the book "{}".'.format(rating, self.title))
        else:
            assert isinstance(rating, int), '......The rating argument needs to be a number (int).'
            if not 0 <= rating <= 4:
                print('Invalid Rating, it must be between (0-4).')
            else:
                self.ratings.append(rating)
                print('A rating ({}) was added to the book "{}".'.format(rating, self.title))
    # method get_average_rating()
    def get_average_rating(self):
        #list if (self.ratings) has ('None') element (eg. self.ratings = ['None', 2, 3])
        ratings_list = [x for x in self.ratings if x != 'None' and x != None]             #strips out ('None' or NoneType) occurence from list
        #if len(self.ratings) == 0:
        if len(ratings_list) == 0:
            return 'There are NO RATINGS (Book) to average.'
        #elif len(self.ratings) > 0:
        elif len(ratings_list) > 0:
            #return sum([x for x in self.ratings]) / len(self.ratings)
            r = sum(ratings_list) / len(ratings_list)
            return format(r, '.1f')
        else:
            print('Something went wrong: Book.get_average_rating()')
    # method print info
    def print_info(self):
            print('\n  Book\n    Title: {}\n    {}\n    Ratings: {}'.format(self.title, self.isbn, self.ratings))
#TEST
# b = Book('Harry Potter', ISBN(9780545010221))
# # <Book: ISBN: 978-0-54-501022-1>
# b.print_info()
# # Book
# #   Title: Harry Potter
# #   ISBN: 978-0-54-501022-1
# #   Ratings: []
# b.get_title()                       #'Title: Harry Potter'
# b.title                 #'Harry Potter'
# b.isbn                  #ISBN: 978-0-54-501022-1
# b.isbn.isbn             #9780545010221
# # TEST (equality)
# b1 = Book('Harry Potter', ISBN(9780545010221))
# b2 = Book('Harry Potter', ISBN(9780545010221))
# b1 == b2            #True
# # TEST (rating)
# b.add_rating(5)
# # Invalid Rating, it must be between (0-4).
# b.add_rating(3)
# # A rating (3) was added to the book "Harry Potter".
# # TEST ('None' rating)
# b.add_rating('None')
# # TEST (set isbn)
# b.set_isbn(ISBN(1234567890123))
# # ISBN: 123-4-56-789012-3 has been updated
# b.set_isbn(ISBN(1234567890123))
# # This ISBN is already updated.
# # TEST (failures)
# b2 = Book('Harry Potter', 9780545010221)
# # AssertionError: The ISBN argument needs to be an ISBN object (ISBN).
# # SET ISBN (from Book object)
# b.isbn.set_isbn(1234567890123)          #ISBN: 123-4-56-789012-3 has been updated
# b.ratings                               #[1, 2, 3]
# b.get_average_rating()                  #2.0
