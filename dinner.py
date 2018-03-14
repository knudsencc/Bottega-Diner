import time

def user_name_input():
	return input("Welcome to Bottega Dinner! I am Cameron, I will be your Waiter today. what is your name?")

def my_name_method(name):
	print(f"hi {name}")

my_name_method(user_name_input())

def user_drink_input():
	return input("Can I Start you off with something to drink?")

def my_drink_method(Drink_order):
	print(f"Ok I will bring that {Drink_order} right out")

my_drink_method(user_drink_input())

print("While I grab your drinks look over our menu")

time.sleep(2)

print("Todays special is the Cheeseburger with your choice of fries or onion rings for only $10.00 ")

time.sleep(3)

Menu = [ 'Cheeseburger  $10.00','Chicken tenders  $9.00','Soup n Salad  $12.00','Pasta Dinner  $16.00','Pizza  $14.00']

print(Menu[0])
print(Menu[1])
print(Menu[2])
print(Menu[3])
print(Menu[4])

time.sleep(5)

def user_food_input():
	return input("May I recomend the Cheeseburger, its my personal favorite. Order when you are ready...")

def my_food_method(Food_order):
	print(f"Great Choice!!! I will get your order of {Food_order} to the chef right away!")
	
my_food_method(user_food_input())

time.sleep(5)

def user_opinion_input():
	return input("How was everything tonight? (good or bad)")

def my_opinion_method(Food_opinion):
  
  if Food_opinion == "good":
	  print('I am very happy to hear that!')
	  
  if Food_opinion == "bad":
	  print('I am so sorry to hear that!')  
	  
my_opinion_method(user_opinion_input())


def user_comment_input():
	return input("Is there anything you would like me to relay back to the kitchen? (yes or no)")
	
def my_comment_method(Food_comment):
  
	if Food_comment == "yes":
	  print('I will pass that message on right away!')
	  
my_comment_method(user_comment_input())

print('Thank You for coming in tonight. Here is your check!')

time.sleep(2)

print('Enter the total amount for your food:')

your_food_total = int(input(''))

operation = ('+')

print('Enter your tip amount:')

your_tip_amount = int(input(''))

print('Your total today Is:')

if operation == '+':

  print (your_food_total + your_tip_amount)

print("Thank you Come Again!")

time.sleep(3)

print("Remember we also serve breakfast and dinner!")

time.sleep(5)


breakfast_Menu = [ 'Breakfast Menu','Omlet  $12.00','Chicken and waffles  $14.00','pancakes  $10.00','french toast  $10.00','waffles  $11.00']

print(breakfast_Menu[0])
print(breakfast_Menu[1])
print(breakfast_Menu[2])
print(breakfast_Menu[3])
print(breakfast_Menu[4])
print(breakfast_Menu[5])

time.sleep(5)

Dinner_Menu = [ 'Dinner Menu','Cheeseburger  $15.00','Chicken tenders  $13.00','Soup n Salad  $16.00','Pasta Dinner  $21.00','Pizza  $20.00']

print(Dinner_Menu[0])
print(Dinner_Menu[1])
print(Dinner_Menu[2])
print(Dinner_Menu[3])
print(Dinner_Menu[4])
print(Dinner_Menu[5])

