number = input("Enter a positve integer: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is divisible by 10.")
else:
    print(f"\nThe number {number} is not divisible by 10.")