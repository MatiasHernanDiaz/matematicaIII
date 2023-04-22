# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:21:50 2023

@author: Matias
"""


def interConjuntos(*conj):
    """
    Interseccion entre todo los conjuntos pasados por parametro
    
    Parameters
    ----------
    *conj : TYPE set, recibe multiples conjuntos
        DESCRIPTION. se colocan

    Returns
    -------
    C : TYPE set
        DESCRIPTION. nuevo set

    """
    C = conj[0].copy()
    for i in conj:
        C.intersection_update(i)
    return C


def difConjuntos(*conj):
    """
    Diferencia entre el primero conjunto pasado por parametros y los sucesivos
    conjuntos de parametros

    Parameters
    ----------
    *conj : TYPE set
        DESCRIPTION. 

    Returns
    -------
    C : TYPE set
        DESCRIPTION. nuevo set 

    """
    
    C = conj[0].copy()
    for e,i in enumerate(conj, start = 0):
        if(e !=0): C.difference_update(i)
    return C

def uniConjuntos(*conj):
    """
    Union entre todos los conjuntos pasados por parametro

    Parameters
    ----------
    *conj : TYPE set
        DESCRIPTION.

    Returns
    -------
    C : TYPE set
        DESCRIPTION. nuevo set

    """
    C = set()
    for i in conj:
        C.update(i)
    return C


def completarVenn3(A,B,C):
    """
    Arma un diccionario con la identificacion de cada subconjunto para
    faciliat el armado del grafico del diagrama de Venn3
    
    para la utilizacion usar:
        for k,v in completarVenn3.items():
            diagrama.get_label_by_id(k).set_text(v)

    Parameters
    ----------
    A : TYPE set
        DESCRIPTION.
    B : TYPE set
        DESCRIPTION.
    C : TYPE set
        DESCRIPTION.

    Returns
    -------
    subConjuntos : TYPE dict
        DESCRIPTION. diccionario con clave de referencia a subconjuntos y
        valores set()

    """
    
    centro = interConjuntos(A,B,C)
    soloA = difConjuntos(A,B,C)
    soloB = difConjuntos(B,A,C)
    soloC = difConjuntos(C,B,A)
    CiAdB = difConjuntos(interConjuntos(C,B),A)
    AiCdB = difConjuntos(interConjuntos(A,C),B)
    AiBdC = difConjuntos(interConjuntos(A,B),C)
    
    subConjuntos = dict()
    subConjuntos["001"] = soloC
    subConjuntos["010"] = soloB
    subConjuntos["011"] = CiAdB
    subConjuntos["100"] = soloA
    subConjuntos["101"] = AiCdB
    subConjuntos["110"] = AiBdC
    subConjuntos["111"] = centro
    
    return subConjuntos


def sumaElementos(conjunto):
    if isinstance(conjunto, dict):
        return sum(conjunto.values())
    else:
        return sum(conjunto)

def convertirASet(conjunto):
    if isinstance(conjunto,dict):
        return set(conjunto.values())
    else:
        return set(conjunto)

if(__name__=="__main__"):
    
    import matplotlib.pyplot as plt
    from matplotlib_venn import venn3
    
    B = [3,5,10,12]
    M = {"a":10,"b":20,"c":15,"d":5}
    U = (12,10,20,18)
    
    print("Suma de los valores de cada tipo")
    print(f"{B} = {sumaElementos(B)}")
    print(f"{M} = {sumaElementos(M)}")
    print(f"{U} = {sumaElementos(U)}")
    
    print("Convierte los diferentes tipos en set")
    b = convertirASet(B)
    m = convertirASet(M)
    u = convertirASet(U)
    
    print(b)
    print(m)
    print(u)
    
    inter = interConjuntos(b,m,u)
    dif = difConjuntos(b,m,u)
    union = uniConjuntos(b,m,u)
   
    print(f"Interseccion {inter}")
    print(f"diferencia {dif}")
    print(f"union {union}")
   
        
    diagrama = venn3([b,m,u], set_labels=("B","M","U"))
    
    for k,v in completarVenn3(b, m, u).items():
        diagrama.get_label_by_id(k).set_text(v)
    
    plt.title("Diagrama de Venn")
    plt.show()