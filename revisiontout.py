import unittest


def maximum_normale(tab:list[int]) -> int :

    max=tab[0]
    for i in range (1, len(tab)): 
        # ca on peut aussi ecrire comme ca pour etre un peu plus logique 
        # for i in tab [1 :]
        if tab[i]>max: 
         max = tab[i]
    return max    

def max_avc_valeurs(tab : list[int])  -> int :
    maxv=tab[0]
    for valeur in tab[1:] : 
       if valeur > maxv :
        maxv= valeur
       
    return maxv     


def max_drp(tab:list[int]) -> int : 
    n=len(tab)
    if n== 1 :
        return tab[0]
   
    milieu = n//2
    max1 = max_drp(tab[: milieu])
    max2 = max_drp(tab[milieu : ])

    return max(max1 , max2) 

 
def sous_tableu(tab : list[int]) -> int :
    n=len(tab)
    if n== 1 :
        return tab[0]
    milieu = n//2
    somme =0

    somme_gauche, tableau_gauche = sous_tableu(tab[:milieu])
    somme_droite, tableau_droite = sous_tableu(tab[milieu:])
    m_somme=float("-inf")
    for i in range(milieu-1, -1 , -1 ) :
        somme += tab[i]
 # Si on trouve une somme meilleure que l'ancienne
        if somme > m_somme : 
            m_somme = somme
            meilleur_gauche=tab[i:milieu] 
        
    somme1=0
    m_somme1=float("-inf")
    for j in range(milieu , n ) : 
       somme1+= tab[j]
       if somme1 > m_somme1 : 
         m_somme1 = somme1
       meilleur_droit = tab[milieu : j+1]
        
    somme_croisee = m_somme + m_somme1

    meilleur_croise = meilleur_gauche + meilleur_droit

    if somme_gauche >= somme_droite and somme_gauche >= somme_croisee:
        return somme_gauche, tableau_gauche

    elif somme_droite >= somme_croisee:
        return somme_droite, tableau_droite

    else:
        return somme_croisee, meilleur_croise



Bit=Literal[0,1] ### ca  veut dire soit 0 soit 1 
binaire= list[Bit]

def bin_to_dec(bin : binaire) -> int : 
    puissance = 1 
    for i in range(len(bin), -1 , -1) :
        resultat= bin[i]*p 
        p*=2
    return resultat  

def dec_to_bin(nombre : int ) -> binaire : 
   resultat  = []

   while nombre > 0 :

      rest= nombre %2
      resultat.insert(0, rest)
      nombre=nombre//2

def compléter(b: binaire, n: int) -> binaire:
    z: binaire = [0]

    if len(b) < n:
        b = z * (n - len(b)) + b # (n - len(b)) ca pour trouver combien de 0 que on rajoute 

    return b

def addition_binaire(b1 : binaire , b2 : binaire ) -> binaire :
   n=max(len(b1), len(b2))
   b1= compléter(b1, n)
   b2=compléter(b2,n)
   resultat = compléter([], n) #tableau de 0 
   retenue =0
   for i in range(n-1 , -1,-1):
      x= b1[i] + b2[i]+retenue
      resultat[i] = x % 2  # 1
      retenue = x // 2     # 1
      
