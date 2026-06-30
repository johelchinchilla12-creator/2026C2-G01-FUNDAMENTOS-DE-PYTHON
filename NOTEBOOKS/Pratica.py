print("Hello, World!")

name = input("Whats your name?    ")
print(f"Hello, {name}!")

number = float(input("Enter a number:   "))

number2 = float(input("Enter another number:   "))

sum_result: float = number + number2
print(f"The sum of the two numbers is {sum_result:.2f}")

sub_result: float = number - number2
print(f"The subtraction of the two numbers is {sub_result:.2f}")

mult_result: float = number * number2
print(f"The multiplication of the two numbers is {mult_result:.2f}")

div_result: float = number / number2
print(f"The division of the two numbers is {div_result:.2f}")


number = int(input("Enter a number to check if it is even or odd:"))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"That {number} is not an even number, please use an even number")

number = int(input("Enter a number to start the countdown:  "))
for i in range(number, 0, -1):
    print(i)
print("Blastoff")


number = int(input("Enter a number to create a multiplication table:  "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

import random

secret_number = random.randint(1, 20)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    guesses += 1
    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
    elif guess < secret_number:
        print("No! Your guess is too low.")
    elif guess > secret_number:
        print("No! Your guess is too high.")

    elif guess == secret_number:
        print(f"Yes! that's exactly right! You guessed it in {guesses} tries.")
        break


sentence = input("Enter a sentence:     ")

words = sentence.split()
sorted_words = sorted(words)
key = input("Enter a word to search for:     ")
if key in sorted_words:
    print(f"The word '{key}' is present in the sentence.")
else:
    print(f"The word '{key}' is not present in the sentence.")

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
