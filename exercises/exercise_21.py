portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20  
}

def best_asset(portfolio):

    best_return = -999
    best_name = ""

    for asset, value in portfolio.items(): 

        if value > best_return:
            best_return = value 
            best_name = asset
            
     
    return best_name

result = best_asset(portfolio)

print(result)
