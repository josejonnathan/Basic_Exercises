print("write a word or phrase that can be a Palindrome: ")
User_Input = input("")


def is_palindrome(User_Input):
    flat_word = User_Input.lower().replace(" ", "")
    rev_input = flat_word[::-1]
    if flat_word == rev_input:
        print("Good!, it is a Palindrome")
    else:
        print("Sorry it is not a Palindrome")


is_palindrome(User_Input)
