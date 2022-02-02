# Author: SCT (AMDG) 1/25/22

last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
# List of initals and rows to be combined
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

index = 0 # Set a base value to start at for index to create a counting system

for row in rows:
    for name in (row): # Sets a loop to iterate by each name in a row
        print("{0} {1}".format(name, last_initials[index])) # Function prints the name in iteration + the corresponding inital by index
        index += 1 # Index counter for each iteration to keep list lined up