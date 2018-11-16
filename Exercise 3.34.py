print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignment #1")
print("Exercise 3.34\n\n")

def pay(x,y):
    if y>40:
        z=y-40
        s=x*40
        p=z*(x*1.5)
        print("Pay :",s+p)
    else: 
        print("Pay :",x*y)
    

wage = int(input("Please enter the hourly wage            :"))
hour = int(input("Please enter the number of hours worked :"))

pay(wage,hour)
