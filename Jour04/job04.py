"""Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
“pomme”, “cerise”, “orange, Melon”. Cette fonction doit à son appel ajouter à la liste
“fruits” une String “Mangue” à l’index 2."""

def list():
    fruits = ["pomme", "cerise", "orange","Melon"]
    fruits.insert(4,"mangue")
    print(fruits)
list()
