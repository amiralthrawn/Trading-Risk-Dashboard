trades = [100, -50, 200, 150, -80, 20]

compteur  = 0

for trade in trades:
     if trade > 0:
        compteur += 1

print("Nombre de trades gagnants:", compteur)

