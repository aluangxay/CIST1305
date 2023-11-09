# Shopping cart exercise

cart = []
prices = []
total = 0

while True:
    items = input("Enter new item you need to buy (q to quit): ")
    if items.lower() == "q":
        break 
    else:
        price = float(input(f"Enter the price of a {items}: $"))
        cart.append(items)
        prices.append(price)
print("----- YOUR CART -----")

for items in cart:
    #print (items,end=" ")
    print(items)

for price in prices:
    total += price

print()
print(f"This will be your total bill: ${total:.2f}")