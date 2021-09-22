# #lesson 89
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
# }
#
# print(programming_dictionary["Function"])
#
# #Adding a new item to dictionary
#
# programming_dictionary["Loopy"] = "Loopy loop"
#
# print(programming_dictionary)
#
#create an empty dictionary and wipiing them
# programming_dictionary = {}
#
#edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth on your computer"
#
#looping through dictionaries
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# #lesson 90
#
# student_scores = {
#      "Harry": 81,
#      "Ron": 78,
#      "Hermione": 99,
#      "Draco": 74,
#      "Neville": 62,
#  }
# # # 🚨 Don't change the code above 👆
# #
# # #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# #
# # #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectatations"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] > 60:
#         student_grades[student] = "Below average"
#     else:
#         student_grades[student] = "failed"
#
#
# # # 🚨 Don't change the code below 👇
# print(student_grades)

#lesson 91

# trave_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Paris", "Lille", "Stuttgart"]
#         "total_visits": 5
#     },
# ]

# #lesson 92
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

#lesson 93

#from replit import clear
#import os
#from art import logo

#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the bidding program!")
#os.system("clear")

bids = {}


bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is the {winner} with the bid of {highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is  your bid?: $"))
    bids[name] = price


    should_continue = input("Are there more bidders? Yes or No\n")
#    os.system("clear")

    if should_continue == "No":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        print("lol")
        #os.system("clear")





#print(bidders)
