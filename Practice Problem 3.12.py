print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.12")

def negatives(x):
    for a in x:
        if a<0:
            print(a)
print("\n\n")
user_lst=[]
for x in range(6):
    a=int(input("Pleasse enter number "+str(x+1)+":"))
    user_lst.append(a)

negatives(user_lst)
