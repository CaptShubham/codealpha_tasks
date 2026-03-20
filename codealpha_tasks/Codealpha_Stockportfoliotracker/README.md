stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")

for i in range(3):  # user enters 3 stocks
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value
        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")
    else:
        print(f"{stock}: Price not available")

print("Total Investment Value: $", total_value)

save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            if stock in stock_prices:
                value = stock_prices[stock] * quantity
                file.write(f"{stock}: {quantity} shares = ${value}\n")
        file.write(f"Total Investment Value: ${total_value}\n")

    print("Portfolio saved to portfolio.txt")
