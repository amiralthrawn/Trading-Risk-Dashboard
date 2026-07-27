returns = [2, -1, 3, -2, 1]

def calculate_average_return(returns):

    total = 0

    for value in returns:
        total += value

    return total / len(returns)

result = calculate_average_return(returns)

print(f"{result:.2f}%")