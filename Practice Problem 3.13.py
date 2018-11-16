print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.13")

def average(x,y):
    'Returns average of x and y'
    avg = (x+y)/2
    return avg

user_num_1 = float(input("\n\nPlease enter the first number :"))
user_num_2 = float(input("Please enter the second number:"))

print("The average of these 2 numbers is :",average(user_num_1,user_num_2))


def negatives(x):
    'returns all the negative integers in x'
    for a in x:
        if a<0:
            print(a)
print("\n\n")
user_lst=[]
for x in range(6):
    a=int(input("Pleasse enter number "+str(x+1)+":"))
    user_lst.append(a)

negatives(user_lst)
