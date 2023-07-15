import random
secret_number = "8016"
# secret_number = random.sample(range(1, 10), 4)
# secret_number = (''.join(map(str, secret_number)))
user_number = ""
cow = 0
bull = 0
tries = 0

print("*** Welcome to Bulls and Cows ***")
print("you will guess a 4 digit number with no repeats, every guessed number in the right position is a 'bull' and every guessed number in the wrong position is a 'cow'. Good luck!!!")


def evaluate(user_digit):
    if secret_number.find(user_digit) >= 0:
        if secret_number.find(user_digit) == user_number.find(user_digit):
            global bull
            bull += 1
        else:
            global cow
            cow += 1
    else:
        pass


while bull < 4:
    cow = 0
    bull = 0
    user_number = input("Give me your number: ")
    tries += 1
    evaluate(user_number[0])
    evaluate(user_number[1])
    evaluate(user_number[2])
    evaluate(user_number[3])
    print(f"{cow} Cows, {bull} Bulls")
else:
    print(f"You wonn and took {tries} tries")
