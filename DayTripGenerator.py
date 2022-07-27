 # Day Trip Generator

 #(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own seperate lists.
 #(5 points): As a user, I want a destination to be randomly selected for my day trip.
 #(5 points): As a user, I want a restaurant to be randomly selected for my day trip.
 #(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
 #(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
 #(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
 #(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
 #(10 points): As a user, I want to display my completed trip in the console. 
 #(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
 
from tkinter import Y


print("Welcome to the Day Trip Generator! Let's plan your Oklahoma Lakes daytrip!")
destinations_list = ['Lake Tenkiller, Lake Eufala, Lake Murray, Grand Lake']
restaurant_list = ["Twisted Minnow",'Applebees', "Ed's Hideaway", 'Olive Garden', "Hide Away Grill", 'Texas Roadhouse', "Mooneys Sunset Bar and Grill"]
mode_of_transportation_list = ["Boat", "Rental Car", "Hot Air Balloon", "Motorcycle"]
form_of_entertainment_list = ["wave runners", "swimming", "cornhole tournament", "fishing"]

print(destinations_list)
destination = input("Which lake would you like to visit?") 
if destination == 'Lake Tenkiller':
    print('Awesome! You have chosen my favorite lake!')
elif destination == 'Lake Eufala':
    print('Great! Get ready for sandy beaches!')
elif destination == 'Lake Murray':
    print('You have chosen our most beautiful lake!')
elif destination == 'Grand Lake':
    print('Look for the rare paddlefish!')    
else:
    print('Not a valid Oklahoma Lake, please try again')
    destination2 = input('please choose one of the above listed lakes')


print('Next we will choose a restaurant.')

print(restaurant_list)

restaurant = input("Which restaurant lake would you like to dine at?") 
if restaurant == 'Twisted Minnow':
    print('Awesome! You have chosen the favorite restaurant at Lake Tenkiller!')
elif restaurant == 'Applebees':
    print('Fancy like! Applebees! On a date night!')
elif restaurant == 'Eds Hideaway':
    print('You have chosen the most popular food on the lake!')
elif restaurant == 'Olive Garden':
    print('Love me some shrimp alfredo and never ending salad and bread sticks!') 
elif restaurant == 'Hide Away Grill':
    print('The best of Lake Murray!')   
elif restaurant == 'Texas Roadhouse':
    print('Bloomin onion')
elif restaurant == 'Mooneys Sunset Bar and Grill':
    print('Grand Lake favorite!')
else:
    print('Not a valid food option, please try again')
    destination2 = input('please choose one of the above listed options')

print(restaurant)

print('Now lets choose your mode of transportation.')
print(f"Which  choice do you want?{mode_of_transportation_list}")

transportation = input(f"transportation_choice from {mode_of_transportation_list}")
print(transportation)

entertainment = input(f"Which entertainment would you like?{form_of_entertainment_list}") 
print(entertainment)



print('Great choice! Your day trip options are:')
print(destination)
print(restaurant)
print(transportation)
print(entertainment)




