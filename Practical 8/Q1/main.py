from myinputreaders import *
from mystringinput import *

def main():
    text = read_string("Enter a string: ")
    
    print ("\nNo of Word: ", count_words(text))
    
    print("Averafe word length: {:.2f}\n".format(calculate_average_word_length(text)))
    
    for vowel, frequency in count_vowel_aeiou(text).items():
        print("No of {} :{:d}".format(vowel, frequency))
        
        main()