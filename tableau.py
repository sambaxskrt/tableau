import random

# création d'un tableau de n entiers aléatoires compris entre 0 et N

def creation_tableau(N,n):
    tableau = []
    for i in range(n):
        tableau.append(random.randint(0,N))
    return tableau

T=creation_tableau(100,15)

def recherche_occurrence(tableau, element):
    """
    recherche l'indice d'une occurrence d'un élément dans un tableau
    :param tableau: (list) un tableau
    :param element:(any)
    :return: (int)
    :CU: elt appartient à tableau
    """
    indice = 0
    while indice != len(tableau) and tableau[indice] != element:
        indice += 1
    return indice

def recherche_max(tableau):
    """
    recherche le maximum parmi les valeurs d'un tableau d'entiers
    :param tableau: (list) un tableau
    :return: (int)
    """
    maxi = tableau[0]
    for i in range(1,len(tableau)):
        if tableau[i] > maxi:
            maxi = tableau[i]
    return maxi

def recherche_min(tableau):
    """
    recherche le minimum parmi les valeurs d'un tableau d'entiers
    :param tableau: (list) un tableau
    :return: (int)
    """
    mini = tableau[0]
    for i in range(1,len(tableau)):
        if tableau[i] < mini:
            mini = tableau[i]
    return mini

def recherche(tableau, element):
    """
    recherche un élément dans un tableau d'entiers triés
    :param tableau: (list) un tableau
    :param element: (int) un entier
    :CU: tableau doit être trié
    :return: (int) -1 si l'element n'est pas dans le tableau, l'indice d'une occurrence de l'element sinon
    """
    indice_gauche = 0
    indice_droit = len(tableau)-1
    indice_milieu = (indice_gauche + indice_droit) // 2
    while element != tableau[indice_milieu] and indice_gauche < indice_droit:
        if element < tableau[indice_milieu]:
            indice_droit = indice_milieu -1
        else:
            indice_gauche = indice_milieu + 1
        indice_milieu = (indice_gauche + indice_droit) // 2
    if element == tableau[indice_milieu]:
        return indice_milieu
    else:
        return len(tableau)
    
def somme(tableau):
    """
    recherche la somme des elements d'un tableau d'entiers
    :param tableau: (list) un tableau
    :return: (int)
    """
    somme = 0
    for elt in tableau:
        somme += elt
    return somme

def moyenne(tableau):
    """
    recherche la moyenne des elements d'un tableau d'entiers
    :param tableau: (list) un tableau
    :return: (float)
    """
    somme = 0
    for elt in tableau:
        somme += elt
    return somme/len(tableau)

def echange(tableau, i, j):
    """
    echange les éléments d'indice i et j d'un tableau
    :param tableau: (list) un tableau
    :param i:(int) un entier
    :param j:(int) un entier
    :CU: 0 <= i < len(tableau)
        0 <= j < len(tableau)
    :return: (None)
    :Side-effects: Le tableau est modifié
    """
    tableau[i], tableau[j] = tableau[j], tableau[i]
    
def tri_selection(tableau):
    """
    trie un tableau
    :param tableau: (list) un tableau
    :return: (list) le tableau trié
    :Side-effects: Le tableau est modifié
    """    
    for i in range(len(tableau)):
        indice_mini = i
        for j in range(i+1, len(tableau)):
            if tableau[indice_mini] > tableau[j]:
                indice_mini = j
        echange(tableau, i, indice_mini)
    return tableau

def insertion(tableau, element):
    """
    insère un élément dans un tableau d'entiers triés
    :param tableau: (list) un tableau
    :param element: (int) un entier
    :CU: tableau doit être trié
    :return: (None)
    :Side-effects: Le tableau est modifié
    """
    indice = 0
    while len(tableau) != 0 and indice != len(tableau) and tableau[indice] < element:
        indice += 1
    return tableau[:indice]+[element]+tableau[indice:]

def tri_insertion(tableau):
    """
    trie un tableau
    :param tableau: (list) un tableau
    :return: (list) le tableau trié
    """
    resultat = []
    for i in range(len(tableau)):
        resultat = insertion(resultat, tableau[i])
    return resultat