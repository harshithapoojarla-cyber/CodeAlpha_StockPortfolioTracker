stocks = {
    "TCS": 3500,
    "INFY": 1800,
    "RELIANCE": 2900,
    "HDFC": 1700
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        portfolio[stock_name] = quantity
        total_value += stocks[stock_name] * quantity
    else:
        print("Stock not found!")

print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    print(stock, ":", quantity, "shares")

print("Total Portfolio Value: ₹", total_value)