# 1. Check sign
number = float(input('Enter a number: '))

if number > 0:
    print('The number is positive')
elif number < 0:
    print('The number is negative')
else:
    print('The number is zero')

# 2. Smallest
number1 = float(input('Enter a number: '))
number2 = float(input('Enter another number: '))

if number1 < number2:
    print(f'{number1} is smaller')
else:
    print(f'{number2} is smaller')

# 3. Right angle
angle1 = float(input('Enter the first angle in degrees: '))
angle2 = float(input('Enter the second angle in degrees: '))
angle3 = float(input('Enter the third angle in degrees: '))

if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print('All angles must be greater than 0 degrees. Try again.')
elif angle1 + angle2 + angle3 != 180:
    print('The angles do not form a triangle. Sum must be 180 degrees. Try again.')
else:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print('The triangle has a right angle!')
    else:
        print('The triangle does not have a right angle.')

# 4. Medicine
age = int(input('Enter an age: '))
weight = float(input('Enter a weight in kg: '))

if age > 12 and weight > 40:
    pills = '1-2'
elif age >= 7 and age <= 12 and weight >= 26 and weight <= 40:
    pills = '1/2-1'
elif age >= 3 and age <= 7 and weight >= 15 and weight <= 25:
    pills = '1/2'

print(f'Recommendation: {pills} pills')

# 5. Divisible
number = float(input('Enter a number: '))

if number % 2 == 0:
    print('Number is even.')
else:
    print('Number is odd.')

if number % 5 == 0:
    print('Number is divisible by 5.')
else:
    print('Number is not divisble by 5.')

if number % 5 == 0 and number % 2 != 0:
    print('Number is divisible by 5 and is odd.')

# 6. Luggage size
max_weight = 8
max_length = 55
max_width = 40
max_height = 23

weight = float(input('Enter the weight (kg): '))
length = float(input('Enter the length (cm): '))
width = float(input('Enter the width (cm): '))
height = float(input('Enter the height (cm): '))

if weight > max_weight:
    print('Your luggage is too heavy. Maximum weight is 8 kg.')
elif length > max_length:
    print('Your luggage is too long. Maximum length is 55 cm.')
elif width > max_width:
    print('Your luggage is too wide. Maximum width is 40 cm')
elif height > max_height:
    print('Your luggage is too tall. Maximum height is 23 cm.')
else:
    print('Your luggage is allowed. Welcome aboard!')