# 📉 Calcul de la volatilité d'un actif

## 🎯 Pourquoi apprendre ça ?

En finance, une bonne performance ne suffit pas.

Deux actifs peuvent avoir un rendement moyen similaire, mais un niveau de risque très différent.

Exemple :

### Actif A :

```
+1%
+1%
+1%
+1%
```

Les variations sont faibles et régulières.

### Actif B :

```
+5%
-4%
+6%
-5%
```

Les variations sont beaucoup plus importantes.

Même si la performance moyenne peut être proche, l'actif B est beaucoup plus risqué.

La volatilité permet justement de mesurer l'amplitude des variations autour de la moyenne.

---

# Données utilisées

```python
returns = [2, -1, 3, -2, 1]
```

Ces valeurs représentent des rendements journaliers en pourcentage :

```
+2%
-1%
+3%
-2%
+1%
```

---

# Objectif

Créer une fonction :

```python
def calculate_volatility(returns):
```

qui retourne la volatilité de cette série de rendements.

---

# Notion utilisée : l'écart-type

La volatilité financière est généralement mesurée avec l'écart-type (*standard deviation*).

L'écart-type mesure à quel point les valeurs s'éloignent de leur moyenne.

- Valeurs proches de la moyenne → volatilité faible
- Valeurs très éloignées → volatilité élevée

---

# Utilisation d'une bibliothèque Python

Python possède une bibliothèque appelée `statistics` qui contient déjà des fonctions statistiques.

On commence par l'importer :

```python
import statistics
```

Puis on utilise :

```python
statistics.stdev()
```

qui calcule l'écart-type d'une série de données.

---

# Code final -> correspondant à l'exercise 22 

```python
import statistics

returns = [2, -1, 3, -2, 1]

def calculate_volatility(returns): 
    return statistics.stdev(returns)

result = calculate_volatility(returns)

print(result)
```

Résultat :

```
2.0736...
```

---

# Ce que j'ai appris

- Importer une bibliothèque Python avec `import`
- Utiliser une fonction existante provenant d'un module
- Créer une fonction réutilisable
- Comprendre la différence entre une amplitude simple (`range`) et une vraie mesure statistique du risque (`volatilité`)

---

# 🚀 Application au Trading Risk Dashboard

La volatilité sera utilisée pour mesurer le niveau de risque d'un actif.

Exemple :

Un dashboard pourra comparer :

```
Nasdaq :
Volatilité = 1.2%

Bitcoin :
Volatilité = 4.5%
```

Cela permettra d'identifier les actifs les plus risqués et d'aider à la prise de décision.