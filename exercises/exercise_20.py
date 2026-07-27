portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}

def calculate_portfolio_return(portfolio):
     
     total = 0

     for value in portfolio.values():
         total = total + value

     return total

 

result = calculate_portfolio_return(portfolio)

print(f"result : {result:.2f}")