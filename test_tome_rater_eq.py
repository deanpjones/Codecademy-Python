from TomeRater import *

import io
import sys

# ----------------------------------------------------------------------------
# TOME RATER (EQUALITY)(__eq__)(==)(COMPARE EQUALITY ON TWO TomeRater OBJECTS)

# trap printout (START) *************************
trap = io.StringIO()
sys.stdout = trap

# OBJECT#1
tr1 = TomeRater()

book1 = tr1.create_book("Society of Mind", 1234512345678)
novel1 = tr1.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")
nonfiction1 = tr1.create_non_fiction("Automate the Boring Stuff", 1234561929452, "Python", "beginner")

tr1.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])

# OBJECT#2
tr2 = TomeRater()

book2 = tr2.create_book("Society of Mind", 1234512345678)
novel2 = tr2.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")
nonfiction2 = tr2.create_non_fiction("Automate the Boring Stuff", 1234561929452, "Python", "beginner")

tr2.add_user("Marvin Minsky", "marvin@mit.edu", books=[book2, novel2, nonfiction2])

# trap printout (END) *************************
sys.stdout = sys.__stdout__

# COMPARE OBJECTS (SHOULD RETURN TRUE)
print('***********************************************************************************************')
print('TEST: COMPARE EQUALITY ON TWO TomeRater OBJECTS')
print('Object#1: --------------------')
tr1.print_catalog()
tr1.print_users()
print('Object#2: --------------------')
tr2.print_catalog()
tr2.print_users()
print('Comparison (should be EQUAL): --------------------')
print('Is (tr1) equal to (tr2): ', tr1 == tr2)
print('Add another USER and retest...')
tr1.add_user("Alan Turing", "alan@turing.com")           #add user
tr1.add_book_to_user('alan@turing.com', book1, 1)       #add book (to user)
print('Comparison (should be NOT EQUAL): --------------------')
print('Is (tr1) equal to (tr2): ', tr1 == tr2)
print
