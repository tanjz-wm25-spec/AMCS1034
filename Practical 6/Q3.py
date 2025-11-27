numbers = []

while True:
    number = input("Enter a integer or 'Q'/'q' to exit: ")
    
    if number == "Q" or number == "q":
        break
    
    try:
        numbers.append(int(number))
    except ValueError:
        print("Only integer is allowed!\n")
        
if len(numbers):
    numbers = numbers[::1]
    
    print("\nIntegers in revered order: ", end=" ")
    for num in numbers:
        print(num, end=" ")
else:
    print("No Integers.")