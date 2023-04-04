# Program: address_book.py
# Author: Jesse Tucker III
# Date: April 2023

# Constants for the menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SAVE = 5

# 
def main():
    # A variable named filename that hold the name of the file.
    filename = 'phonebook.in'

    # A variable named read_mode that specifies which mode to
    # open the file in.
    read_mode = 'r'

    # An empty dictionary named phonebook.
    phonebook = {}

    # Opens a file for reading and assigns each line to the
    # phonebook dictionary as key value pairs.
    infile = open(filename, read_mode)
    lines = infile.readlines()

    # Assigns line 1 (index 0) as key, and line 2 (index 1)
    # as value to line 1 etc...
    phonebook[lines[0].rstrip()] = lines[1].rstrip()
    phonebook[lines[2].rstrip()] = lines[3].rstrip()
    phonebook[lines[4].rstrip()] = lines[5].rstrip()
    phonebook[lines[6].rstrip()] = lines[7].rstrip()
    phonebook[lines[8].rstrip()] = lines[9].rstrip()
    phonebook[lines[10].rstrip()] = lines[11].rstrip()

    # A variable that holds the user's choice.
    choice = 0

    while choice != SAVE:
        # Display the menu choices.
        choice = get_menu_choice()

        # Evalutes the user's choice and call a specific function
        # for that choice.
        if choice == LOOK_UP:
            look_up(phonebook)
        elif choice == ADD:
            add(phonebook)
        elif choice == CHANGE:
            change(phonebook)
        elif choice == DELETE:
            delete(phonebook)
        elif choice == SAVE:
            save(phonebook)

# This function display a menu to the user with 5 choices to
# choose from, validates that choice, then returns that choice
# in the variable choice.
def get_menu_choice():
    print()
    # Display menu.
    print('Enter')
    print('1) look up an email address')
    print('2) add a new name and email address')
    print('3) change an email address')
    print('4) delete a name and email address')
    print('5) save address book and exit', end='')

    # Get choice from user.
    choice = int(input(':'))
    
    # Validates the choice.
    while choice < LOOK_UP or choice > SAVE:
        choice = int(input('Enter a valid choice: '))
    
    # Return the choice.
    return choice

# The look_up function gets a name and check if name exits
# in the phonebook. If name does not exits, it display a message.
# if name does exits, it display an email address.
def look_up(phonebook):
    # Get name from user.
    name = input('Enter name:')
    # Validate that the name exits in phonebook.
    if name not in phonebook:
        print('Sorry, no contact exists under that name.')
    else:
        print(phonebook[name])

# The add function adds a name and email address to the
# phonebook.
def add(phonebook):
    # Get name from user.
    name = input('Enter name:')
    # Get email address from user.
    email = input('Enter email:')

    # Checks if name not in phonebook before adding it.
    if name not in phonebook:
        phonebook[name] = email

# The change function changes the email address of a
# name in the phonebook.
def change(phonebook):
    # Get the name to look up.
    name = input('Enter name:')

    # if name is in phonebook, get new email address,
    # then update the email.
    if name in phonebook:
        email = input('Enter new email:')
        phonebook[name] = email

# The delete function delete an item from the phonebook.
def delete(phonebook):
    # Get the name to look up.
    name = input('Enter name:')

    # if name exits, delete it from phonebook.
    if name in phonebook:
        del phonebook[name]

# The save function save changes made to a file.
def save(phonebook):
    # Output filename stored in variable filename.
    filename = 'phonebook.out'
    # The write file mode stored a variable.
    write_mode = 'w'
    # Open file for writing.
    outfile = open(filename, write_mode)

    # Writes changes to file.
    for key in phonebook:
        outfile.writelines(key + '\n' + phonebook[key] + '\n')

    # Close the file.
    outfile.close()

# Call the main funtion
main()
