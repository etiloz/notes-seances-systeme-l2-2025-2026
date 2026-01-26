# visionner aussi : https://www.youtube.com/watch?v=V_NXT2-QIlE
def premier_elt(L):
    """Renvoie le premier élément de la liste L.
    
    Lève une exception ValueError si la liste est vide.
    """
    if not L:
        raise ValueError("La liste est vide, aucun élément à renvoyer.")
    return L[0]

# Exemple d'utilisation
try:
    print(premier_elt([]))
except ValueError as e:
    print(f"Erreur rencontrée : {e}")