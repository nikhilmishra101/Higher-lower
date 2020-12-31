from game_data import data
import random
from replit import clear
from art import logo
from art import vs


def get_random_account():
  return random.choice(data)

def format_account(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name},a {description},from {country}"

def check(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_over = False
  account_a = get_random_account()
  account_b = get_random_account()
  while not game_over:
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
      account_b = get_random_account()
      print(f"Compare A: {format_account(account_a)}")
      print(vs)
      print(f"Compare B:{format_account(account_b)}")
      guess = input("Who has more followers? Type 'A' or 'B':").lower()
      account_a_followers = account_a["follower_count"]
      account_b_followers = account_b["follower_count"]
      is_correct = check(guess,account_a_followers,account_b_followers)

      clear()
      print(logo)
      if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
      else:
        game_over = True
        print(f"Sorry, that's wrong.Final score: {score}")


game()