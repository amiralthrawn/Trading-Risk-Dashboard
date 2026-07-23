asset = "Nasdaq"
entry_price = 22000
exit_price = 22500

gain = exit_price - entry_price
performance = (gain / entry_price) * 100

print("Actif :", asset)
print("Gain :", gain, "points")
print(f"Performance : {performance:.2f}%") 