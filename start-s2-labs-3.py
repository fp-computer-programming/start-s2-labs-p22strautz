# Author: SCT (AMDG) 2/1/22

def comes_after(st, letter): # Start defining of function
    letter = letter.lower() # makes sure input is lower case for no user error
    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha()) # combines all instancesc of letters that come after input in each test case

# test cases
print(comes_after("are you really learning Ruby?","r"))
print(comes_after("Katy Perry is on the radio!","r"))
print(comes_after("Pirates say arrrrrrrrr.","r"))
print(comes_after("r8 your friend","r"))