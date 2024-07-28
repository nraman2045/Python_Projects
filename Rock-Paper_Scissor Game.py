import random

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

#Write your code below this line 👇
choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("You have given invalid input.")

print("Computer chooses  : ")

output = [rock, paper, scissors]
random_output = random.choice(output)
print(random_output)

if choice == "0":
    if random_output == rock:
        print("It's a Draw!")
    elif random_output == paper:
        print("You Lose!")
    elif random_output == scissors:
        print("You Win!")

if choice == "1":
    if random_output == paper:
        print("It's a Draw!")
    elif random_output == rock:
        print("You Win!")
    elif random_output == scissors:
        print("You Lose!")

if choice == "2":
    if random_output == scissors:
        print("It's a Draw!")
    elif random_output == paper:
        print("You Win!")
    elif random_output == rock:
        print("You Lose!")

print("\nGame End! Thank You for playing.\n")
