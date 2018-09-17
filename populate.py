from TomeRater import *


# TESTING (for TomeRater.py)
# Dean Jones, Sep.15, 2018

# This file has been modified to run 
#   The order of attributes is a bit different 
#   The ISBN number (class) I added (requires 13 digits)
#   There where some inconsistencies (with the naming)(between the INSTRUCTIONS and THIS FILE) calling methods



#CREATE OBJECT (TomeRater)
tr = TomeRater()


#CREATE BOOKS
book1 = tr.create_book("Society of Mind", 1234512345678)										#All (ISBN) (require 13 digits)
novel1 = tr.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")		
#novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.isbn.set_isbn(9781536831139)															
#novel1.set_isbn(9781536831139)
nonfiction1 = tr.create_non_fiction("Automate the Boring Stuff", 1234561929452, "Python", "beginner")
#nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = tr.create_non_fiction("Computing Machinery and Intelligence", 1234511111938, "AI", "advanced")
#nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = tr.create_novel("The Diamond Age", 1234510101010, "Neal Stephenson")
#novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = tr.create_novel("There Will Come Soft Rains", 1234510001000, "Ray Bradbury")
#novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)


#CREATE USERS
tr.add_user("Alan Turing", "alan@turing.com")
tr.add_user("David Marr", "david@computation.org")


#Add USER (with BOOKS ARGUMENT)
tr.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])
#tr.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])		#(User ARGUMENT user_books (DOESN'T EXIST))


#Add BOOK (Alan Turing)
tr.add_book_to_user('alan@turing.com', book1, 1)            #['None', 1]						#(switched the order of arguments)
tr.add_book_to_user('alan@turing.com', novel1, 3)           #['None', 3]
tr.add_book_to_user('alan@turing.com', nonfiction1, 3)      #['None', 3]
tr.add_book_to_user('alan@turing.com', nonfiction2, 4)      #[4]
tr.add_book_to_user('alan@turing.com', novel3, 1)           #[1]
#tr.add_book_to_user(book1, 'alan@turing.com', 1)  
#tr.add_book_to_user(novel1, "alan@turing.com", 3)
#tr.add_book_to_user(nonfiction1, "alan@turing.com", 3)
#tr.add_book_to_user(nonfiction2, "alan@turing.com", 4)
#tr.add_book_to_user(novel3, "alan@turing.com", 1)

#Add BOOK (Marvin Minsky)
tr.add_book_to_user('marvin@mit.edu', novel2, 2)            #[2]								#(switched the order of arguments)
tr.add_book_to_user('marvin@mit.edu', novel3, 2)            #[1, 2]
#tr.add_book_to_user(novel2, "marvin@mit.edu", 2)
#tr.add_book_to_user(novel3, "marvin@mit.edu", 2)

#Add BOOK (David Marr)
tr.add_book_to_user('david@computation.org', novel3, 4)     #[1, 2, 4]							#(switched the order of arguments)
#tr.add_book_to_user(novel3, "david@computation.org", 4)


#TEST (print analysis functions)
tr.print_catalog()					# tr.print_catalog()
tr.print_users()					# tr.print_users()
tr.most_read_book()					# print(tr.get_most_read_book())							#(inconsistent METHOD NAME (most_read_books))
tr.highest_rated_book()				# print(tr.highest_rated_book())
tr.most_positive_user()				# print(tr.most_positive_user())


