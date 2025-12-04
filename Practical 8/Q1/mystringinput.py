def read_integer(prompt = "Enter an Integer: ", error = "Error: Wrong Input!\n", minimum= -(10**10), maximum = 10**10):
    """
    purpose:
    read integer from user input

    parameter:
    prompt:prompt message, default "Enter an Integer: "
    error: error message, default "Error: Wrong Input!
    minimum = int, lower bond of user input, default to -(10**10)
    maximum = int, upper bond of user input, default to (10**10)
    
    return:
        int: The integer entered by user

    """

    while True:
        number = input(prompt)
        try:
            number = int(number)
            if number >= minimum and number <= maximum:
                return number
            else:
                print(error)
        except ValueError:
            print("Error: Only Integer are Allowed\n")

def read_float(prompt = "Enter a number: ", error = "Error: Wrong Input!\n", minimum= float("-inf"), maximum = float("inf")):
    """
    purpose:
    read number from user input, default is positive value

    parameter:
    prompt:prompt message, default "Enter  number: "
    error: error message, default "Error: Wrong Input!
    minimum = float, lower bond of user input, default to float("-inf")
    maximum = float, upper bond of user input, default to float("inf")
    
    return:
        int: The floating-point number entered by user

    """

    while True:
        
        try:
            number = float(input(prompt))

            if number >= minimum and number <= maximum:
                return number
            else:
                print(error)
        except ValueError:
            print("Error: Only Floating-point Number is Allowed\n")

def read_integers(prompt = "Enter an Integer: ", error = "Error: Wrong Input!\n", minimum= -(10**10), maximum = 10**10, stop = "q", loop = 10**10):
    """
    purpose:
    read integer from user input

    parameter:
    prompt:prompt message, default "Enter an Integer: "
    error: error message, default "Error: Wrong Input!
    minimum = int, lower bond of user input, default to -(10**10)
    maximum = int, upper bond of user input, default to (10**10)
    stop = string, use for stopping condition indicate by user using one letter "q"
    loop = int ,iteration to be execute to read "loop " number of input value
    
    return:
        list: A series of the integer entered by user

    """

    integers = []
    count = 0
    stop = str(stop)


    while True:
        integer = input(prompt)
        if integer.lower() == stop.lower():
            return integers
        try:
            integer = int(integer)
            if integer >= minimum and integer <= maximum:
                integers.append(integer)
                count += 1
                if count == loop:
                    return integers

            else:
                print(error)
        except ValueError:
            print("Error: Only Integer are Allowed\n")


def read_floats(prompt = "Enter a number: ", error = "Error: Wrong Input!\n", minimum= float("-inf"), maximum = float("inf"), stop = "q", loop = 10**10):
    """
    purpose:
    read number from user input, default is positive value

    parameter:
    prompt:prompt message, default "Enter  number: "
    error: error message, default "Error: Wrong Input!
    minimum = float, lower bond of user input, default to float("-inf")
    maximum = float, upper bond of user input, default to float("inf")
    stop = string, use for stopping condition indicate by user using one letter "q"
    loop = int ,iteration to be execute to read "loop " number of input value

    
    return:
        list: A series of The floating-point number entered by user

    """
    floats = []
    count = 0


    while True:
        number = input(prompt)
        if number.lower() == stop.lower():
            return floats
        
        try:
            number = float(input(prompt))

            if number >= minimum and number <= maximum:
                floats.append(number)
                count +=1
                if count == loop:
                    return floats
            else:
                print(error)
        except ValueError:
            print("Error: Only Floating-point Number is Allowed\n")

def read_string(prompt = "Enter a string: "):
    return input(prompt).strip()