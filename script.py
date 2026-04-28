# Fortune Cookie Python Script

# Libraries

import random

# Variables

fortunes = open('fortunes.txt').read().strip().split('\n')

# Functions

def printRandomFortune():
    print(random.choice(fortunes))

printRandomFortune()

input("Press Enter to exit...")

# End of script