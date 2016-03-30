import string
import sys

def remove_input_format(user_input):
    excluded_items = set(string.punctuation)
    return_string = "".join(char for char in user_input if char not in excluded_items and char != " ")
    return return_string.lower()

def is_palindrome(user_input):
    user_input = remove_input_format(user_input)
    if len(user_input) <= 1:
        return True
    if user_input[0] == user_input[-1]:
        return is_palindrome(user_input[1:-1])
    return False

def output_result(user_input):
    if is_palindrome(user_input):
        print("Palindrome!")
    else:
        print("NOT palindrome :(")

def main():
    print("\n")
    f = open(sys.argv[1])
    end_test = True
    while end_test == True:
        content = f.readline()
        if content == "":
            end_test = False
            break
        content = content.strip("\n")
        print(content, end = ": ")
        output_result(content)
    f.close()
    print("\n")

if __name__ == '__main__':
    main()
