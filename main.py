import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print (f"You chose {player} and computer chose {computer}.")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You Win. Congratulations!"
    else:
      return "Paper covers the rock! Unfortunately, computer wins this time."
  elif player == "paper":
    if computer == "scissors":
      return "Scissors cuts the paper! Unfortunately, computer wins this time."
    else:
      return "Paper covers the rock! You Win. Congratulations!"
  elif player == "scissors":
    if computer == "rock":
      return "Rock smashes scissors! Unfortunately, computer wins this time."
    else:
      return "Scissors cuts the paper! You Win. Congratulations!"

choices = get_choices()
      
      
      

age = 17
if age >= 18:
  print("You are an adult.")
elif age > 12:
  print("You are a teenager.")
elif age > 1:
  print("You are a child.")
else:
  print("You are a baby.")
