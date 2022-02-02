# Author: SCT (AMDG) 2/1/22

def double_every_other(lst): # Starts defining of function
    x = [] # Sets blank list for values to return to
    for i in range(len(lst)): # seperates index from input
        if i % 2 != 0: #if index is not even, double it and append it to results
            x.append(lst[i] * 2)
        else:
            x.append(lst[i]) # if index is even append it to list
    return x

# test cases
print(double_every_other([1,2,3,4]))