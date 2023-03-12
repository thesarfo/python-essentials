# This is an insecure password locker program

PASSWORDS = {'email': 'F7min1Bddjghalslfashfhag', 'bog': 'vmanala57jfjEHENNajklja', 'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There is no accoount named " + account)
    
# This program takes an account name as a command line argument, checks if it is present in a dictionary of passwords called PASSWORDS, 
# and if so, copies the password to the clipboard using the pyperclip module.

# If the script is run with no arguments or with an account name that is not in the PASSWORDS dictionary,
# it will print a usage message or an error message, respectively.
