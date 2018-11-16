print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.22")

user_lst=[]
for x in range(8):
    a=int(input("Pleasse enter number "+str(x+1)+":"))
    user_lst.append(a)

for a in range(8):
    y = user_lst[a]
    z = y**2
    if z%8==0:
        print(y)
