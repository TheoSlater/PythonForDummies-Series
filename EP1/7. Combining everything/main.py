# Simple program combining everything
name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello, " + name + "!")

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

print("Counting down from your age:")
for i in range(age, 0, -1):
    print(i)

print("Done!")
