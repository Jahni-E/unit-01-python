stock_symbol = input("Enter stock symbol: ")
current_price = float(input("Enter starting price: "))
target_price = float(input("Enter target price: "))
stop_loss = float(input("Enter stop-loss price: "))

price_updates = 0
alert_triggered = False

while current_price > target_price:
    current_price = float(input("Enter starting price: "))

if current_price <= target_price:
    print("Buy")
    current_price = float(input("Enter starting price: "))

if current_price >= stop_loss:
    print("Sell")
    current_price = float(input("Enter starting price: "))


if current_price == 0:
    print("ERROR")

