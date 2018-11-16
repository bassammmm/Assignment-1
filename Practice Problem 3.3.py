print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.3")


print("\n\nA) This program lets you know if the year is a leap year or not:-")
year = int(input("Please enter the year:"))

if (year%4 == 0):
    print("Could be a leap year")
else:
    print("Definitely not a leap year")


print("\n\nB) This program lets you know if your list of ticket number is the lottery number:-")

lst_ticket = []
ticket = int(input("Please enter the first number in ticket :"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the second number in ticket:"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the third number in ticket :"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the fourth number in ticket:"))
lst_ticket.append(ticket)

lst_lottery = [5,4,6,9]
print("Ticket :", lst_ticket)
print("Lottery:",lst_lottery)
if lst_ticket == lst_lottery:
    print("\nYOU WON!")
else:
    print("\nBetter luck next time!")






