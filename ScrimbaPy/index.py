
# Printing an variable
# print('hiii')

# variable assignment
# failed_subjects="2"
# name='John'
# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name + '  will need to redo ' + failed_subjects + '  courses.')
# print(name + '  is doing well in geography.')


# DataType & typeCasting

# int
# age = 21
# # str
# name = 'prajwal'
# # float 
# present = 87.9
# # bool 
# is_Alive = True

# print(age)




# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))

# typeCasting

# a = int(1)        # a will be 1
# b = int(2.5)      # b will be 2
# c = int("3")      # c will be 3
# c1 = int(float("3.4"))   # c1 will be...
# d = float(1)      # d will be 1.0
# e = float(2.5)    # e will be 2.5
# f = float("3")    # f will be 3.0
# g = float("4.23") # g will be 4.23
# h = str("80s")    # h will be '80s'
# i = str(22)       # i will be '22'
# j = str(3.01)     # j will be '3.01'

# print([a,b,c,c1,d,e,f,g,h,i,j])

# print('Variables & Datatypes - Exercise')
# #Create appropriate Variables for Item name, the price 
# #and how many you have in stock
# banana = 30
# bury = 60
# print("banana "+ str(banana) +" price 2Rpce per 1 ")
# print("banana "+ str(bury) +" price 5Rpce per 1 ")


# slicing the word
# msg = "I am leaning python"

# # print(msg  + msg )
# # print(msg , msg )
# # print(msg * 3 )
# # print(len(msg))
# # print(msg.count("Leaning"))
# # print(msg.upper())
# # print(msg.lower())
# # print(msg.capitalize())
# # print(msg.title())
# print(msg)
# print(msg[3:-3])

# msg='welcome to Python 101: Strings'
  
# print(msg[-10],msg[:7],msg[25:29],msg[8:10],msg[13:15])


#multi line writing
# msg = """ goooo
#   toooo 
#   home
# """
# print(msg)
# output :-
#  goooo
#   toooo 
#   home



# msg = 'Welcome to Python 101: Strings'

# # print(msg)
# # msg= msg.replace("Python","JavaScript")
# # print(msg)
# print("Python" not in msg)


# pormating
# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 =f'[{name}] loves the color {color.capitalize()} !'
# print(msg)
# print(msg1)


#input Box
# name= input('What is your name?: ')
# age=input('What is your age?: ')
# print('Hello '+ name + '! You are '+ age + ' years old.')

# num1 = int(input("Enter an number : "))
# num2 = int(input("enter the second number : "))
# goo = num1+num2
# print(type(goo))
# print("answer is : ",goo)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# name = input("Enter your name : ")
# disKil = float(input("enter the kilometers"))
# print(f"hiii {name} your kilometers {disKil} to miles is {round(1*disKil/1.609,4)}")

# lists
# friends = ['John','Michael','Terry','Eric','Graham']

# print(friends[1],friends[4])
# print(len(friends))
# print(friends.index('Eric'))

# home = ["gooo","hooooo","rooooo","fooooo"]
# print(home.count("gooo"))

# friends = ['John','Michael','Terry','Eric','Graham']
# fooo = ["2","4","6","7","3","4"]

# friends.append("gopal")
# friends.insert(3,"gopal34")
# friends[1]="gp"
# friends.pop()
# friends.pop(1)
# friends.remove("John")
# friends.sort()
# friends.sort(reverse=True)
# friends.reverse()
# # del friends
# friends.extend(fooo)

# # freind1= list(friends)
# freind1= friends[:]
# print(friends)
# print(freind1)


# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []

# w2_add_day = int(input("add an list value : "))
# sales_w1.extend(sales_w2)
# sales = sales_w1[:]
# print(sales)
# print(f"The best day {max(sales)}")
# print(f"The worst day {min(sales)}")
# print(f"The total day {sum(sales)}")

# msg ='Welcome  to  Python  101: Split  and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(''.join(friends_list))

# print(msg.split("c"))


# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ",".join(",".join(csv.split(";")).split(":")).split(",")
# print(friends_list)
# print(((csv.replace(":",",")).replace(";",",")).split(","))
# # From the list above fill a list(friends_list) properly
# # with the names of all the friends. One per "slot"
# # you may need to run same command several times
# # use print() statements to work your way through the exercise

# # friends_list.extend(csv)
# # print(friends_list)

# goo = ["jjjj","hhhhhh","llllllll","hhhhhhh","sgsgsgs","llllllll"]
# goo1 = ("jjjj","hhhhhh","llllllll","hhhhhhh","sgsgsgs","llllllll")
# goo2 = {"jjjj","hhhhhh","llllllll","hhhhhhh","sgsgsgs","llllllll"}
# gp = {"jjjj","hhhhhh","llllllll","hhhhhhh","sgsgsgs","llllllll","77535"}
# print(goo)
# print(goo1)
# print(goo2)

# print(goo2.union(gp))


#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# print('Eric' and 'John' in friends)
# print(friends.union(my_friends))
# print(friends.intersection(my_friends))
# print(friends.difference(my_friends))
# clone= set(cars[:])
# print(clone)

#Function



# def Greeting(name,age=22):
#     print(f"hiii {name}, you are {age} old!")
    

# name= input("enter your name : ")
# age = input("enter your age : ")

# Greeting(name,age)
# Greeting("gggggg")

# def greeting(name, age=28,color="red"):
#     #Greets user with 'name' from 'input box' and 'age', if available, default age is used
#     print('Hello '  +  name + ', you will be ' + str(age+1) +'years old next birthday')
#     print(f'Hello {name.capitalize()}, you are {age}!')
#     print(f'We hear you like the color {color.lower()}! xxx is a string with color')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# color = input('Enter your color: ')
# greeting(name, 32,color)
# # 1. Add new print statement - on a new line
# #    which says 'We hear you like the color xxx! xxx is a string with color 
# # 2. extend the function with another  input parameter 'color', that defaults to 'red'
# # 3. Capture the color via an input box as variable:color 
# # 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
# #  adding 1 to the age
# # 5. Capitalize first letter of the 'name', and rest are small caps 
# # 6. Favorite color should be in lowercase 


# if/Else/elif

# def num_days(month):

#     if month in ['jan','mar','may','jul','aug','oct','dec']:
#         print('number of days in',month,'is',31)
#     elif month in ['apr','jun','sep','nov']:
#         print('number of days in',month,'is',30)
#     else :
#         print('number of days in',month,'is',28)    
        
# num_days('feb')
# # optimize/shorten the code in the function
# # try to reduce the number of conditionals 

# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")


# loops
# i=0
# while i<=5 :
#     print(f"{i}.{i*"*"}Loops are great{i*"*"}")
#     i=i+1

# print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

# theVlaue = 45
# i=1
# while i<=3:
#     useVlaue = int(input(f"Enter the  number {i}. chance : "))
#     if useVlaue == theVlaue :
#         print("You are Right")
#         break
    
#     elif useVlaue>theVlaue:
#         print("your value is too high")
#     elif  useVlaue<theVlaue:
#         print("your value is too low")

#     if i==3 and   useVlaue != theVlaue :
#         print("you lose  all chances")    
#     print(f"{3-i} chance remaning")
#     i+=1    

#loops 

# fri = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
# for friends in fri:
#     if friends == "mar":
#         continue
#     print(friends, fri.index(friends))

# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']

# for name in range(2):
#     names1e = input("Enter the name : ")
#     names1.append(names1e)

# print(names1)
# names.extend(names1)

# for invitation in names:
#   
#   print(f"{invitation.title()}! you are invited to the party on saturday.")



# Disctionery

# profile = {
#     "name" : "Prajwal",
#     "age" : 20 ,
#     "city" : "kundapura"
# }
# print(profile.items())
# print(profile.values())
# print(profile.keys())

# for key,value in profile.items() :
#     print(key,value)

