friend = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
user_name = input("Enter your name: ")

if user_name == "Anderson":
	print("Hello, Master!")
elif user_name in friend:
	print("Hello, friend!")
elif user_name in family:
	print("Hello, family!")
else:
	print("I don't know you!")