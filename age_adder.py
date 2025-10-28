age = int(input("Hi there! Please enter your age: "))
while age <= 0:
    print()
    age = int(input("Enter your age (Must be a whole number): "))

counter = 0
for x in range (1, age + 1):
    counter += x
        
print(f'The sum of all numbers from 1 to {age} is: {counter}')
