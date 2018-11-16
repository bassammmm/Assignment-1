print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.11")


def allEven(x):
    for a in x:
        if a%2!=0:
            print("Fasle")
            break
    else:
        print("True")

user_lst=[]
for x in range(6):
    a=int(input("Pleasse enter number "+str(x+1)+":"))
    user_lst.append(a)

allEven(user_lst)
