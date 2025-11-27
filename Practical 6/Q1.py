while True:
    score = input("Enter a score or 'Q'/'q' to exit: ")
    
    if score =="Q" or score =="q":
        break
    try:
        score = float(score)
    except ValueError:
        print("Only number is allowed!")
    else:
        if not (score >= 0 and score <= 100):
            print("Only 1 ≤ number ≤ 100 inclusize are allowed!")
        else:
            if score >= 90 and score <= 100:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"
                
            match grade:
                case "A"| "F":
                    print("You got an", grade," for the test!\n")
                case "B"| "C" | "D":
                    print("You got a", grade," for the test!\n")
print("Thank you")