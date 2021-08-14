dash = '-' * 60
print(dash)
print('Hello, Welcome to the program')
print(dash)
numberOfCustomers = int(input('Enter the number of customers: '))
print(dash)
data = [['Name', 'Quantity', 'Reseller', 'Charge']]

spendingMost=0
spendingLess=4000
spendingMostCustomer=''
spendingLessCustomer=''
for i in range(numberOfCustomers):
    customers=[]
    name = input("\nEnter customer name: ")
    customers.append(name)
    while True:
        number = int(input("Enter the number of coffee beans bags (bag/1kg): "))
        if number<1:
            print('Enter at least 1 quantity.')
        elif number<=100:
            break
        else:
            print('Thats beyond the range. You can select up to 100 only.')
    customers.append(number)

    price=0
    totalPrice=0
    if number <=3:
        price=38*number
    elif number >=4 and number<=10:
        price=35.5*number
    else:
        price=33.7*number

    while True:
        reseller=input('Enter yes/no to indicate whether you are a reseller: ')
        if reseller == 'yes':
            totalPrice= price-price*0.1
            break
        elif reseller == 'no':
            totalPrice=price
            break
        else:
            print('Sorry! That is a wrong input.')
    if totalPrice>spendingMost:
        spendingMost=totalPrice
        spendingMostCustomer=name
    if totalPrice<spendingLess:
        spendingLess=totalPrice
        spendingLessCustomer=name


    customers.append(reseller)
    customers.append('${:0.2f}'.format(totalPrice))
    data.append(customers)
    print("The total sales from", name, "is", totalPrice)
    print(dash)
print('\n'+'Summary of the sales'.center(60)+'\n'+dash+'\n'+dash)
for i in range(len(data)):
    print('{:<15}{:^15}{:^15}{:^15}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
print(dash,'\n')
print('The customer spending most is',spendingMostCustomer,'with an amount of','${:0.2f}'.format(spendingMost))
print('The customer spending least is',spendingLessCustomer,'with an amount of','${:0.2f}'.format(spendingLess))

