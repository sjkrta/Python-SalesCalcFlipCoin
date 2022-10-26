DASH = "-" * 60

print(DASH)
print("Hello, Welcome to the program")
print(DASH)
n_customers = int(input("Enter the number of customers: "))
print(DASH)

data = ["Name", "Quantity", "Reseller", "Charge"]

spendingMost = 0
spendingLeast = 4000
spendingMostCustomer = None
spendingLessCustomer = None

names = []
quantities = []
resellers = []
charges = []

for i in range(n_customers):
    name = input("\nEnter customer name: ")
    names.append(name)
    while True:
        quantity = int(input("Enter the number of coffee beans bags (bag/1kg): "))
        if 1 < quantity <= 100:
            break
        if quantity < 1:
            print("Enter at least 1 quantity.")
            continue
        print("Thats beyond the range. You can select up to 100 only.")
    quantities.append(quantity)

    price = 0
    totalPrice = 0

    if quantity <= 3:
        price = 38 * quantity
    elif quantity <= 10:
        price = 35.5 * quantity
    else:
        price = 33.7 * quantity

    while True:
        reseller = input("Enter yes/no to indicate whether you are a reseller: ")
        if reseller not in ("yes", "no"):
            print("Sorry! That is a wrong input.")
            continue
        totalPrice = price - price * 0.1 if reseller == "yes" else price
        break

    if totalPrice > spendingMost:
        spendingMost = totalPrice
        spendingMostCustomer = name

    if totalPrice < spendingLeast:
        spendingLeast = totalPrice
        spendingLessCustomer = name

    resellers.append(reseller)
    charges.append(f"${totalPrice:0.2f}")

    print(f"The total sales from {name} is {totalPrice}")
    print(DASH)

print(f"\n{'Summary of the sales'.center(60)}\n{DASH}\n{DASH}")
for name, quantity, reseller, charge in zip(names, quantities, resellers, charges):
    print(f"{name:<15}{quantity:^15}{reseller:^15}{charge:^15}")
print(DASH, "\n")
print(
    f"The customer spending most is {spendingMostCustomer} with an amount of ${spendingMost:0.2f}"
)
print(
    f"The customer spending least is {spendingLessCustomer} with an amount of ${spendingLeast: 0.2f}"
)
