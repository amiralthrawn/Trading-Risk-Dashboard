# 📉 Calcul du drawdown maximal

## 🎯 Pourquoi apprendre ça ?

En trading, une stratégie ne se juge pas uniquement sur sa performance finale.

Deux stratégies peuvent avoir le même rendement, mais un niveau de risque très différent.

Exemple :

### Stratégie A

```
10 000 €
↓
9 000 €
↓
12 000 €
```

### Stratégie B

```
10 000 €
↓
11 000 €
↓
12 000 €
```

Les deux terminent à 12 000 €, mais la première stratégie a subi une perte temporaire beaucoup plus importante.

Le drawdown mesure justement cette baisse depuis le dernier sommet atteint.

---

Dans un futur Trading Risk Dashboard, cet indicateur permettra d'afficher :

```
📈 Performance totale : +20%

📉 Drawdown maximal : -15%

⚠️ Niveau de risque élevé
```

Un investisseur utilise le drawdown pour évaluer la difficulté psychologique et financière de supporter une stratégie.

---

# Données utilisées

```python
prices = [100, 110, 105, 90, 120]
```

Ces valeurs représentent l'évolution d'un prix dans le temps.

Visualisation :

```
100 → 110 → 105 → 90 → 120
```

---

# Objectif

Créer une fonction :

```python
def calculate_max_drawdown(prices):
```

qui retourne le drawdown maximal.

Résultat attendu :

```
-18.18%
```

---

# Comprendre la logique

Le drawdown dépend de l'ordre des données.

On ne peut pas simplement utiliser :

```python
max(prices)
```

car le sommet utilisé pour calculer une perte doit avoir existé **avant** la baisse.

Le programme doit donc parcourir les prix dans l'ordre.

---

# Principe de l'algorithme

On garde deux informations en mémoire :

## 1) Le plus haut prix observé

Au départ :

```python
maximum = prices[0]
```

Le programme considère le premier prix comme le sommet actuel.

Ensuite, à chaque nouveau prix :

- si le prix est supérieur au sommet actuel → nouveau sommet ;
- sinon → on calcule la baisse depuis ce sommet.

---

## 2) Le pire drawdown trouvé

On conserve également :

```python
drawdown_max = 0
```

À chaque baisse :

1. Calculer le drawdown actuel.
2. Comparer avec le pire drawdown déjà trouvé.
3. Mettre à jour si la perte est plus importante.

---

# Formule du drawdown

```
(prix actuel - sommet précédent) / sommet précédent × 100
```

Exemple :

Sommet :

```
110
```

Prix actuel :

```
90
```

Calcul :

```
(90 - 110) / 110 × 100

= -18.18%
```

---

# Code final -> correspondant à l'exercise 24. 

```python
prices = [100, 110, 105, 90, 120]


def calculate_max_drawdown(prices):

    drawdown_max = 0
    maximum = prices[0]

    for value in prices:

        if value > maximum:
            maximum = value

        else:
            drawdown = (value - maximum) / maximum * 100

            if drawdown < drawdown_max:
                drawdown_max = drawdown

    return drawdown_max


result = calculate_max_drawdown(prices)

print(f"{result:.2f}%")
```

Résultat :

```
-18.18%
```

---

# Ce que j'ai appris

- Parcourir des données financières dans l'ordre chronologique.
- Garder une valeur de référence pendant une boucle.
- Comprendre la différence entre un nouveau sommet et une baisse.
- Utiliser une logique de comparaison pour conserver le pire scénario.
- Créer un indicateur de risque utilisé en finance.

---

# 🚀 Application au Trading Risk Dashboard

Le drawdown sera utilisé pour évaluer le risque réel d'une stratégie.

Exemple :

```
Stratégie A

Rendement : +30%
Drawdown : -5%


Stratégie B

Rendement : +30%
Drawdown : -35%
```

Même performance finale, mais risque très différent.

Le drawdown permettra donc de compléter les autres indicateurs :

- Rendement moyen
- Volatilité
- Range
- Drawdown
- Value at Risk (VaR)

afin d'obtenir une vision complète de la performance et du risque.