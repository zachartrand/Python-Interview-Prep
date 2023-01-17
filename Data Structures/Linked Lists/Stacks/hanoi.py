#!/usr/bin/env python3
from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks = dict(
    L = left_stack,
    M = middle_stack,
    R = right_stack
)

#Set up the Game
print()
num_disks = int(input("How many disks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n\n"))

for n in reversed(range(num_disks)):
    left_stack.push(n)

num_optimal_moves = 2**num_disks - 1
print(f"The fastest you can solve this game is in {num_optimal_moves} moves.")

#Get User Input
def get_input():
    choices = [key for key in stacks.keys()]
    user_input = ""
    while user_input not in choices:
        for stack in stacks.values():
            name = stack.get_name()
            letter = name[0]
            print(f"Enter {letter} for {name}")

        user_input = input().upper()

    return stacks[user_input]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n...Current Stacks...")
    for stack in stacks.values():
        stack.print_items()
    while True:
        print()
        print("Which stack do you want to move from?\n")
        from_stack = get_input()
        print()
        print("Which stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n")
            print("Invalid move. Try again.")
        elif (to_stack.is_empty()
              or to_stack.peek() > from_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n")
            print("Invalid move. Try again.")

print("\n\n...Final Stacks!...")
for stack in stacks.values():
    stack.print_items()
print("\n")

print(f"You completed the game in {num_user_moves} moves, ")
print(f"and the optimal number of moves is {num_optimal_moves}")
