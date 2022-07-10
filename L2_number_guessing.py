import random

min_number = 0
max_number = 10

secret_number = random.randint(min_number, max_number)

player_guess = input(f"Guess the secret number between {min_number} and {max_number}! ")

if(player_guess.isdigit()):
  # "5" -> 5
  # like a word that is red in color but says "blue"?
  
  player_guess = int(player_guess) 
  
  if(player_guess == secret_number):
    print("You win!")
  elif(player_guess > secret_number):
    print("Your number was too big! :(")
  else:
     print("Your number was too small! :(")
    
else:
  print("You didn't type a number! >:(")

# teach while loop then lists w/ for?