# 1. Counting letters
word = input('Enter a word: ')

# a)
print(len(word))

# b)
uppercase = 0
lowercase = 0

for char in word:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print(f'Uppercase letters: {uppercase}')
print(f'Lowercase letters: {lowercase}')

# 2. Counting words
sentence = """'A picture says more than a thousand words,
a mathematical formula says more than a thousand pictures.'"""
print(sentence)

words = sentence.split()
word_count = len(words)
print(f'There are {word_count} words in the sentence.')

# 3. Palindrome
word = input('Enter a word: ')

if word == word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')

# 4. Vowels
sentence = 'Pure mathematics is, in its way, the poetry of logical ideas.'

vowels = 'aeiou'
count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1

print(f'The sentence contains {count} vowels.')
