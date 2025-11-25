message = input("Enter a string: ").strip()

words = message.split()

print("\n No. of words: ",len(words))

vowel = "aeiou"

message = message.lower()
print()
for character in vowel:
    print("No. of {}:{:d}".format(character, message.count(character)))
    
total = 0
for word in words:
    total += len(word)
print("\nAverage:{:.2f}".format(total/len(words)))