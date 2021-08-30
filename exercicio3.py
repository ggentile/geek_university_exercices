speed = input("Please, select the speed method you wanna convert to: ".lower())
number = float(input("Insert the speed: "))

if speed == "km/h":
    kilometers_hour = (number * 3.6)
    print(f"The car speed in Km/h is: {kilometers_hour}")

elif speed == "miles":
    miles = number/1.61
    print(f"The speed in miles is: {miles}")

elif speed == "quilometers":
    quilometers = 1.61 * number
    print(f"The speed in quilometers is: {quilometers}")

else:
    meters_second = (number / 3.6)
    print(f"The car speed in m/s is: {meters_second}")
