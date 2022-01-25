# Author: SCT (AMDG) 1/25/12

def smash(lst): # Defines function
    sentence = "" # Creates empty string to add inputs to for final result
    for i, v in enumerate(lst): # Seperate inputs by there index and value to be used later
        if i == 0: # the first input of the function will always be added straight to the result list
            sentence = sentence + v
        else:
            sentence = sentence + " " + v # any inputs that come after are added with a space in between

    return sentence # returns final output back to function

# Test Case
print(smash(["I", "love", "all", "foods"]))
