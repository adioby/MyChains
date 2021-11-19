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
    
 
def  Block_Remontable(chaine):
     if chaine=='':
         return False
     else :
        valide = False
        x0 = Trouver_Car_Debut_Block(chaine)
        if not x0=='':
            valide = Block_Complet(chaine, x0)
        return valide


def Remonter_Block(chaine, Car_Remontee=","):
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
                    ch = "\n" + x
                else:
                    ch = ch + "\n" + x
            else:
                if not(x in ch0) and not (x in ch1):
                    if ch == "":
                        ch = x
                    else:
                        ch = ch + x
    return ch


def Descendre_Code(Chaine_Code, Caractere_Separation=","):
    if not Block_Complet(Chaine_Code,Trouver_Car_Debut_Block(Chaine_Code)):
        return Chaine_Code
    # remove all existing break lines

    ch = str(Chaine_Code)
    ch = ch.replace("\n", "")

    x0 = str(Caractere_Separation)
    if not (x0 in ch):
        return ch
    
    T = str(ch).split(x0)
    n = len(T)
    
    ch = ""
    
    for i in range(n):
        x = T[i].strip()
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


def Remonter_Code(Chaine_Code,Car_Remontee=",", Toute_La_Liste=True):

    # X0, X1, X, CH, XX
    Tout=Toute_La_Liste
    list1=[]
    List1=str(Chaine_Code).split("\n")

    Debut_Block=False
    Fin_Block=False

    CH = ""
    CH0 = "{(["
    CH1 = ")]}"

    XX = ""
    kkkk = 0

    List19=[]

    Debut_Selection=False
    Fin_Selection=False

    Block_Selectionne=""

    Fin_Premier_Block=False

    # for i in 0..list1.zise
    #         'Ligne_Fic = List1.List(i)
    #         Debut_Selection = False
    #         Fin_Selection = False
    #
    #         If (List1.Selected(i)) Or Tout Then
    #             'Verifier si on est au debut d'un block sur la ligne courante
    #             X = Trouver_Car_Debut_Block(List1.List(i))
    #             If X = "" Then
    #                 List19.AddItem List1.List(i)
    #                 GoTo Ignorer
    #             End If
    #
    #             Debut_Selection = True
    #             Block_Selectionne = ""
    #
    #             'Trouver le block_Selectionne
    #             k = i
    #             List20.Clear
    #             X1 = ""
    #             Fin_Premier_Block = False
    #
    #             Do While (k <= List1.ListCount - 1) And ((List1.Selected(k)) Or Tout)
    #                 Block_Selectionne = Block_Selectionne & List1.List(k)
    #                 List20.AddItem List1.List(k)
    #
    #                 'Verifier si on a attein la fin d'un block contigu
    #                 If X1 = "" Then
    #                     X1 = Trouver_Car_Debut_Block(Block_Selectionne)
    #                     If X1 <> "" Then
    #                         If Block_Complet(Block_Selectionne, X1) Then
    #                             Fin_Premier_Block = True
    #                             GoTo Sortir
    #                         End If
    #                     End If
    #                 Else
    #                     If Block_Complet(Block_Selectionne, X1) Then
    #                         Fin_Premier_Block = True
    #                         GoTo Sortir
    #                     End If
    #                 End If
    #
    #                 k = k + 1
    #                 If Not (k <= List1.ListCount - 1) Then
    #                     GoTo Sortir
    #                 End If
    #             Loop
    # Sortir:
    #
    #             If Not Tout Then
    #                 If k <= (List1.ListCount - 1) Then
    #                     Fin_Selection = (List1.Selected(k) = False)
    #                 End If
    #
    #                 If Fin_Selection And (Not Fin_Premier_Block) Then
    #                     k = k - 1
    #                 End If
    #             End If
    #
    #             If Block_Remontable(Block_Selectionne) Then
    #                 List19.AddItem Remonter_Block(Block_Selectionne, Car_Remontee)
    #             Else
    #                 For Q = 0 To List20.ListCount - 1
    #                     List19.AddItem List20.List(Q)
    #                 Next Q
    #             End If
    #
    #             X1 = ""
    #             i = k
    #
    #         Else
    #             List19.AddItem List1.List(i)
    #         End If
    #
    # 'Cas des lignes non traitées
    # Ignorer:
    #
    # Next i


x=myChain("fred.txt").value()

print(Descendre_Code(x))
print("********************************")
print(Remonter_Block(x))

# print(Descendre_Code(y))