# exo 1.1.3

import unittest


def maximum_classique(tab: list[int]) -> int:
    """
    Args:
        tab (list[int]): tableau d'entiers

    Returns:
        int: la valeur du maximum
    """
    if not tab:
        raise ValueError("Le tableau ne doit pas être vide")

    maximum = tab[0]
    for valeur in tab[1:]:
        if valeur > maximum:
            maximum = valeur
    return maximum


def max_dpr(tab: list[int]) -> int:
    """Maximum calculé par la méthode diviser pour régner.

    Args:
        tab (list[int]): tableau des entiers

    Returns:
        int: maximum
    """
    if not tab:
        raise ValueError("Le tableau ne doit pas être vide")
    if len(tab) == 1:
        return tab[0]

    m = len(tab) // 2
    max1 = max_dpr(tab[:m])
    max2 = max_dpr(tab[m:])
    return max1 if max1 > max2 else max2

# exo 1.1.2. Recherche du maximum

def rechechemax(tab: list[int]) -> int:

    """"
    recherche de maximuim dans un tableu.
  
    Args 
    tab(list[int]): tableu des entiers 
    """
    maximum=tab[0]
    for i in range(len(tab)) :
        if tab[i] > maximum :
            maximum = tab[i]
        
    return maximum               


# exo 1.1.2. Recherche du maximum 

def max_sous_tableu_naif(tab:list[int]) -> int:

    """"
         calcul le maximum des sommes des sous tableu de tab version en complexité O(n carré)

    
        Args:

        tab(list[int]): tableu des entiers 
    """

     

    