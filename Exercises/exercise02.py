# 1. Count numbers
i = -10
while i <= 10:
    print(i, end=' ')
    i += 1

# 2. Arithmetic sum

# a)
i = 1
n = 1
while i < 100:
    n += i + 1
    i += 1
print(n)

# b)
i = 1
n = 1
while i < 99:
    n += i + 2
    i += 2
print(n)

# 3. Guess number game
import random
import numpy as np
i = random.randint(1, 100)
n = 1

guess = 50
d = guess // 2
while True:
    if guess == i:
        print('Congratulations, you guessed correct after {n} guesses!')
        break
    else:
        if guess < i:
            guess += d
            d = np.ceil(d / 2)
            n += 1
        elif guess > i:
            guess -= d
            d = np.ceil(d / 2)
            n += 1

# 4. Multiplication game
import random
import time

def get_difficulty():
    print('Choose difficulty level:')
    print('1. Easy (1-10)')
    print('2. Medium (1-20)')
    print('3. Hard (1-50)')
    choice = input('Enter 1, 2 or 3: ')

    if choice == '1':
        return 10
    elif choice == '2':
        return 20
    elif choice == '3':
        return 50
    else:
        print('Invalid choice, defaulting to Easy.')
        return 10
    
max_number = get_difficulty()

score = 0
high_score = 0
streak = 0
time_limit = 10

print('Welcome to the Multiplication Game!')
print('Type q anytime to quit.')

while True:
    x = random.randint(1, max_number)
    y = random.randint(1, max_number)

    start_time = time.time()
    answer = input(f"What is {x} x {y}? ")
    elapsed_time = time.time() - start_time

    if answer.lower() == 'q':
        print(f"You quit! Your final score is: {score}")
        break
    
    elif elapsed_time > time_limit:
        print(f"Time's up! You took too long. Your final score is: {score}")
        break
    
    elif answer.isdigit() and int(answer) == x * y:
        streak += 1
        bonus = streak // 5
        score += 1 + bonus
    if score > high_score:
        high_score = score
        print(f"Good work! Current score: {score} | High score: {high_score} | Streak: {streak}")
    if bonus > 0:
        print(f"Streak bonus! +{bonus} points")

    else:
        print(f"Incorrect! The correct answer was {x * y}.")
        print(f"Your final score is: {score}")
        break

