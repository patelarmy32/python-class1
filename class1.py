# Prompt the user for their name
name = input("Please enter your name: ")

# Welcome the user
print(f"Welcome, {name}!")
# Prompt the user for hours worked
hours = float(input("Enter hours worked: "))

# Prompt the user for rate per hour
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate gross pay
gross_pay = hours * rate_per_hour

# Display the gross pay
print(f"Gross pay: ${gross_pay:.2f}")
width = 17
height = 12.0

#evaluting the expressions

a = width//2
print(a)

b = width/2.0
print(b)

c = height/3
print(c)

# Prompt the user for a Celsius temperature
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature with three significant digits
print(f"Temperature in Fahrenheit: {fahrenheit:.3f}")
