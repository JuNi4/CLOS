import os
import sys
import json

# Import CLOS Utils
f = open(os.path.dirname(os.path.realpath(__file__))+'/dirs.json', 'r')
dirs = json.loads(f.read())
f.close()

sys.path.append(dirs['LIB_DIR'])

# Read user_data
f = open(dirs['DATA_DIR']+'/settings.json', 'r')
pdata = json.loads(f.read())
f.close()

import clos_utils

# Custome print
print = clos_utils.text_style.typinganimation

#print('Welcome to some good old dialog! Your goal is simple: answer the questions. There is no right or wrong answer, Just answer the question.')
print('Let\'s start with a simple question: What is your name?')
x = input('> ')
print(f'Hello {x}!')

print('Now, the second question: What is your favorite colour?')
x = input('> ')
# Check if favourite color is same as set as clos value
if str(x).lower() == str(pdata['fav_color'].lower()):
    print(f'Although I said there where no right or wrong answer, you answered.......     correctly! This is because you set {x} as your favourite color while setting up CLOS.')
else:
    print(f'Although I said there where no right or wrong answer, you answered.......     wrongly! This is because you set {pdata["fav_color"]} as your favourite color while setting up CLOS. Not {x}. I\'m sorry, but your answer was wrong!')
