number = input("Enter any integer and I will tell you if it is divisible by 3: ")
number = int(number)

if number % 3 == 0:
    print(f"\nThe number {number} is divisible by 3.")
else:
    print(f"\nThe number {number} is not divisible by 3.")