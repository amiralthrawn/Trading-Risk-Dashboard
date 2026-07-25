portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}

best_asset = max(portfolio, key=portfolio.get)

print(best_asset)