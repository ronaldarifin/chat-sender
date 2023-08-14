import re
import pyperclip

def keep_numbers_and_plus(string):
    # Replace all non-numbers and non-"+" characters with an empty string
    string = re.sub(r'[^\d+]', '', string)
    return string

# Example usage:

while True:
   text = input()
   result = "Person("", " + keep_numbers_and_plus(text) +", [""]),"
   pyperclip.copy(result)
   print(result) # "1234+5678"