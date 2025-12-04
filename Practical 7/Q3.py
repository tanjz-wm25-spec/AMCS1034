def main():
    number = read_size()
    scores = read_scores(number)
    first, secound = get_top_two_scores(scores)
    
    print("\n The Highest Score         : {:.0f}%".format(first))
    print(" The Second Highest Score  : {:.2f}%".format(secound))
    print(" The Average Score         : {:.2f}%".format(calculate_average(scores)))


def read_size():
    while True:
        number = input("Enter the number of students: ")
        if number.isdigit():
            number = int(number)
            if number >= 1:
                return number
            else:
                print("Error: Only Positive Integer is Allowed!\n")
        else:
            print("Only Integer is Allowed!\n")


def read_scores(loop):
    floats = []
    count = 0
    
    while count < loop:
        number = input("Enter a score: ")
        try:
            number = float(number)
            if number >= 0:
                floats.append(number)
                count += 1
            else:
                print("Error: Only Positive Value or 0 is Allowed!\n")
        except ValueError:
            print("Error: Only Floating-point number is Allowed!\n")
    
    return floats


# Returns the highest and the second highest scores from a list of scores.
def get_top_two_scores(scores):
    scores.sort(reverse=True)
    return scores[0], scores[1]


# Returns the average of all scores contained in a list of scores.
def calculate_average(scores):
    return sum(scores) / len(scores)


# Returns the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if 11 <= number % 100 <= 13:
        return "th"

    last = number % 10
    if last == 1:
        return "st"
    elif last == 2:
        return "nd"
    elif last == 3:
        return "rd"
    else:
        return "th"


main()
