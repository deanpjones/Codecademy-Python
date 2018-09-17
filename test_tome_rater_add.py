from TomeRater import *


#TEST (CONCATENATION)(+)(__add__)(with + operator)

# ------------------------------------------
# TOME RATER (OBJECT#2)(default from populate.py)
#CREATE OBJECT (TomeRater)
tr = TomeRater()

#CREATE BOOKS
book1 = tr.create_book("Society of Mind", 1234512345678)										#All (ISBN) (require 13 digits)
novel1 = tr.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")
novel1.isbn.set_isbn(9781536831139)
nonfiction1 = tr.create_non_fiction("Automate the Boring Stuff", 1234561929452, "Python", "beginner")
nonfiction2 = tr.create_non_fiction("Computing Machinery and Intelligence", 1234511111938, "AI", "advanced")
novel2 = tr.create_novel("The Diamond Age", 1234510101010, "Neal Stephenson")
novel3 = tr.create_novel("There Will Come Soft Rains", 1234510001000, "Ray Bradbury")

#CREATE USERS
tr.add_user("Alan Turing", "alan@turing.com")
tr.add_user("David Marr", "david@computation.org")

#Add USER (with BOOKS ARGUMENT)
tr.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])

#Add BOOK (to users)
tr.add_book_to_user('alan@turing.com', book1, 1)
tr.add_book_to_user('alan@turing.com', novel1, 3)
tr.add_book_to_user('alan@turing.com', nonfiction1, 3)
tr.add_book_to_user('alan@turing.com', nonfiction2, 4)
tr.add_book_to_user('alan@turing.com', novel3, 1)
tr.add_book_to_user('marvin@mit.edu', novel2, 2)
tr.add_book_to_user('marvin@mit.edu', novel3, 2)
tr.add_book_to_user('david@computation.org', novel3, 4)
# ------------------------------------------

# ------------------------------------------
# TOME RATER (OBJECT#1)
# TEST (ADD TWO TOME RATER OBJECTS)
# create new object
tr1 = TomeRater()
# add user
tr1.add_user("Dean Jones", "djones@email.com")
# create books
b1 = Book('Harry Potter', ISBN(9780545010221))
b2 = Book('Python: The Hard Way', ISBN(9780134692883))
# add books to user
tr1.add_book_to_user('djones@email.com', b1, 1)
tr1.add_book_to_user('djones@email.com', b2, 4)
tr1.add_book_to_user('djones@email.com', novel3, 3)            #add same book (test ADD OPERATOR **overlapping**)
# ------------------------------------------

#TEST (CONCATENATION)(+)(__add__)(with + operator)
tr2 = tr + tr1


print('***********************************************************************************************')
print('TEST: TomeRater: Concatenation of two TomeRater OBJECTS')
print('TomeRater object (to add): ')
print(tr1.__dict__)
print('---')
print('...added to DEFAULT (from populate.py file)')
print(tr2.__dict__)
print('***********************************************************************************************')
tr2.print_users()
print('MOST READ BOOK, was (3) time for: There Will Come Soft Rains by Ray Bradbury')
print('...see if this is (4)?')
tr2.most_read_book()
