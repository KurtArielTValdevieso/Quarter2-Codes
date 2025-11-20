place = []
print("Please enter your FIVE destination trips.")
for x in range(1,6):
    y = str(input(f'\nDistance {x}: '))
    place.append(y)

print("This is your travel list:")
for i, p in enumerate(place, start=1):
    print(f"{i}. {p}")

print(f'\n\nThis time, we will change your 2nd and 5th options for no reason!')

dest2 = str(input("\nNew destination 2: "))
place.pop(1)
place.insert(1,dest2)

dest5 = str(input("\nNew destination 5: "))
place.pop(4)
place.insert(4,dest5)

print("\nThis is your NEW travel list:")
for i, p in enumerate(place, start=1):
    print(f"{i}. {p}")
