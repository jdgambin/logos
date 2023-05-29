"""Modulo que contiene el motor inferencial lógos."""

import itertools

#
# Inicio de la definición de funciones de asistencia.
#

# Funciones para asistir en la creación y evaluación de tablas de verdad del
# motor inferencial.

def andinsert(a, b):
    """Retorna una cadena en la que se insertan dos proposiciones-literal como
        argumentos de una función AND-literal."""
    return "AND(" + a + "," + b + ")"

def commainsert(a,b):
    """Retorna una cadena en la que se insertan dos variables-literal separadas
        por coma."""
    return a + ", " + b

def commavars(varlist):
    """Retorna una cadena de N variables-literal separadas por coma, las inserta
        en la cadena de manera recursiva."""
    np = len(varlist)
    if np == 1:
        return varlist[0]
    if np == 2:
        return commainsert(varlist[0], varlist[1])
    joinedvars = [ commainsert(varlist[0], varlist[1]) ]
    return commavars(joinedvars + varlist[2:])

def andvars(props):
    """Retorna una cadena con funciones AND-literal anidadas para la conjunción
        de N proposiciones-literal, las inserta en la cadena de manera
        recursiva."""
    np = len(props)
    if np == 1:
        return props[0]
    if np == 2:
        return andinsert(props[0], props[1])
    joinedprops = [ andinsert(props[0], props[1]) ]
    return andvars(joinedprops + props[2:])

#
# Fin de la definición de funciones de asistencia.
#

#
# Inicio de la codificación del motor inferencial (lógos).
#

# Funciones que formalizan las conectivas lógicas.

def NOT(p):
    """
        Conectiva: 'Negación'.

        P | ¬P
        ------
        T   F
        F   T 
    """
    return not p

def AND(p, q):
    """
        Conectiva: 'Conjunción'.

        P | Q | P^Q
        -----------
        T   T   T
        T   F   F
        F   T   F
        F   F   F
    """
    return p and q

def OR(p, q):
    """
        Conectiva: 'Disyunción'.

        P | Q | PvQ
        -----------
        T   T   T
        T   F   T
        F   T   T
        F   F   F
    """
    return p or q

def IF(p, q):
    """
        Conectiva: 'Condicional'.

        P | Q | P->Q
        ------------
        T   T   T
        T   F   F
        F   T   T
        F   F   T
    """
    return (not p) or q

def FF(p, q):
    """
        Conectiva: 'Bicondicional'.

        P | Q | P<->Q
        -------------
        T   T   T
        T   F   F
        F   T   F
        F   F   T
    """
    return AND(IF(p, q), IF(q, p))

def NR(p, q):
    """
        Conectiva: 'Negación conjunta'.

        P | Q | NOR(P,Q)
        ----------------
        T   T   F
        T   F   F
        F   T   F
        F   F   T
    """
    return (not p) and (not q)

def XR(p, q):
    """
        Conectiva: 'Disyunción excluyente'.

        P | Q | XOR(P,Q)
        ----------------
        T   T   F
        T   F   T
        F   T   T
        F   F   F
    """
    return OR(AND(p, NOT(q)), AND(NOT(p), q))

# Función que verifica la implicación entre premisas y conclusión de un
# argumento.

def isvalidarg(prems, concprop, allvars):
    """Verificar implicación entre las premisas-literal (prems) y la
        conclusión-literal (concprop), las cuales contienen
        varias variables-literal (allvars)."""
    nvars = len(allvars)
    concprop = concprop.upper()
    conjprems = andvars(prems).upper()
    varlist = commavars(allvars)
    posstruthvalues = list(set(list(itertools.permutations([True, False]*nvars,
        nvars))))

    implication = True

    for tv in posstruthvalues:
        exec(varlist.upper() + " = " + str(tv))
        if not eval("IF(" + conjprems + ", " + concprop + ")"):
            implication = False
            break

    return implication

#
# Fin de la codificación del motor inferencial (lógos).
#
