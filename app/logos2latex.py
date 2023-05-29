""" Funciones para traducir del lenguaje funcional de lógos a LaTeX."""

def LNOT(a):
    """Crear expresión para aplicar el símbolo de negación en LaTeX."""
    return '\\lnot('+a+')'

def LAND(a,b):
    """Crear expresión para aplicar el símbolo de conjunción en LaTeX."""
    return '('+a+'\\land '+b+')'

def LOR(a,b):
    """Crear expresión para aplicar el símbolo de disyunción en LaTeX."""
    return '('+a+'\\lor '+b+')'

def LIF(a,b):
    """Crear expresión para aplicar el símbolo de condicional en LaTeX."""
    return '('+a+'\\rightarrow '+b+')'

def LFF(a,b):
    """Crear expresión para aplicar el símbolo de bicondicional en LaTeX."""
    return '('+a+'\\leftrightarrow '+b+')'

def LNR(a,b):
    """Crear expresión para aplicar el símbolo de negación conjunta en LaTeX."""
    return '('+a+'\\downarrow '+b+')'

def LXR(a,b):
    """Crear expresión para aplicar el símbolo de disyunción exclusiva
        en LaTeX."""
    return '('+a+'\\oplus '+b+')'

def logos2latex(a, varlist):
    """Retorna cadena traducida del lenguaje funcional de lógos a LaTeX."""
    for j, var in enumerate(varlist):
        exec(var.upper()+" = "+"'"+var.upper()+"'")
    a.upper()
    a = a.replace("NOT","LNOT")
    a = a.replace("AND","LAND")
    a = a.replace("OR","LOR")
    a = a.replace("IF","LIF")
    a = a.replace("FF","LFF")
    a = a.replace("NR","LNR")
    a = a.replace("XR","LXR")
    return eval(a)
