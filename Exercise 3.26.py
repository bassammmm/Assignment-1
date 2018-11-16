print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.26\n\n")

user_lst = []
for x in range(5):
    a = input("Please enter element "+str(x+1)+":")
    user_lst.append(a)

print("\n\nThe first element is :",user_lst[0])
print("The last element is :",user_lst[-1])
