
stock_prices = {
    "AAPL": 180,   
    "TSLA": 250,   
    "MSFT": 330, 
    "GOOGL": 140,  
    "AMZN": 135    
}

portfolio = {}

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock symbol! Try again.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty


total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    total_value += value

print(f"\nTotal Investment Value = ${total_value}")


save_choice = input("Do you want to save portfolio to file? (yes/no): ").lower()
if save_choice == "yes":
    filename = "portfolio.csv"
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
        f.write(f"Total,,,{total_value}\n")
    print(f"Portfolio saved to {filename}")
