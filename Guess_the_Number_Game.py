import random
print("Guess the secret number between 1 - 9, you have 3 tries ;)")

attempts = 1
Answer = random.randrange(1, 10)
rest = 3

while attempts <= 3:
    attempts += 1
    n1 = int(input(f"Still have {rest} tries, write a number: "))
    rest -= 1
    if n1 != Answer:
        print("No")
    elif n1 == Answer:
        print("You won!!!")
        break
else:
    print(f"You lose the number was {Answer}")
