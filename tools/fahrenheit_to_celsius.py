# This is a simple python script to convert degrees in 
# fahrenheit to degrees in celsius

print("This is the fahrenheit to celsius converter!")

fahrenheit = input("\nEnter your degrees in fahrenheit: ")
fahrenheit = int(fahrenheit)

def fahreinheit_converter(fahrenheit):
    """Simple function to convert fahrenheit to celsius"""
    celsius = 5 * (fahrenheit - 32) / 9
    celsius = int(celsius)
    return celsius

celsius = fahreinheit_converter(fahrenheit)

print(f"\n{fahrenheit} degrees in fahrenheit is equal to {celsius} degrees in celsius.")