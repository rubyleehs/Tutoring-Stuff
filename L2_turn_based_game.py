import random

### reminder to self: teach arrays, for/while loops, index/len() and string interpolation first!

#assigning some variables
player_hp = 10

enemy_name = None
enemy_hp = 0

enemy_min_hp = 3
enemy_max_hp = 7
enemy_min_attack = 1
enemy_max_attack = 4
possible_enemy_name = ["Zombie","Spider","Vampire"]

player_min_attack = 1
player_max_attack = 4
possible_player_actions = ["Attack", "Defend", "Nothing"]

# game loop
while(player_hp > 0):
  # Spawn new enemy if no enemy
  if(enemy_name == None): 
    random_enemy_index=random.randint(0, len(possible_enemy_name)-1)
    enemy_name = possible_enemy_name[random_enemy_index]
    enemy_hp = random.randint(enemy_min_hp, enemy_max_hp)
    print(f'A {enemy_name} appeared!')

  # What will the enemy do?
  enemy_action = None
  if(random.randint(0, 100) > 50):
    enemy_action = "a"
    print(f"The {enemy_name} is preparing to attack!")

  # Print combat stats and ask what the player want to do.
  print("=======================")
  print(f"Your Hp: {player_hp} | Enemy Hp: {enemy_hp}")
  print(f"Available Options: {possible_player_actions}")
  
  player_action = None
  while(player_action == None):
    player_input = input("What do you do? ").lower()
    
    # Loop though all possible player actions and check against it to see if player input is a valid action
    for possible_player_action in possible_player_actions:
      if(player_input == possible_player_action.lower() or player_input == possible_player_action[0].lower()):
        player_action = possible_player_action[0].lower()

    # If invalid action, print that it is invalid
    if(player_action == None):
      print("That is not a valid action!")
  print("=======================")

  # Perform player action 
  if(player_action=="a"):
    player_damage = random.randint(enemy_min_attack, enemy_max_attack)
    enemy_hp = enemy_hp - player_damage
    print(f"You attacked the {enemy_name} for {player_damage} points of damage!")
  elif(player_action=="d"):
    print("You defended!")
  elif(player_action=="n"):
    print("You did nothing!")

  # Perform enemy action if enemy is still alive
  if(enemy_hp <= 0):
    print(f"You defeated the {enemy_name}! :D \n")
    enemy_name=None
  elif(enemy_action=="a"):
    if(player_action=="d"):
      print(f"The {enemy_name} attacked but you sucessfully defended against it!")
    else:
      enemy_damage = random.randint(enemy_min_attack, enemy_max_attack)
      player_hp = player_hp - enemy_damage
      print(f"The {enemy_name} attacked you for {enemy_damage} points of damage!")

# The only way (so far) to exit the game loop is to die
print("You died! :(")

### lesson 3: functions, maybe dictionaries?
### lesson 4: classes?
### lesson 5: visual stuff?