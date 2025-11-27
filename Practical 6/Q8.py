#Question 8

import random

state_capital = {
    "Johor": "Johor Bahru", "Kedah": "Alor Setar", "Kelantan": "Kota Bharu",
    "Malacca": "Malacca City", "Negeri Sembilan": "Seremban",
    "Pahang": "Kuantan", "Penang": "George Town", "Perak": "Ipoh",
    "Perlis": "Kangar", "Sabah": "Kota Kinabalu", "Sarawak": "Kuching",
    "Selangor": "Shah Alam", "Terengganu": "Kuala Terengganu",
    "Kuala Lumpur": "Kuala Lumpur", "Labuan": "Victoria", "Putrajaya": "Putrajaya"
}

count = 0
keys = list(state_capital.keys())
random.shuffle(keys)

print("Identify the capital of following states:")
for i in range(len(keys)):
    string = "\nEnter the capital of {:16}: ".format(keys[i])    
    if input(string).lower() == state_capital[keys[i]].lower():
        print("Correct")
        count += 1
    else:
        print("Wrong")

print("\nYou answered {:d} {:s} correctly!".format(count, "questions" if count > 1 else "question"))