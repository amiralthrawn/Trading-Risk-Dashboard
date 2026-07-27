import statistics

returns = [2, -1, 3, -2, 1]

def calculate_average_return(returns):

    total = 0

    for value in returns:
        total += value

    return total / len(returns)

result = calculate_average_return(returns)

def asset_summary(returns):
     
     summary = {
         "average_return": calculate_average_return(returns),
         "volatility": round(statistics.stdev(returns), 2),
         "best_return": max(returns),
         "worst_return": min(returns)
     }

     return summary 

    
summary = asset_summary(returns)

print(summary)
