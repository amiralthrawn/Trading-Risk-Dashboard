performance = 6
reference_performance = 5
breakeven = 0

if performance >= reference_performance:
    print ("excellent trade")

elif performance >= breakeven:
    print ("trade gagnant")

else:
    print("trade perdant")
