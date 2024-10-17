pword = input('Enter a password that consists of letters and numbers only')
if(len(pword) >= 8):
    twotypes = False
    if(pword.isdecimal() == False and pword.isalpha() == False):
        print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
