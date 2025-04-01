import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity, price):
        if quantity <= 0 or price <= 0:
            print("Error: Quantity and price must be positive numbers.")
            return

        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
            self.portfolio[symbol]['price'] = float(price)
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'price': float(price)}
        print(f"Stock {symbol} added successfully.")

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Stock {symbol} removed successfully.")
        else:
            print("Error: Stock not found in portfolio.")

    def update_stock(self, symbol, quantity, price):
        if quantity <= 0 or price <= 0:
            print("Error: Quantity and price must be positive numbers.")
            return

        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] = quantity
            self.portfolio[symbol]['price'] = float(price)
            print(f"Stock {symbol} updated successfully.")
        else:
            print("Error: Stock not found in portfolio.")

    def get_portfolio_value(self):
        total_value = sum(data['quantity'] * data['price'] for data in self.portfolio.values())
        return total_value

    def display_portfolio(self):
        if not self.portfolio:
            print("\nYour stock portfolio is empty.")
            return

        print("\nStock Portfolio:")
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: {data['quantity']} shares at ${data['price']:.2f} each")
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    # Add stocks to portfolio
    portfolio.add_stock("AAPL", 10, 150.50)  # Adding AAPL stock
    portfolio.add_stock("TSLA", 5, 700.75)   # Adding TSLA stock
    
    # Display portfolio
    portfolio.display_portfolio()
    
    # Update AAPL stock
    portfolio.update_stock("AAPL", 15, 155.25)
    
    # Remove TSLA stock
    portfolio.remove_stock("TSLA")
    
    # Display portfolio after updates
    portfolio.display_portfolio()
