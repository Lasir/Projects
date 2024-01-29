
import random

def get_choices():
  player_choice=input("Enter a choice (rock,paper,sissors)")
  options = ["rock","paper","sissors"]
  computer_choice= random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return computer_choice

choices = get_choices()
print(choices)
