weight = float(input("Enter the weight: "))
weight_output = input("Enter weight output in Kilos(K) or in Pounds(P): ").upper()

if weight_output == "K":
    result = float(weight / 2.205)
    print (round(result))
elif weight_output == "P":
    result = float(weight * 2.205)
    print (round(result))
else:
    print("You have not provided the correct option enter either K or P")

