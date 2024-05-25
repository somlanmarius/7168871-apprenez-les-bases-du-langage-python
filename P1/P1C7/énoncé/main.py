# Écrivez votre code ici !
# Étape 1 : Créer le dictionnaire fruits
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Étape 2 : Ajouter la clé "kiwi" avec la valeur "vert"
fruits["kiwi"] = "vert"

# Étape 3 : Accéder à la valeur correspondant à la clé "banane" et la stocker dans une variable
couleur_banane = fruits["banane"]

# Étape 4 : Modifier la valeur associée à la clé "pomme"
fruits["pomme"] = "vert"

# Étape 5 : Supprimer la clé "banane" du dictionnaire
del fruits["banane"]

# Étape 6 : Afficher les clés restantes dans le dictionnaire
cles_restantes = list(fruits.keys())
print(cles_restantes)
['pomme', 'orange', 'kiwi']

