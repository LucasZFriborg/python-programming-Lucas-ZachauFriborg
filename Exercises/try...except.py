# Övning 1 – Division
# Be användaren skriva två tal.
# Försök dela det första talet med det andra.
# Om användaren skriver bokstäver istället för siffror → skriv ut ett felmeddelande.
# Om användaren försöker dela med noll → skriv ut ett annat felmeddelande.
try:
    n1 = float(input('Enter a number: '))
    n2 = float(input('Enter another number: '))
    result = n1 / n2
    print(f'Result: {result}')
except ValueError:
    print('Error: Please enter numbers only.')
except ZeroDivisionError:
    print('Error: Numbers cannot be divided by zero.')

# Övning 2 – Heltal
# Be användaren skriva ett heltal.
# Om det är ett giltigt heltal → skriv ut talet.
# Om användaren skriver något annat (t.ex. text) → skriv ut ett felmeddelande.
try:
    number = int(input('Enter an integer: '))
    print(f'Number: {number}')
except ValueError:
    print('Error: Please enter a number only.')

# Övning 3 – Lista
# Skapa en lista med tre olika frukter.
# Be användaren skriva en siffra mellan 0 och 2.
# Om siffran är giltig → skriv ut frukten på den platsen.
# Om användaren skriver något som inte är en siffra → skriv ut felmeddelande.
# Om användaren skriver ett tal som inte finns i listan → skriv ut felmeddelande.
fruits = ['Mango', 'Papaya', 'Banana']

try:
    num = int(input('Enter a number between 0 and 2: '))
    print(f'You chose {fruits[num]}.')
except ValueError:
    print('Error: Please enter an integer only.')
except IndexError:
    print('Error: Please enter a number between 0 and 2.')
