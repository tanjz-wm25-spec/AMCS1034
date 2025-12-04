import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Update sys.path: ",sys.path)


from mypalindrome import *
from Q1.myinputreaders import *

def main():
    text = input("Enter a string").strip()
    print("{} {} a palinfrome!" .format(text, "is"if is_palindrome(text)else "is not"))
    
    main()