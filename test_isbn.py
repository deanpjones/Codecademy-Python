from Isbn import *


print('***********************************************************************************************')
print('TEST CLASS: Email')
isbn = ISBN(9780134692883)
print('isbn: ', isbn)
print('isbn.__dict__: ', isbn.__dict__)
print('isbn check digit (9780306406157): ', isbn.check_digit(9780306406157))
print('isbn check digit (false)(9780134692883): ', isbn.check_digit(isbn.isbn), '(this book must use a different algorithm?)')
isbn.set_isbn(1234567890123)
print('isbn.set_isbn(1234567890123): ', isbn)
print('----')
print('Assertion Errors...')
try:
    print('TEST: ISBN(123456)')
    ISBN(123456)
except AssertionError as err:
    print('AssertionError: The ISBN argument needs to be 13 digits long')
print('***********************************************************************************************')

# isbn = ISBN(9780134692883)                  #ISBN: 978-0-13-469288-3
# isbn.isbn                                   #9780134692883
# isbn.check_digit(9780306406157)             #True (example from Wikipedia link)
# isbn.check_digit(isbn.isbn)                 #False (this book must use a different algorithm?)
# # TEST (failures)
# isbn2 = ISBN(23423)
# # AssertionError: The ISBN argument needs to be 13 digits long.
# # TEST (set_isbn)
# isbn.set_isbn(1234567890123)                #ISBN: 123-4-56-789012-3 has been updated
# isbn.set_isbn(1234567890123)                #This ISBN is already updated.
