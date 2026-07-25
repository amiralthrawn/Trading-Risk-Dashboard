# 📊 Comprendre le rendement d'un portefeuille

## 🎯 Pourquoi apprendre ça ?

En finance, on n'analyse pas toujours un seul actif.

La plupart des investisseurs possèdent un portefeuille composé de plusieurs actifs.

Par exemple :

| Actif | Rendement |
|-------|-----------|
| Nasdaq | +10 % |
| Brent | +5 % |
| Bitcoin | -20 % |

Pour connaître la performance globale, il faut additionner les contributions de chaque actif (dans cet exercice, sans pondération).

Cette logique est la première étape vers le calcul de la performance d'un portefeuille réel.

---

## 💻 Première implémentation en Python (correspond à l'exercise 20)

```python
portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}

def calculate_portfolio_return(portfolio):
    total = 0

    for value in portfolio.values():
        total += value

    return total

result = calculate_portfolio_return(portfolio)

print(result)
```

---

## 🧠 Ce que j'ai appris

- créer un dictionnaire Python
- parcourir les valeurs d'un dictionnaire avec `.values()`
- utiliser une boucle `for`
- créer une fonction réutilisable

---

## 🚀 Suite du projet

Dans le Trading Risk Dashboard, cette logique sera étendue pour calculer le rendement d'un portefeuille composé de plusieurs actifs avec des poids différents et des données de marché réelles.