#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
# freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
# antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
# pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

# names = []

# # Add the stores to the list
# for store in (freelancers, antiques, pet_shop):
#     names.append(store)

# # Create an empty shopping cart
# cart = {}

# # Loop through stores/dictionaries
# for shop in names:
#     while True:  # Loop to allow multiple purchases from each shop
#         # Show items available in the shop
#         available_items = {key: value for key, value in shop.items() if key != 'name'}
#         buy_item = input(f"Welcome to {shop.get('name')}! What do you want to buy: \n{available_items}\nType 'done' to finish shopping here.\n: ").lower()

#         if buy_item == 'done':
#             break  # Exit the loop to go to the next shop

#         # Check if the item exists in the shop
#         if buy_item in available_items:
#             # Add the item and its price to the cart
#             cart[buy_item] = available_items[buy_item]
#             print(f"{buy_item.capitalize()} added to your cart.")
#         else:
#             print(f"Sorry, {buy_item} is not available in {shop.get('name')}.")

# # Display the final cart
# print(f"\nYou purchased {cart}. Today it is all free. Have a nice day of mayhem!")


# File reading
# with open("C:/Users/prajw/OneDrive/Desktop/PyThon/ScrimbaPy/goo.txt","r") as f:
#     print(f.readline())
#     print(f.readlines())
#     print(f.readlines())

# Try/Except, Raise
# try:
#     number = int(input("Enter a number: "))
#     print(10 / number)
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# try:
#     num = input("Enter the number")
    
#     if num == "a":
#         raise ValueError("Inavlid name")
#     print(num) 
# except ValueError as e:
#     print(e)          
     
# class Profile:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 

# p1=Profile("gopal",23)
# print(p1.age,p1.name)



# inheritence
# class Docter:
#     def heal(self):
#         print("i heal")
#     def figth(self):
#         print("i can fight")

# class ninja:
#     def fast(self):
#         print("i can move fast")

# class nimbele(Docter,ninja):
#     def goo(self):
#         print("i can move solvely")


# p1=nimbele()

# p1.fast()

# lambda


# gooo = lambda x : x*2

# print(gooo(3))

# print('Lambdas Exercise')

# def f(x): return x + 5
# #f = ...#insert equivalent lambda here
# print(f(2))

# multi = lambda x: x+5

# # print(multi(2))

# print('Lambdas Exercise')

 
# def strip_spaces(str):
#    return ''.join(str.split(' '))
# #write equivalent lambda and insert Lambda here
# # strip_spaces1 =lambda x : x.replace(" ","")
# strip_spaces1 =lambda x : "".join(x.split() ) 
# print(strip_spaces('Monty Pythons Flying Circus')) 
# print(strip_spaces1('Monty Pythons Flying Circus')) 

# print('Lambdas Exercise')
 
# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
# list_a = [1,2,3,4]
# list_b = [3,4,5,6,7]
# #write lambda below 
# join_list_no_duplicates1 = lambda list_a,list_b : list(set(list_a+list_b))
# print(join_list_no_duplicates(list_a,list_b))
# print(join_list_no_duplicates1(list_a,list_b))

# print('Lambdas Exercise')

# #Complete the function so it returns a function
# def create_quad_func(a,b,c):
#     '''return function f(x) = ax^2 + bx + c'''
#     return lambda x: a*x**2 + b*x + c
# f = create_quad_func(2,4,6)
# g = create_quad_func(2,4,6)
# print(f(2))
# print(g(2))

# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# print(sorted(signups)) # Lexicographic sort
# #write sorting by integer
# print(sorted(signups,key=lambda x:int(x[3:])) )# Integer sort


# comprohention

# numbers = [1,2,3,4,5,6,7,8,9]

# # ne_list = [(num,x) for num in "Prajwal" for x in range(4)]
# # print(ne_list)
# new_list= [num for num in numbers if num % 2 == 1]
# print(new_list)

# Randomness

import random as rand

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(rand.choice(friends_list))
