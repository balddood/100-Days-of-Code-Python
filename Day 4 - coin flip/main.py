#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
import time

print("Coin flip in progress")
print("...")
time.sleep(3)

coin = random.randint(0, 1)

if coin == 0:
  print("Result: Tails")
else:
  print("Result: Heads")
