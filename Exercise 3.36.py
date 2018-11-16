print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.36\n\n")

def reverse_int(x):
    for y in range(3):
        y = int(x%10)
        print(y,end=" ")
        x = x/10
    

user_num = int(input("Please enter a 3-digit number only:"))
reverse_int(user_num)
