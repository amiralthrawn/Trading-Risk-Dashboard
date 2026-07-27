# 📊 Création d'un résumé d'analyse d'un actif

## 🎯 Pourquoi apprendre ça ?

En analyse financière, on ne regarde jamais un seul indicateur.

Un analyste veut généralement obtenir une vue globale d'un actif ou d'une stratégie.

Par exemple :

- Quel est le rendement moyen ?
- Quelle est la volatilité ?
- Quelle a été la meilleure performance ?
- Quelle a été la pire performance ?

L'objectif est de regrouper plusieurs indicateurs afin d'obtenir une analyse complète.

---

Dans un futur Trading Risk Dashboard, cette logique permettra d'afficher un résumé automatique :

```
📈 Rendement moyen : +0.60%

📉 Volatilité : 2.07%

🏆 Meilleure performance : +3%

⚠️ Pire performance : -2%
```

---

# Données utilisées

```python
returns = [2, -1, 3, -2, 1]
```

Ces valeurs représentent des rendements journaliers en pourcentage, (en cohérence avec les précédents exercises).

---

# Objectif

Créer une fonction :

```python
def asset_summary(returns):
```

qui retourne un dictionnaire contenant plusieurs indicateurs.

Résultat attendu :

```python
{
    "average_return": 0.6,
    "volatility": 2.07,
    "best_return": 3,
    "worst_return": -2
}
```

---

# Réutilisation des fonctions précédentes

Cet exercice permet de comprendre une notion importante en programmation :

# Code final (correspond à l'exercise 25)

```python
import statistics

returns = [2, -1, 3, -2, 1]


def calculate_average_return(returns):

    total = 0

    for value in returns:
        total += value

    return total / len(returns)


def asset_summary(returns):

    summary = {
        "average_return": calculate_average_return(returns),
        "volatility": round(statistics.stdev(returns), 2),
        "best_return": max(returns),
        "worst_return": min(returns)
    }

    return summary


result = asset_summary(returns)

print(result)
```

Résultat :

```text
{
'average_return': 0.6,
'volatility': 2.07,
'best_return': 3,
'worst_return': -2
}
```

---

# Ce que j'ai appris

- Créer une fonction qui utilise d'autres fonctions.
- Regrouper plusieurs résultats dans un dictionnaire.
- Comprendre qu'un programme complexe est souvent une combinaison de petites briques.
- Utiliser `round()` pour contrôler l'affichage d'une valeur.
- Structurer une analyse financière complète.

---

# 🚀 Application au Trading Risk Dashboard

Cet exercice représente la première version simplifiée d'un module d'analyse.

Dans un vrai dashboard, cette fonction pourra évoluer pour produire automatiquement :

```
Nom de l'actif

Prix actuel

Rendement

Volatilité

Drawdown maximal

VaR

Ratio risque/rendement
```

L'objectif final sera de transformer des données brutes de marché en informations utiles pour la prise de décision.