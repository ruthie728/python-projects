amount = 0
coins = [25, 10 ,5]
while amount < 50:
    coin  = int(input("Insert Coin "))
    if coin in coins:
        amount += coin
    else:
        print(f"Amount due: {amount}")

    if amount < 50:
        print(f"Amount due: {50 - amount}")
    else:
        print(f"Change Owed: {amount - 50}")



