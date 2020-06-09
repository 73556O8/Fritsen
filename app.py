'''
Fritsen Drinking Game
73556O8
'''



# imports
import dice
from funcs import *

import time
import sys
import random

sys.path.append(sys.path.append("/home/dylan/code/Fritsen/venv/bin/python3"))

from tqdm import tqdm

# variables
mylist = [1,2,3,4,5,6,7,8]


# main menu
print('''
---------------------------------------------------

    HEEEEEUUUUUUJ LEKKER FRITSEN
         GRAP YOUR DRINK AND ENJOY!

      ########        ##########
      **********     $$$$$$$$$$$
      ********  **  $$  $$$$$$$$
      ********  **  $$  $$$$$$$$
      ******** **    $$ $$$$$$$$ 
       *********      $$$$$$$$$

---------------------------------------------------\n
Python 3.6.9                                73556O8
''')

### This is the loading bar
for i in tqdm(mylist):
    time.sleep(1)

clear()

main = input('''
---------------------------------------------------
                M A I N     M E N U
---------------------------------------------------
                    (a) Start
                    (b) Settings
                    (c) Dices

                    > ''')

if main == "a":
    clear()
    amountPlayers()
    playerNames()
    sips = int(input("\n\t\tAmount of points per sip: "))
elif main == "b":
    clear()
    settings()
elif main != "a" or "b":
    print("\n\t\tError 422: input not valid")
else:
    print("\n\t\tJeez, you're drunk. Go to bed.")
    sys.exit(1)

clear()
starter = random.choice(names)
print(f"\n\t\t{starter} starts!")

turn = input('''
\n\t\t[ENTER] to throw
  \t\t(score) for scoreboard
  \t\t(quit) to terminate the game
''')

if turn == "":
    throw()
elif turn == "score":
    score()
elif turn == "quit":
    quit()