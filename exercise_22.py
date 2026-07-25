import statistics

returns = [2, -1, 3, -2, 1]

def calculate_volatility(returns): 
    return statistics.stdev(returns)

result = calculate_volatility(returns)

print(result) 