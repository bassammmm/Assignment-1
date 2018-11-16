print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.42\n\n")

def avg(x):
    print("\n\n")
    for a in range(len(grade)):
        tot=0
        avg=0
        for b in range(len(grade[a])):
            tot+= grade[a][b]
        avg=tot/len(grade[a])
        print("The average grade of Student",a+1,":",avg)
        
grade=[]
st_num = int(input("How many students?:"))
grade=[[] for row in range(st_num)] 
for x in range(st_num):
    st_sub = int(input("How many subject of student"+str(x+1)+":"))
    for y in range(st_sub):
        m = int(input("Please enter marks of Student"+str(x+1)+" Subject"+str(y+1)+":"))
        grade[x].append(m)
avg(grade)
