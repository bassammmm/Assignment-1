print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.40\n\n")

user_lst = []
for x in range(5):
    a = input("Please enter Soccer Player "+str(x+1)+" Name:")
    user_lst.append(a)

for x in range(5):
    if user_lst[x][:1]not in ('n','N','o','O','p','P','Q','q','r','R','s','S','t','T','u','U','v','V','x','X','y','Y','z','Z'):
        print(user_lst[x])
