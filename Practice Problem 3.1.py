print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.1")

print("\n\nA) This program will let you know if you are eligible for pension benefits:-")
age = int(input("Please enter your age :"))
if age>62:
    print("You can get your pension benefits")

print("\n\nB) This program will take baseball player's name input and tell if he is the best or not:-")
lst = ['Musial','Aaraon','Williams','Gehrig','Ruth']
name = input("Please enter a baseball player name:")
name = name.title()
if name in lst:
    print("One of the top 5 baseball players, ever!")

print("\n\nC) This program will take input of hit and shield and tell if you will die or not:-")
hit = int(input("Please enter your hit level :"))
shield = int(input("Please enter your shield level :"))

if (hit>10) and (shield == 0):
    print("Sorry youre dead.")

print("\n\nD) This program will tell wether you can escape or not:-")
north = True
south = False
east  = False
west  = False

if (north or south or east or west)== True :
    print("You can escape")
              
