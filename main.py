import random

def menu (): 
  # ask player for number
  user_numbers = get_player_number

  # Calculate Lottery numbers
  lottery_numbers = create_lottery_numbers

  # Print out the winnings
  matched_numbers = user_numbers.intersection(lottery_numbers)
  print("you matched {}. you won £{}!". format(matched_numbers, 100 ** len(matched_numbers)))

# User can pick 6 numbers 
def get_player_number():
  number_csv = input("Enter your 6 numbers, separated by commas: ")
  # Now, I want to create a set of integers from this number_csv
  number_list = number_csv.split(",") # ['1','2','3','4']
  integer_set = {int(number) for number in number_list}
  return integer_set

# so at the moment we have only just got the user to pick out 6 numbers. 

# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
  values = set () # Cannot use {} in python
  while len(values) < 6: #range in [0,1,2,3,4,5]
#while loop will carry on giving out 6 numbers as stated above.
    values.add(random.randint(1,20))
  return values

# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched


print(menu())