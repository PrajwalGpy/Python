
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


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

w2_add_day = int(input("add an list value : "))
sales_w1.extend(sales_w2)
sales = sales_w1[:]
print(sales)
print(f"The best day {max(sales)}")
print(f"The worst day {min(sales)}")
print(f"The total day {sum(sales)}")