# Program: address_book.py
# Author: Jesse Tucker III
# Date: April 2023

# CHAPTER 10 PAGE 388, IN THE SPOTLIGHT 10-2

# Constants to control menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SAVE = 5

# 

def main():
    print()

    # A variable named filename that hold the name of the file.
    filename = 'phonebook.in'

    # A variable named read_mode that specifies which mode to
    # open the file in.
    read_mode = 'r'

    # An empty dictionary named phonebook.
    phonebook = {}

    # Opens a file for reading and assigns each line to the
    # phonebook dictionary as key value pairs.
    with open(filename, read_mode) as infile:
        lines = infile.readlines()

        # Assigns line 1 (index 0) as key, and line 2 (index 1)
        # as value to line 1 etc...
        phonebook[lines[0].rstrip()] = lines[1].rstrip()
        phonebook[lines[2].rstrip()] = lines[3].rstrip()
        phonebook[lines[4].rstrip()] = lines[5].rstrip()
        phonebook[lines[6].rstrip()] = lines[7].rstrip()
        phonebook[lines[8].rstrip()] = lines[9].rstrip()
        phonebook[lines[10].rstrip()] = lines[11].rstrip()

        choice = display_message()

        if choice == 1:
             look_up(phonebook)
        elif choice == 2:
             add()
        elif choice == 3:
             change()
        elif choice == 4:
             delete()
        elif choice == 5:
             save()


# This function display a menu to the user with 5 choices to
# choose from and returns that choice in the variable user_choice.
def display_message():
        print('Enter')
        print('1) look up an email address')
        print('2) add a new name and email address')
        print('3) change an email address')
        print('4) delete a name and email address')
        print('5) save address book and exit', end='')
        user_choice = int(input(':'))
        return user_choice

# This function ask the user for a name and then check if name exits
# in the phonebook. If name does not exits, it display a message.
# if name does exits, it display an email address.
def look_up(phonebook):
    name = input('Enter name: ')
    if name not in phonebook:
        print('Sorry, no contact exists under that name.')
    else:
         print(phonebook[name])

# Call the main funtion
main()
