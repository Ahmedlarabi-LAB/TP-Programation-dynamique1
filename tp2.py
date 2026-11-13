###########
 ###TP MULTIPLICATION D'entiers####


from typing import Literal
import unittest 
Bit=Literal[0,1] ### ca  veut dire soit 0 soit 1 
binaire= list[Bit] ### logique 

#1) converstion binaire -> decimal(int)
def bin_to_dec(bin: binaire) -> int :
  
    p=1 # puissance de 2
    resultat=0
    for i in range(len(bin) -1 , -1 , -1 ) : # len(bin-1) c'est la fin du tableu , -1 c'est le debut et -1 c'est le parcours a l'anvers  
        resultat += bin[i]*p
        p=p*2 
    return resultat

class TestMultiplication(unittest.TestCase):
    def test_bi_to_dec(self):
        r=bin_to_dec([1, 1, 0, 1])
        self.assertEqual(r, 13)
        self.assertEqual(bin_to_dec([0]), 0)

    def test_dec_to_bin(self):
        r=dec_to_bin(13)
        self.assertEqual(r, [1, 1, 0, 1])

    def test_addition(self):
        for i in range(1000):
                for j in range (1000):
                    b=add_binaire(dec_to_bin(i), dec_to_bin(j))
                    self.assertEqual(b, dec_to_bin(i+j))

    def test_dpr_multi(self):
        r=mult_naive_dpr([1,0,0,1] , [1,0,1,0])
        self.assertEqual(r,[1,0,1,1,0,1,0])

    def soustraction(self):
            r=soustraction([1,0,0,1] , [1,0,1,0])
            self.assertEqual(r,[1,1,1,1])  

    de           

#2) conversion decimal -> bianire

def dec_to_bin(dec:int )-> binaire :

    if dec==0 :

        return[0]
    resultat=[]
    while dec>0 :
        resultat.insert(0, dec %2)# 0 c'est l'indice 0 et dec ca se rajoute a gauche a chaque fois 
        #
        #si par exemple on a 10>0 et donc on entre dans la boucle et 
        # dans l'indice 0 , on ajoute le dec%2 =0 et on refait 
        # donc la on est a 5 > 0 et et il est pas modulo 2 donc on ajoute 1 a gauche de 0  psk modulo 2 donne 1 ou 0 
        #
        dec= dec//2

    return resultat

#3) add binaire 
def add_binaire(b1: binaire, b2: binaire ) -> binaire : 
    # on commence a mettre un 0 au débur des biniaires 
    # pour eviter les déplacement 
    n=max(len(b1), len(b2))
    b1= compléter(b1,n)
    b2= compléter(b2,n) 
    resultat = compléter([], n) #tableau de 0 
    retenue =0 
    for i in range(n-1 , -1 , -1 ):
        x=  b1[i] + b2[i] +retenue
        resultat[i]= x%2
        retenue =  x//2
    if retenue:
        resultat.insert(0, retenue)
    return resultat

def compléter(b: binaire , n : int) -> binaire :
    """"""
    z :binaire = [0]
    if len(b) < n : 
        b= z*(n-len(b))+b
    return b     


  
#3) multuplication par 2 puissance k 

def mul_puissance_2(b: binaire , k : int) -> binaire :
  z :binaire=[0]
  return b+ z*k


#3) multuplication basique 


def mutuplication_bas(b1 :binaire , b2 : binaire )-> binaire : 
    resultat : bin[0]
    n=len(b2)
    for i in range(n) :
        if b2[n-1-i] == 1 : # de  la fin psk (n-1 c'est la fin - i et i c'est 0 au debut si egale 1 on fait comme ca et ca s'increment n-1 -1 donc ca sera a lindice 2 etc )
            resultat[i]=add_binaire(resultat, mul_puissance_2(b1, i)) # ici le i c'est l'indice au debut c'est 0 , et ca se croissent 


    return    resultat


def mult_naive_dpr(a : binaire , b : binaire ) -> binaire : 
    if len(a)> len(b):
        a,b= b, a 
    n=len(b)
    a= compléter(a, n)
    # cas d'arret : 

    if n==1 :
        return [a[0]*b[0]]
    n1= n//2 
    n0 = n - n//2
    a1 , a0 = a[: n1] , a[n1:]
    b1  , b0 = b[: n1] , b[n1:]
    t1=mult_naive_dpr(a1,b1)
    t2=mul_puissance_2(t1, 2*n0)
    t3=mult_naive_dpr(a0,b1)
    t4=mult_naive_dpr(a1,b0)
    t5=add_binaire(t3,t4)
    t6=mul_puissance_2(t5,n0)
    t7=mult_naive_dpr(a0,b0)
    result=add_binaire(t2,t6)
    return add_binaire(result, t7)




def soustraction(b1:binaire, b2: binaire) -> binaire : 
    n=max(len(b1), len(b2))
    b1= compléter(b1,n)
    b2= compléter(b2,n) 
    resultat = compléter([], n) #tableau de 0 

    retenue = 0
    for i in range(n-1 , -1 , -1 ):
        x=  b1[i] - b2[i] -retenue
        if x < 0:
            x += 2
        retenue = 1
    else:
        retenue = 0
    resultat[i] = x
   


def multiplication_dpr_karatsuba(a: binaire, b: binaire) -> binaire:

    n = max(len(a), len(b))
    a = compléter(a, n)
    b = compléter(b, n)

    # Cas d'arrêt
    if n == 1:
        return [a[0] * b[0]]

    # Découpage
    n1 = n // 2
    n0 = n - n1

    a1, a0 = a[:n1], a[n1:]
    b1, b0 = b[:n1], b[n1:]

    # Trois multiplications récursives
    t = multiplication_dpr_karatsuba(a1, b1)
    c = multiplication_dpr_karatsuba(a0, b0)

    d = add_binaire(a0, a1)
    e = add_binaire(b0, b1)

    g = multiplication_dpr_karatsuba(d, e)

    # Calcul des termes croisés
    f = soustraction(g, t)
    h = soustraction(f, c)

    # Décalages
    t2 = mul_puissance_2(t, 2*n0)
    h2 = mul_puissance_2(h, n0)

    # Résultat final
    resultat = add_binaire(t2, h2)
    return add_binaire(resultat, c)


if __name__ == "__main__":
    unittest.main()
     

