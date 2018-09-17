# TOME RATER (BOOK RATINGS)
# PROJECT (CAPSTONE)
# CODE ACADEMY
# PROGRAMMING WITH PYTHON
# Dean Jones, Sep.15, 2018

# IMPORTS
from startup import *


# -------------------------------------------------------------
# CLASS: TOME RATER
class TomeRater():
    # ***************************************************************************
    # METHODS (DUNDER)
    # constructor
    def __init__(self):
        self.users = {}             #{email: UserObj, ...}{'email1': u1, 'email2': u2}
        self.books = {}             #{BookObj: count, ...}{b1: 1, b2: 2, b3: 1}
    # string representation
    def __repr__(self):
        #return 'This is the TOME RATER object.'
        s = ''
        s += '\n**************************************************************'
        s += '\nJoke: Why was Laura Croft sad?\n'
        s += '\n\t\t\t...because her career was in ruins!'
        s += '\n**************************************************************'
        return s
    # addition (+)(add two(2) TomeRater objects together)
    def __add__(self, other):
        # *** WARNING, (if there are DUPLICATE KEYS, the LAST DICTIONARY (KEY) will overwrite it) ***
        tr = TomeRater()
        #USERS
        tr.users = {**self.users, **other.users}        #Note, if two USERS have the same (email) the last one will overwrite
        #BOOKS
        overlap = {k:v+v2 for k,v in self.books.items() for k2,v2 in other.books.items() if k == k2}    #adds up the (books read)(if duplicate book)
        tr.books = {**self.books, **other.books, **overlap}
        return tr
    # equal (==)(if two TomeRater objects are compared)
    def __eq__(self, other):
        #users (same list of users)
        users = [x for x in self.users]         #list of (emails)
        users.sort()                            #make sure it's the same (order)
        #users (other)
        users2 = [x2 for x2 in other.users]
        users2.sort()
        #---
        #books (same list of books)
        books = [y for y in self.books]         #list of (books)
        books.sort()                            #make sure it's the same (order)
        #books (other)
        books2 = [y2 for y2 in self.books]
        books2.sort()
        #---
        return users == users2 and books == books2
    # ***************************************************************************
    # METHODS (CREATE BOOKS)
    # method create_book()
    def create_book(self, title, isbn):
        return Book(title, ISBN(isbn))
    # method create_novel() (fiction object)
    def create_novel(self, title, isbn, author):
        assert len(author.split()) == 2, 'The Author argument needs a first and last name.'     #validations (first and last name)
        return Fiction(title, ISBN(isbn), Name(author.split()[0], author.split()[1]))
    # method create_non_fiction()
    def create_non_fiction(self, title, isbn, subject, level):
        return NonFiction(title, ISBN(isbn), subject, level)
    # ***************************************************************************
    # METHODS (ADD USER)
    # method add_user()
    def add_user(self, name, email, books='No Books'):
        assert not email in self.users.keys(), 'The user ({}) already exists.'.format(email)
        #CREATE (User object)
        assert len(name.split()) == 2, 'The Name argument needs a first and last name.'     #validations (first and last name)
        u = User(Name(name.split()[0], name.split()[1]), Email(email))
        #add user (to self.users)
        self.users[email] = u
        #IF (books list) are in (optional argument)
        #TODO, this ADDS (rating = 'None')(what if I want USER RATINGS?)
        if books != 'No Books':
            #[self.add_book_to_user(email, b) for b in books]
            for b in books:
                print('Book: ', b)
                self.add_book_to_user(email, b)
        return u
    # ***************************************************************************
    # method (utility) (to get the KEY of DICTIONARY object)
    def get_key(self, dict, key_to_save):
        result = [x for x in dict if x == key_to_save]
        if result == []:
            return 'None'
        else:
            return result[0]
    def user_read_book(self, user, book, rating='None'):
        user.read_book(book, rating)                #update user (book and rating)
        print('user_read_book: ', ', ', book, ': ', rating)
    def book_update_count(self, book):
        if not book in self.books:
            self.books[book] = 1    #default (book count to 1)
            print('book_update_count: ', 1)
        else:
            self.books[book] += 1   #increment (book count)
            print('update_book_count: ', self.books[book])
    def book_update_rating(self, book, rating='None'):
        b = self.get_key(self.books, book)
        b.add_rating(rating)
        print('book_update_rating: ', rating)
    def add_book_to_user(self, email, book, rating='None'):
        user = self.users[email]                                        #get (User) from (self.users)
        #user_Alan = tr.users['alan@turing.com']
        #tr.add_book_to_user(user_Alan, book1, 1)
        if not user.email.address in self.users.keys():                 #check if (user exists)
            print('No user with ({})!'.format(user.email.address))
        else:
            self.user_read_book(user, book, rating)                      #update USER (book rating)
            self.book_update_count(book)                                 #update BOOK (count)
            self.book_update_rating(book, rating)                        #update BOOK (rating)
    # method add_book_to_user()
    # def add_book_to_user2(self, email, book, rating='None'):
    #     #CHECK, IF (email)(User exists)(TomeRater.users)
    #     #assert email in self.users.keys(), 'No user with ({})!'.format(email)
    #     if not email in self.users.keys():
    #         print('No user with ({})!'.format(email))
    #     else:
    #         #(User object) read_book(book, rating)
    #         u = self.users[email]           #get (User) OBJECT
    #         u.read_book(book, rating)       #update info (book and rating)
    #         #(Book OBJECT)
    #         #CHECK, IF book exists in (TomeRater.books)
    #         if not book in self.books:    #IF NOT (add book)(add value: 1 to start)
    #             #add book to (self.books)
    #             self.books[book] = 1            #VALUE (is the # of users)(who have read the book)
    #         else:                               #IF YES (count 1+)(count is tally of how many users have read it)
    #             b = [x for x in tr.books if x == book][0]       #get (Book object) from (self.books)
    #             #b = self.books[book]            #ERROR (returning value NOT KEY)(KEY is Book object)(AttributeError: 'int' object has no attribute 'add_rating')
    #             b.add_rating(rating)            #add rating (to book object)
    #             self.books[book] += 1           #book tally: increment (# of users who've read this book)
    # ***************************************************************************
    # METHODS (ANALYSIS)
    # method print_catalog()(prints all books)
    def print_catalog(self):
        if self.books == {}:
            print('*** There are (no books) to PRINT CATALOG. ***')
        else:
            print('\n**************************************************************')
            print('CATALOG (BOOKS)\n')
            for k in self.books:
                print(k)
            print('\n**************************************************************')
    # method print_users()
    def print_users(self):
        if self.users == {}:
            print('*** There are (no users) to PRINT USERS. ***')
        else:
            print('\n**************************************************************')
            print('USERS\n')
            for k in self.users:
                print(k)
            print('\n**************************************************************')
    # method most_read_book()
    def most_read_book(self):
        try:
            get_max = max([v for k,v in self.books.items()])    #do it this way (will return LIST if two are max)
            print('\n**************************************************************')
            print('MOST READ BOOK')
            print('This book has been read ({}) times.\n'.format(get_max))
            for k,v in self.books.items():
                if v == get_max:
                    print(k)
            print('**************************************************************')
        except ValueError:
            print('*** There are (no books read) to select a MOST READ BOOK. ***')
    # method highest_rated_book()
    def highest_rated_book(self):
        try:
            #[b.ratings for b in tr.books]                   #[['None', 1], ['None', 3], ['None', 3], [4], [1, 2, 4], [2]]
            #[b.get_average_rating() for b in tr.books]      #['1.0', '3.0', '3.0', '4.0', '2.3', '2.0']
            books = [b for b in self.books]
            ratings = [b.get_average_rating() for b in self.books]
            get_max = max(ratings)                          #'4.0'
            #which books (have the max rating)?
            max_books = [b for b,r in zip(books, ratings) if r == get_max]          #could be (more than one)
            print('\n**************************************************************')
            print('HIGHEST RATED BOOK')
            print('Book Average Rating: {}\n'.format(get_max))
            for b in max_books:
                print(b)
            print('**************************************************************')
        except ValueError:
            print('*** There are (no user ratings) to select a HIGHEST RATED BOOK. ***')
    # method most_positive_user()
    def most_positive_user(self):
        try:
            #[u.name.fullname for e,u in tr.users.items()]                          #['Alan Turing', 'David Marr', 'Marvin Minsky']
            #[u.get_average_rating() for e,u in tr.users.items()]                   #[2.4, 4.0, 2.0]
            user_names = [u.name.fullname for e,u in self.users.items()]
            ratings = [u.get_average_rating() for e,u in self.users.items()]
            get_max = max(ratings)                                                  #4.0
            #which users (have the max rating)?
            max_users = [u for u,r in zip(user_names, ratings) if r == get_max]          #could be (more than one)
            print('\n**************************************************************')
            print('MOST POSITIVE USER')
            print('User Average Rating: {}\n'.format(get_max))
            for u in max_users:
                print(u)
            print('**************************************************************')
        except (ZeroDivisionError, ValueError):
            print('*** There are (no user ratings) to select a MOST POSITIVE USER. ***')
    # ***************************************************************************
