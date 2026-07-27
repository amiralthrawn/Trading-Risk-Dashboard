# 🏆 Sélection du meilleur actif d'un portefeuille

## 🎯 Pourquoi apprendre ça ?

Un analyste financier ne veut pas seulement connaître la performance globale d'un portefeuille.

Il veut aussi répondre à des questions comme :

- Quel actif a le mieux performé ?
- Quel actif a le moins bien performé ?
- Quel actif contribue le plus au rendement ?

Dans un futur Trading Risk Dashboard, ces informations permettront d'afficher des indicateurs comme :

🏆 Meilleur actif : Nasdaq (+10%)

📉 Pire actif : Bitcoin (-20%)

---

# Données utilisées

```python
portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}
```
## Objectif

Créer une fonction :

```python
def best_asset(portfolio):
```

qui retourne :

```
Nasdaq
```

car le Nasdaq possède le meilleur rendement.

---

## Raisonnement algorithmique

Une première solution consiste à parcourir chaque actif :

1. Comparer son rendement avec le meilleur rendement connu.
2. Garder en mémoire le meilleur résultat.
3. Mettre à jour le nom de l'actif lorsqu'un meilleur rendement est trouvé.

Cette méthode permet de comprendre le fonctionnement interne d'une recherche du maximum.

---

## Code Python -> correspondant à l'exercise 21

```python
portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}


def best_asset(portfolio):

    best_return = -999
    best_name = ""

    for asset, value in portfolio.items():

        if value > best_return:
            best_return = value
            best_name = asset

    return best_name


result = best_asset(portfolio)

print(result)
```

Résultat :

```
Nasdaq
```

---

# Limite de cette approche

Même si cet algorithme fonctionne,j'ai remarqué et constater que l'utilisation d'une valeur de départ arbitraire comme :

```python
best_return = -999
```

n'est pas idéale.

Pourquoi ?

Parce que le programme dépend d'une valeur inventée par le développeur (moi même).

Si les données changent ou si les rendements sont dans une autre échelle, cette valeur peut devenir incohérente.

---

# Amélioration de la logique

Un développeur préférera souvent une approche où le programme ne dépend pas d'une valeur choisie artificiellement.

L'idée devient :

> Au lieu de commencer avec une valeur inventée, on commence avec une donnée réelle du portefeuille.

Le programme prend le premier actif comme référence :

```
Meilleur actif actuel = premier actif
Meilleur rendement actuel = rendement du premier actif
```

Puis il compare les actifs suivants.

Cette méthode est plus robuste car elle s'adapte directement aux données fournies.

---

# Version améliorée avec Python -> correspondant à l'exercise 21 bis

Python possède également des fonctions intégrées permettant d'effectuer cette recherche plus simplement.

Avec `max()` :

```python
portfolio = {
    "Nasdaq": 0.10,
    "Brent": 0.05,
    "Bitcoin": -0.20
}

best_asset = max(portfolio, key=portfolio.get)

print(best_asset)
```

Résultat :

```
Nasdaq
```

---

# Ce que j'ai appris

- Parcourir un dictionnaire avec `.items()`
- Comparer des valeurs dans une boucle
- Maintenir une meilleure valeur trouvée
- Comprendre la logique derrière une fonction comme `max()`
- Utiliser une méthode plus simple et plus adaptée en Python

---

# 🚀 Application au Trading Risk Dashboard

Cette logique sera utilisée pour identifier :

- Le meilleur actif d'un portefeuille
- Le pire actif
- Les meilleures performances journalières
- Les plus grandes variations de marché

Ces indicateurs permettront de construire une analyse financière plus complète.