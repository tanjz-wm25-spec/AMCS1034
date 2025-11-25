str1 = input("Enter a string: ").strip()
str2 = str1.lower()

for letter in str2:
    if not letter.isalpha():
        str2 = str2.replace(letter,"")
        
length = len(str2)
result = True
for i in range(len(str2)):
    if str2[i] != str2[length -1 -i]:
        result = False
        break
print("'{}'{} a palindrome!".format(str1,"is" if result else "is not"))