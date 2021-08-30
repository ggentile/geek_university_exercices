fahrenheit = float(input("Insert the temperature of the location you are in: "))
celsius_conversion_fahrenheit = 5 * (fahrenheit - 32)/9
celsius = float(input("Insert the temperature of the location you are in (ºC): "))
kelvin_conversion = celsius + 273.15
celsius_conversion_kelvin = float(input("Insert the temperature in Kelvin(K): "))
celsius_kelvin = celsius_conversion_kelvin - 273.15

print(f"The temperature in celsius is º{celsius_conversion_fahrenheit}C")

print(f"The temperature in kelvin is {kelvin_conversion}")

print(f"The temperature from kelvin to Celsius (ºC) is: {celsius_kelvin}")




