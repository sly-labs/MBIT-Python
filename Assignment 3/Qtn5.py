# Sample list of Celsius temperatures
celsius_temperatures = [0, 20, 25, 30, -5, 37, -10]

# Convert Celsius to Fahrenheit using lambda and map
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print the results
print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)

# Print each conversion pair for clarity
print("\nDetailed conversions:")
for c, f in zip(celsius_temperatures, fahrenheit_temperatures):
    print(f"{c}°C = {f:.1f}°F")