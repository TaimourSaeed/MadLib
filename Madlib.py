# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

# importint he time module to add a delay later on in the module to help flow.
import time

print('Welcome to my Git! \nThis is the my first real bit of python code where \ni\'ve experimented with some string to write a MadLib, Enjoy! \n')

# wrote this while statement which can be easily reused across different scripts and it includes error handling
print('Start New MadLib?')

# have to .upper the input as y != Y in python
start_game = input('Enter "Y" for yes. \nEnter "N" for no. \n:').upper()

# ensures user can only enter either Y/N
while start_game not in ('Y','N'):
    print(f'Your value: {start_game} does not match either option, Try again')
    start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()

while start_game == 'Y':
    print('Please enter the following:')
    age = input('Age:')
    adjective1 = input('Adjective:')
    town = input('Towm:')
    colour_eyes = input('Eye Colour:')
    cword = input('Coolest word you can think of:')

    # using f string to add in variables
    madlib = f'\n{age} years ago, somewhere in the universe on a remote and {adjective1} planet known as {town}, sealed in an ancient tomb a pair of {colour_eyes} eyes opened and what will in future generations be referred to as \'The {cword}\' began.\n' 

    print(madlib)

    time.sleep(5)

    print ('do you want to restart the MadLib?')
    start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()
        
    while start_game not in ('Y','N'):
        print(f'Your value: {start_game} does not match either option, Try again')
        start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()

print('Thanks! Goodbye.')

# %%



