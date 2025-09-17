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
i = random.randint(1, 100)
n = 1

guess = 50
while True:
    if guess == i:
        print('Congratulations, you guessed correct after {n} guesses!')
        break
    else:
        if guess < i:
            guess += guess // 2
            n += 1
        elif guess > i:
            guess -= guess // 2
            n += 1
# GÖR KLART DEN OVANFÖR^

# 4. Multiplication game


# 5. Check convergence

