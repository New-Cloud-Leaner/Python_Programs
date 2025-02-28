unit = input("Enter the Unit in celcius(C) or fahrenheit (F): ").upper()
temperature = float(input("Enter the termperature: "))
if unit == "F":
    result = ((temperature* 9)/5) + 32
    print(f"The output is {round(result,5)} F")
elif unit == "C":
    result = ((temperature-32)*(5/9))
    print(f"The output is {round(result,5)} C")
else:
    print("Enter C or F to convert temperature")
    exit()