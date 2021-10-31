from myChains import myChains, myChain

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def Trouver_Car_Debut_Block(chaine) :
    ch = str(chaine)
    n = len(ch)
    x0 = "([{"

    for i in range(n):
        x = ch[i]
        if x != "" :
            if x in x0 :
                return x


def Car_Fin_Block(Car_Debut_Block) :
    x = Car_Debut_Block
    return {
        '(': ')',
        '{': '}',
        '[':']'
    }.get(x, '') 


def Cas_Ligne_Descendable (chaine) :
    ch = chaine   
    return ("{" in ch)  or ("}" in ch) or ("(" in ch) or (")" in ch)  or ("[" in ch)  or ("]" in ch)


def Trouver_Caractere_Remontee_Descente(chaine):
    ch = chaine
    if not Cas_Ligne_Descendable(chaine):
        return ''
    else:
        x = ','
        if x in ch:
            return x
        else:
            x = ';'
            if x in ch:
                return x
    

def Block_Complet(Chaine, Car_Debut_Block):
    x = Car_Fin_Block(Car_Debut_Block)
    n1 = str(Chaine).count(Car_Debut_Block)
    n2 = str(Chaine).count(x)

    valide= not (Chaine == "") and(n1==n2) and (n1 > 0)

    return valide
    
 
def  Block_Remontable(chaine)  :  
     if chaine=='':
         return False
     else :
        valide = False
        x0 = Trouver_Car_Debut_Block(chaine)
        if not x0=='':
            valide = Block_Complet(chaine, x0)
        return valide


def Remonter_Block(chaine, Car_Remontee):
    ch = str(chaine)
    x = str(Car_Remontee)

    if ch.count(x) == 0 :
        return ch
    else :
        x0="\n"
        while  ch.count(x0)>0:
            ch =ch.replace(x0,"")

        return ch


def Descendre_Ouverture_Fermeture(chaine) :
    ch0 = "{(["
    ch1 = ")]}"  
    ch = ""
    for i in range(len(str(chaine))) :
        x = str(chaine)[i]
        if (x in ch0) and not (x in ch1) :

            if ch == "" :
                ch = x + "\n"
            else:
                ch = ch + x + "\n"
        else:        
            if not(x in ch0) and (x in ch1) :
                if ch == "":
                    ch = "\n"+ x
                else:
                    ch = ch + "\n" + x
            else :
                if not(x in ch0) and not (x in ch1) :
                    if ch == "":
                        ch = x
                    else:
                        ch = ch + x
    return ch


def Descendre_Code(Chaine_Code, Caractere_Separation=","):
    if not Block_Complet(Chaine_Code,Trouver_Car_Debut_Block(Chaine_Code)):
        return Chaine_Code

    ch = str(Chaine_Code)
    x0 = str(Caractere_Separation)
    if not (x0 in ch) :
        return ch
    
    T = str(ch).split(x0)
    n = len(T)
    
    ch = ""
    
    for i in range(n):
        x = T[i]
        if i < n-1:
            if i == 0:
                ch = Descendre_Ouverture_Fermeture(x) + " " + x0 + "\n"
            else:
                # 'verifier si le dernier caractere est identique au separateur si oui pas de retour a la ligne
                if (i == n - 1) and (right(Chaine_Code, len(Caractere_Separation)) == Caractere_Separation):
                    ch = ch + x + " " + x0
                else:
                    ch = ch + x + " " + x0 + "\n"
        
        
        else:
            if not x == "":
                ch = ch + " " + Descendre_Ouverture_Fermeture(x)
    
    return ch

x="def listInString(str_List, chaine, andCondition=False, caseSensitive=False):"
y=myChain("fred.txt").value()

print(Descendre_Code(y))