print("Welcome to the distance converter!")

try:
    kilometers = float(input("Enter the distance in kilometers: "))
except Exception:
    print("Invalid input. Please enter a number for kilometers.")
    exit()

print("You entered " + str(kilometers) + " kilometers")

conversion_rate = 1.60934

miles = kilometers * conversion_rate

conversion_rate = 1.60934

miles = kilometers * conversion_rate

print(str(kilometers) + " kilometers are equal to " + str(miles) + " miles")