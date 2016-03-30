import string

def remove_input_format(user_input):
    excluded_items = set(string.punctuation)
    return_string = "".join(char for char in user_input if char not in excluded_items and char != " ")
    return return_string.lower()

def is_palindrome_recursive(user_input):
    user_input = remove_input_format(user_input)
    if len(user_input) <= 1:
        return True
    if user_input[0] == user_input[-1]:
        return is_palindrome(user_input[1:-1])
    return False

def output_result_recursive(user_input):
    if is_palindrome_recursive(user_input):
        print("You have a palindrome!")
    else:
        print("You do not have a palindrome :(")

def is_palindrome_iterative(user_input):
    user_input = remove_input_format(user_input)
    counter = 0
    test_value = True
    while counter < int(len(user_input)/2):
        if user_input[counter] != user_input[(counter * -1) - 1]:
            test_value = False
            break
        counter += 1
    return test_value

def output_result_iterative(user_input):
    if is_palindrome_iterative(user_input):
        print("You have a palindrome!")
    else:
        print("You do not have a palindrome :(")

def main():
    print("\n\nPlease enter some text.")
    output_result_recursive(input("> "))

main()
