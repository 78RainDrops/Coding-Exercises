numerator = float(input("Enter numerator: "))
dominator = float(input("Enter dominator: "))

if dominator == 0:
    print("Error: Dominator cannot be zero")
else:
    percentage = (numerator / dominator) * 100
    print(f"The percent is: {percentage:.2f}%")
