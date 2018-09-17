from Email import *


# TEST
e = Email('djones@email.com')       #Email: djones@email.com
e.address                           #'djones@email.com'
e.username                          #'djones'
e.domain                            #'email.com'
e.__dict__                          #{'address': 'djones@email.com', 'username': 'djones', 'domain': 'email.com'}

print('***********************************************************************************************')
print('TEST CLASS: Email')
print('Email1: ', e.__dict__)
print('---')
# TEST (DOMAIN)
print('Email2 (bad domain)(using custom EmailDomainError Exception...): ')
print('...try to create (Email) object with email (djones@email.ca) with INCORRECT DOMAIN.\n')
e2 = Email('djones@email.ca')        #Email name must contain a (.com, .org, .edu) domain name.
print('***********************************************************************************************')
