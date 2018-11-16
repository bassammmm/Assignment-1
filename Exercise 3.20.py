print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.20")

user_str=[]
for x in range(5):
    a = input("Please enter word"+str(x+1)+":")
    user_str.append(a)

for x in range(5):
    print(user_str[x][:3])
