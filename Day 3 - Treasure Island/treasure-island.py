print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("\nYou are in a dark cave and can barely see ahead.\nAfter walking in the only direction you can for some time you come across two passages.\nWhich passage do you take? (L or R): ")
if direction.lower() == 'l' or direction.lower() == 'left':
  lake = input("\nYou notice light coming from the end of the pasage.\nAfter walking towards it you emerge from the cave on the bank of a large lake.\nYour map indicates the treasure is on an island in the lake that you can see in the distance.\nYou're a strong swimmer but there is also a small sailboat coming toward you.\nDo you wait for the boat or swim to the island? (swim or wait): ")
  if lake.lower() == 'w' or lake.lower() == 'wait':
    door = input("\nThe boat arrives at the shore where you're standing and the sailor is friendly.\nHe offers to ferry you to the island.\nUpon arriving at the island you approach a temple with a BLUE door, a RED door, and a YELLOW door.\nWhich door do you choose? (red, blue, or yellow): ")
    if door.lower() == 'y' or door.lower() == 'yellow':
      print("Congratulations! You have found the treasure and won the game.")
    elif door.lower() == 'r' or door.lower() == 'red':
      print("A ball of fire bursts from the flaming room and burns you alive.\nGAME OVER!")
    else:
      print("You have been eaten by rapid beasts.\nGAME OVER.")
  else: 
    print("You were attacked by sharks.\nGAME OVER.")
else:
  print("After walking for a few minutes you fall into a deep pit filled with spears.\nGAME OVER.")