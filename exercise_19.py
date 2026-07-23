returns = [2, -1, 3, -2, 1]

def calculate_range(returns): 
    return (max(returns) - min(returns))

result = calculate_range(returns)

print (result)