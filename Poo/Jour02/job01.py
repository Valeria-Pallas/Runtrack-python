"""Créer une classe Personne qui aura comme attribut age prenant un entier et initialisé à
14 par défaut. Ajouter une méthode “afficherAge” qui affichera en console l’age de la
personne et une méthode bonjour qui écrit en console ‘Hello’. Créer une méthode
“modifierAge” prenant en paramètre un entier et permettant de modifier l’age de la
personne.
Créer une classe Eleve qui hérite de la classe “Personne” qui n’a pas d’attribut et une
méthode publique “allerEnCours” qui affiche : “Je vais en cours” ainsi qu’une méthode
“affichageAge” qui écrit en console : ‘J’ai XX ans’
Créer une classe Professeur avec un attribut privé “matiereEnseignée”, qui indiquera la
matière du professeur, et une méthode publique “enseigner” qui affiche :. ‘Le cours va
commencer’.
Instancier une classe “Personne” et une classe “Eleve”. Afficher l’age par défaut de
l’élève en console."""

class Personne():
    def __init__(self, age=14):
        self.age = age
        
    def affichageAge(self):
        print("j'ai",self.age, "ans")
        
    def bonjour(self):
        print("Hello")        
        
    def modifierAge(self, age):
        self.age = age
    
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en Cours")
    
    def affichAge(self, age):
        print("j'ai", age, "ans")
        
class Proffeseur():
    def __init__(self, matiereEnseigne):
        self.__matiereEnseigne = matiereEnseigne
        
    def enseigner(self):
        print("Le cours va commencer")   
        
personne = Personne()
eleve = Eleve()
print("l’age par défaut del’élève :", eleve.age)

    
    