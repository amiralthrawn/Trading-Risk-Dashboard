price_start = 22000
price_end = 22500

def calculate_return(price_start, price_end):
    return (price_end - price_start) / price_start * 100

result = calculate_return(22000, 22500)

print (f"result : {result:.2f}")
