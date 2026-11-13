#pcc = plus court chemin

def pcc_ascendant(mat : list[list[int]]) -> list[list[int]]:
    """renvoie la matrice des longueurs optimales
    des chemins de la case (0,0) à la case (n-1,m-1)
    si mat possède n lignes et m colonnes
    procède ligne par ligne, de gauche à droite
    et de haut en bas

    Args:
        mat: matrice d'entiers du coût de chaque case*
    """
    f =[[None] * len(mat[0]) for i in range(len(mat))] 

    # on remplit la premiere ligne 
    f[0][0]=mat[0][0]
    for i in range (1,len(mat[0])):
        f[0][i]=f[0][i-1] +mat[0][i]

        # on remplit la première colone : 
        for j in range(len(mat)):
            f[i]=f[i][0]+mat[i][0]

        for i in range(1,len(mat)):
            for j in range (1,len(mat[0])):
                    f[i][j]=min(f[i-1][j], f[i][j-1])+mat[i][j]    
                    
    pass


def chemin_optimal(f : list[list[int]])-> list[tuple[int]]:
    """Renvoie un chemin optimal à partir de la matrice
    des résultats "f"

    Args:
        f (list[list[int]]): matrice des longueurs optimales,
            déjà calculée

    Returns:
        list[tuple[int]]: suite de sommets 
            du chemin ex: [(0,0),(0,1),(1,1),(2,1),...]
    """




def pcc_descendant(mat, i,j, memo={}):
    """renvoie la longueur du plus court chemin de (0,0) ) (i,j)

    Args:
        mat (_type_): matrice entière
        i : entier
        j : entier
        memo (dict, optional): mémoïsation
    """



mat = [[2,-1,3,0,2,1],
    [1,1,1,-2,-2,2],
    [-2,10,7,-1,3,3],
    [4,-3,-1,1,-3,2],
    [2,4,4,12,4,1],
    [-10,1,0,8,-4,0]]