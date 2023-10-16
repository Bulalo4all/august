x = (25 * (9/5)) + 32
x = float(x)
# formula for Celsius to Farenheit = (Temp in Celsius * 9/5) + 32
print(f"25 Degrees in Celsius is {x:.1f} in farenheit")

# Step 2:
def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees in celsius is {farenheit:.1f} in farenheit")
celsius_to_farenheit(25)
