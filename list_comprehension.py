friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
	print(f"{friend.title()} is one of your friends.")

"""ages = [age for age in range(1, 101)]
print(ages)
odds = [age for age in ages if age % 2 == 1]
print(odds)
even = [age for age in ages if age % 2 == 0]
print(even)"""

"""friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
	name.title() for name in guests if name.lower() in friends_lower
]

print(present_friends)"""