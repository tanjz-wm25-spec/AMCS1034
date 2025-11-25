message = input("Enter a string: ").strip()

words = message.split()

acyroom = ""

for word in words:
    acyroom += word[0].upper()
    
print("The acronym for '{}'is '{}'".format(message.strip(),acyroom))