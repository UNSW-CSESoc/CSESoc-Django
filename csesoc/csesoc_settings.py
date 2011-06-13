# nothing in this file is the real code that the website uses
# these passworde and keys are for testing purposes
DB_USERNAME = 'cse_auth'
DB_PASSWORD = 'dummy_password'

SETTINGS_SECRET_KEY = '0g$%0eu0flf(0o0n@k0al$h@0fo0@lk=s0obe0**@r+dupn00l'

# Only ever set to true in Development, this will always be false on the live site because setting
# this variable to true activates a back door that allows anyone access to the admin site without a
# password or any form of verification.
ADMIN_NO_LOGIN  = True

# Turn this on in production but for the here and now it just lets you send emails to non standard
# addresses instead so that you can debug email messages. Just a heads up, if you are on your local
# linux machine then your username@computer-name should send to your mailbox in /var/mail/username.
# For example I put 'robert@Shhnap' in the email fields when I am testing.
USE_REAL_EMAILS = False
MY_LOCAL_EMAIL = 'robert@Shhnap'  # This is purely for development purposes and will not be used if 
                                  # USE_REAL_EMAILS is True
