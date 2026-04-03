#Convert Celsius to Fahrenheit.
try:
    celsius = float(input("Enter the temperature in Celsisus: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.1f} celsius is equal to {fahrenheit:.1f} fahrenheit.")
except ValueError:
    print(TypeError("Invalid input. Please enter the temperature as a numeric value."))