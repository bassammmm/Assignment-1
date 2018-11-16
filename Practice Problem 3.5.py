print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Assignent #1")
print("Practice Problem 3.5")

print("\n\nPractice Problem 3.5")

lst_words=[]
word = input("Please enter a word:")
lst_words.append(word)
word = input("Please enter a word:")
lst_words.append(word)
word = input("Please enter a word:")
lst_words.append(word)
word = input("Please enter a word:")
lst_words.append(word)

print("\nThe four letter words are:")
for x in lst_words:
    if len(x) == 4:
        print(x)
        
