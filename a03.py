import copy
items = ['milk', 'apples', 'flour', 'bananas',
         'chicken', 'beef', 'orange juice'
        ]
stock = [20, 325, 44, 61, 8, 13, 15]
price = [3.50, 0.40, 4.00, 1.29, 2.99, 3.49, 3.99]
discounted = []
low_stock = []

def add_items():
    items.append(str(input("Item name to add\n")))
    stock.append(int(input("How many of that item being added? (whole number)\n")))
    price.append(float(input("Price of item (X.XX)\n")))

def main(items, stock, price, discounted, low_stock):
    longest_name = items[0]
    for i in items:
        if len(i) > len(longest_name):
            longest_name = i
    c = 0
    while c < len(items):
        if (stock[c] <= 10):
            if items[c] not in low_stock:
                price[c] = round(price[c]*1.25, 2)
                low_stock.append(items[c])
        elif (stock[c] >= 200):
            if items[c] not in discounted:
                price[c] = round(price[c]*0.75, 2)
                discounted.append(items[c])
        c += 1
    print("----------------------------------------")
    print("Items currently on 25% discount: ")
    for i in discounted:
        print(f'{i} (was ${"{:.2f}".format(round(price[items.index(i)]*1.3333, 2))})')
    print("----------------------------------------")
    print("Items currently with low stock: ")
    for i in low_stock:
        print(i)
    print("----------------------------------------")
    print("All items")
    x = 0
    formatted_names = copy.copy(items)
    while x < len(items):
        if len(formatted_names[x]) < len(longest_name):
            for num in range(len(longest_name)-len(formatted_names[x])):
                formatted_names[x] += '.'
        print(f'{formatted_names[x]}.....${"{:.2f}".format(price[x])}  QTY[{stock[x]}]')
        x += 1

flag = True
while (flag):
    main(items, stock, price, discounted, low_stock)
    add_items()
    if (input("\n\nWould you like to quit? Type y to quit or just enter to continue\n") == "y"):
        flag = False