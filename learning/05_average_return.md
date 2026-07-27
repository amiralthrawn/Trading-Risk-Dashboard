# 📊 Calcul du rendement moyen d'un actif

## 🎯 Pourquoi apprendre ça ?

Un analyste financier ne regarde pas uniquement :

- la meilleure performance ;
- la pire perte ;
- la volatilité.

Il cherche aussi à répondre à une question essentielle :

> Quel est le rendement moyen d'un actif sur une période donnée ?

Exemple :

```
Jour 1 : +2%
Jour 2 : -1%
Jour 3 : +3%
Jour 4 : -2%
Jour 5 : +1%
```

Le rendement moyen permet d'obtenir une vision globale de la performance.


Exemple :

```
📈 Rendement moyen : +0.60%

📉 Volatilité : 2.07%
```

---

# Données utilisées

```python
returns = [2, -1, 3, -2, 1]
```

Ces valeurs représentent des rendements journaliers en pourcentage.

---

# Objectif

Créer une fonction :

```python
def calculate_average_return(returns):
```

qui retourne le rendement moyen.

Résultat attendu :

```
0.60%
```

---

# Première approche

La première idée à laquelle j'ai pensé consiste à diviser chaque rendemnt parle nombre de valeurs. 

Exemple :

```python
total += value / 5
```

Cette méthode fonctionne avec monexemple car la liste contient exactement 5 rendements.

Cependant, elle n'est pas adaptable.

Si demain la liste devient :

```python
returns = [2, -1, 3]
```

le calcul serait faux.

---

# Amélioration du code

Une solution plus robuste consiste à :

1. Additionner tous les rendements.
2. Compter automatiquement le nombre de valeurs avec `len()`.
3. Diviser le total par le nombre d'observations.


# Code final -> correspondant à l'exercise 23

```python
returns = [2, -1, 3, -2, 1]


def calculate_average_return(returns):

    total = 0

    for value in returns:
        total += value

    return total / len(returns)


result = calculate_average_return(returns)

print(f"{result:.2f}%")
```

Résultat :

```
0.60%
```

---

# Ce que j'ai appris

- Utiliser une boucle pour accumuler des valeurs.
- Comprendre l'intérêt de `len()`.
- Créer une fonction qui s'adapte à différentes tailles de données.
- Améliorer un code pour le rendre plus robuste.

---

# 🚀 Application au Trading Risk Dashboard

Le rendement moyen sera utilisé pour comparer différents actifs ou stratégies.

Exemple :

```
Nasdaq :
Rendement moyen : +0.4%

Bitcoin :
Rendement moyen : +0.8%
```

Cependant, un rendement moyen seul ne suffit pas.

Il devra être analysé avec d'autres indicateurs comme :

- la volatilité ;
- le drawdown ;
- la Value at Risk.

C'est la combinaison de plusieurs indicateurs qui permet d'évaluer correctement une stratégie financière.