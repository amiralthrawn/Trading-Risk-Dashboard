# 📈 Comprendre l'amplitude de rendements (range)

## 🎯 Pourquoi apprendre ça ?

En trading, le rendement ne suffit pas.

Prenons deux actifs :

### Actif A

```text
+1%
+1%
+1%
+1%
```

### Actif B

```text
+5%
-4%
+6%
-5%
```

Les deux peuvent afficher une performance moyenne similaire.

Pourtant, l'actif **B** est beaucoup plus risqué car ses variations sont beaucoup plus importantes.

Dans le futur **Trading Risk Dashboard**, cet indicateur sera affiché aux côtés du rendement, du drawdown et d'autres mesures de risque.

---

## 💻 Première implémentation en Python (correspond à l'exercice 19)

```python
returns = [2, -1, 3, -2, 1]

def calculate_range(returns):
    return max(returns) - min(returns)

result = calculate_range(returns)

print(result)
```

---

## 🧠 Ce que j'ai appris

À travers cet exercice, j'ai appris à :

- créer une fonction avec `def`
- transmettre une liste à une fonction
- utiliser les fonctions intégrées `max()` et `min()`
- retourner un résultat avec `return`

Cette approche constitue une première étape avant de calculer une véritable volatilité statistique avec Pandas.

---

## 🚀 Suite du projet

Dans les prochains exercices, cette logique sera progressivement remplacée par des calculs financiers plus réalistes à partir de données de marché réelles.