from random import randint


# Create answer range: 1 to 100(integer)
answer = randint(1,100)
# Print answer(for debugging)
print(answer)

# Get user's name, guess
user_name = input('Hello, there! What is your name? ')
guess = int(input(f'Hello, {user_name}! Guess a number between 1~100 : '))
# print to check
print(name,guess)

# Check the answer

if guess == answer:
    print ("Correct!")
else:
    print(f"You are wrong! the answer is {answer}")

