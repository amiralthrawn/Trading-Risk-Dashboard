prices = [100, 110, 105, 90, 120]

def calculate_max_drawdown(prices): 

    drawdown_max = 0
    maximum = prices[0]

    for value in prices:

        if value > maximum:
            maximum = value 
       
        elif value <= maximum:
            drawdown = (value - maximum) / maximum * 100

            if drawdown < drawdown_max:
                drawdown_max = drawdown
        

    return drawdown_max

result = calculate_max_drawdown(prices)

print(f"{result:.2f}%")

