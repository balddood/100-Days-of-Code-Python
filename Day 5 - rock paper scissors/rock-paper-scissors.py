rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = int(input("What do you choose? (0 = Rock, 1 = Paper, 2 = Scissors): "))
cpu = random.randint(0,2)

choices = [rock, paper, scissors]

print(f"You chose...{choices[player]}")
print(f"The CPU chose...{choices[cpu]}")

if player == 0 and cpu == 1:
  print("You lose!")
elif player == 1 and cpu == 2:
  print("You lose!")
elif player == 2 and cpu == 0:
  print("You lose!")
elif player == cpu:
  print("It's a draw!")
else:
  print("You win!")
