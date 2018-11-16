print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.24\n\n")


user_lst = []
for x in range(5):
    a = input("Please enter word "+str(x+1)+":")
    user_lst.append(a)

for x in range(5):
    if user_lst[x]!='secret':
        print(user_lst[x])

        
