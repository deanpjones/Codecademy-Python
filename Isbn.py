# -------------------------------------------------------------
# CLASS: ISBN
#   https://en.wikipedia.org/wiki/International_Standard_Book_Number
#   https://en.wikipedia.org/wiki/Check_digit
#   ISBN is 13 digits long
#   ISBN uses a CHECK DIGIT system to (avoid errors)
#      -errors can include (double-typed, flipped numbers, transposition, single-digit, twin, etc)
#   CHECK DIGIT (algorithm)
#   x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 + x13
#   - the thirteenth DIGIT (x13) is the MODULO (10) of the SUM (of the other 12 values)(evens are multiplied by 3)
#   - NOTE, it doesn't catch all errors, but eliminate a lot of (common human errors)
#   eg. ISBN-13 check digit of 978-0-306-40615-?
#       CHECK DIGIT is 7
#       s = 9×1 + 7×3 + 8×1 + 0×3 + 3×1 + 0×3 + 6×1 + 4×3 + 0×1 + 6×3 + 1×1 + 5×3
#        =   9 +  21 +   8 +   0 +   3 +   0 +   6 +  12 +   0 +  18 +   1 +  15
#        = 93
#        93 / 10 = 9 remainder 3
#        10 –  3 = 7
class ISBN():
    # constructor
    def __init__(self, isbn):
        assert isinstance(isbn, int), 'The ISBN argument needs to be a number (int).'                   #validation (for int)
        assert self.is_thirteen_digits(isbn), 'The ISBN argument needs to be 13 digits long.'           #validation (13 digits long)
        #assert check_digits(isbn), 'The ISBN may be incorrect, as the (check digit) does not match.'   #validation (check digit)(HOLD: unknown algorithm)
        self.isbn = isbn
    # string representation
    def __repr__(self):
        x = str(self.isbn)
        return 'ISBN: {}-{}-{}-{}-{}'.format(x[0:3], x[3:4], x[4:6], x[6:12], x[-1])
        #return 'ISBN: {}'.format(self.isbn)
    # equality (x == y)
    def __eq__(self, other):
        return self.isbn == other.isbn
    # hash (so we can use this object)(as a dictionary KEY)
    def __hash__(self):
        return hash(self.isbn)
        #isbn = ISBN(9780134692883)     #create object (to test)
        #hash(isbn)                     #9780134692883 (<-- if this returns a number, you can use ISBN object as KEY in dictionary)
        #dict = {}
        #dict[isbn] = 'my test for hash ISBN object'
        #dict                           #{ISBN: 978-0-13-469288-3: 'my test for ISBN object'}
    # method set_isbn()
    def set_isbn(self, new_isbn):
        assert isinstance(new_isbn, int), 'The ISBN argument needs to be a number (int).'                   #validation (for int)
        assert self.is_thirteen_digits(new_isbn), 'The ISBN argument needs to be 13 digits long.'           #validation (13 digits long)
        if new_isbn == self.isbn:                                 #test (ISBN isn't the same as existing)
            print('This ISBN is already updated.')
        else:
            self.isbn = new_isbn
            print('{} has been updated'.format(self))       #use (self) to get (__repr__) style format, instead of (self.isbn)
    # method count digits
    def count_digits(self, num):
        return len(str(num))
    # method test (is 13 digits long)
    def is_thirteen_digits(self, num):
        return self.count_digits(num) == 13
    # method check digit (way to verify the isbn)(*** may not work with all ISBN #'s as they could be using different WEIGHTS (formula) ***)
    def check_digit(self, test_isbn):          #I would be interested in doing this, but I think the (check digit) algorithm in not known (for isbn's)
        s = str(test_isbn)      #convert to string (for list comprehension)
        # formula (x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 + x13)
        # s = '9780306406157'
        odds = [int(x) for x in s][1::2]
        evens = [int(x) for x in s][0:-1:2]
        check_digit = [int(x) for x in s][-1]
        # do sum
        r = 3 * sum(evens) + sum(odds)      #103
        mod = r % 10                        #3
        check = 10 - mod                    #7
        return check == check_digit
        # 978-0-306-40615-?
        # test
        # check_digit('self', 9780306406157)            #True
# TEST
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
