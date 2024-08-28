print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

operater = input("Enter the Opreter ex:(+,-,*,/) : ")
num1 = int(input("Enetr the first number"))
if not(operater) == "f":
    num2 = int(input("enter the Second number"))

temp = int(input("enter the Temptecher"))
if operater == "+":
    print(num1+num2)

elif operater == "-" :
    print(num1-num2)

elif operater == "*" :
    print(num1*num2)

elif operater == "/" :
    if num1 == 0:
        print("infinite")
    else:
        print(num1/num2)

elif operater.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
    
else:
    print("Invalid Choiec Choivce Bwetwen (+,-,*,/) them")

tempF = temp*9/5+32
print(f"the temprecger to faernhite is {tempF}")
