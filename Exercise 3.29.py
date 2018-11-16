print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.29\n\n")

user_num = int(input("Please enter a number:"))

for x in range(1,user_num+1):
    if user_num%x==0:
        print(x)
