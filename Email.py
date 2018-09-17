# -------------------------------------------------------------
# CLASS: EMAIL
class Email():
    #constructor
    def __init__(self, address):
        try:
            #do all (Email) validations here (just do an isinstance(x, Email)) in other classes
            assert '@' in address, 'Email name must contain an @ symbol.'      #validation
            #assert '.org' in e or '.com' in e or '.edu' in e or '.ca' in e, 'Email name must contain a (.com, .edu, .org, .ca) domain name'      #validation
            if '.com' in address or '.org' in address or '.edu' in address:
                self.address = address
                #self.username = self.address.split('@')[0]              #not using (as change_email) does not update these field?
                #self.domain = self.address.split('@')[1]                #probably need to use (@property getters/setters)
            else:
                raise EmailDomainError('.com, .org, .edu')
        except EmailDomainError as err:
            print('EmailDomainError: Email name must contain a ({}) domain name.'.format(err.args[0]))		#OutOfStock ERROR: green
    #string representation
    def __repr__(self):
        return 'Email: {}'.format(self.address)
    #contains (x in string)
    def __contains__(self, x):
        return x in self.address
    #method change_email()
    def change_email(self, new_email):
        assert new_email != '', 'The email cannot be blank, try again.'     #validation
        assert '@' in new_email, 'Email must contain an @ symbol.'          #validation
        assert '.com' in new_email or '.org' in new_email or '.edu' in new_email, 'Email name must contain a (.com, .edu, .org) domain name'
        if str(new_email) == str(self.address):                             #test (email isn't the same as existing)
            print('This email is already updated.')
        else:
            self.address = new_email
            print('{} email has been updated'.format(self.address))
# TEST
# e = Email('djones@email.com')       #Email: djones@email.com
# e.address                           #'djones@email.com'
# e.username                          #'djones'
# e.domain                            #'email.com'
# TEST (DOMAIN)
# e = Email('djones@email.ca')        #Email name must contain a (.com, .org, .edu) domain name.
# e.change_email('')                  #AssertionError: The email cannot be blank, try again.
# e.change_email('abcd')              #AssertionError: Email must contain an @ symbol.
# e.change_email('abcd@email')        #AssertionError: Email name must contain a (.com, .edu, .org) domain name
# e.change_email('abcd@email.com')      #abcd@email.com email has been updated
# -------------------------------------------------------------
# CLASS: EMAIL DOMAIN (ERROR)
class EmailDomainError(Exception):
		  """
		  Email name must contain a (.com, .edu, .org) domain name
		  """
