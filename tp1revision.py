import unittest

def recherche_maximum(tab: list[int]) -> int : 

    maximum = tab[0]
    for i in range(len(tab)):
        if tab[i] > maximum:
            maximum = tab[i]

    return maximum


def maximmum_drp(tab: list[int]) -> int : 

    if len(tab)==1:
     
        return tab[0]

    m = len(tab)//2
    max1 = maximmum_drp(tab[0:m])
    max2 =maximmum_drp(tab[m:])

    if max1 > max2 : 
        return max1
    else :
        return max2 

 # exo 1.1.3 la somme des entiers positifs dans un tableu donné 


def somme_des_elements(tab: list[int]) -> int :
    
    if not tab:
                raise ValueError("Le tableau ne doit pas être vide")
    if len(tab)==1:
            return tab[0]
    m=len(tab)//2

    sommme1=somme_des_elements(tab[0:m])
    somme2=somme_des_elements(tab[m:])
    return sommme1 + somme2
 
# exo 1.1.4


def sous_tableau_max(tab: list[int]):

    if not tab:
        raise ValueError("Le tableau ne doit pas être vide")

    if len(tab) == 1:
        return tab[0]

    m = len(tab) // 2

    #meillieure somme a gauche 
    somme = tab[m - 1]
    m_somme_gauche=tab[m-1]
    for i in range(m, -1,-2):
         somme+=tab[i]
    if somme > m_somme_gauche :
         return m_somme_gauche
    else : m_somme_gauche     
     
    #meillieure somme a droite 
    somme2 = tab[m]
    m_somme_droite = somme2

    for j in range(m + 1, len(tab)):
        somme2 += tab[j]

    if somme2 > m_somme_droite:
        m_somme_droite = somme2  

    m_somme_achevale= m_somme_droite + m_somme_gauche

    return m_somme_achevale    


 


