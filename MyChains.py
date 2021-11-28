import os.path
from datetime import datetime
from mychain import MyChain

class MyChains():
    def __init__(self, chaines1, chaines2=""):
        # super().__init__(chaines1)

        self.__chaines1 = MyChain(chaines1).value()
        self.__chaines2 = MyChain(chaines2).value()

    def value(self, numero_argument=1):
        if (numero_argument == 1):
            return self.__chaines1

        elif (numero_argument == 2):
            return self.__chaines2

        elif (numero_argument == 3):
            return self.concatenate()

        else:
            return self.add()

    def join(self):
        return str(self.__chaines1).join(str(self.__chaines2))

    def joinNot(self):
        if (str(self.__chaines1).count(self.__chaines2) == 0) or (str(self.__chaines2) == ''):
            return self.__chaines1
        else:
            chs = str(self.__chaines1).split(self.__chaines2)
            chh = ""
            for ch in chs:
                chh += ch
            return chh

    def concatenate(self):
        chain1 = str(self.__chaines1).split("\n")
        chain2 = str(self.__chaines2).split("\n")
        n1 = len(chain1)
        n2 = len(chain2)
        chain = ""

        if n1 >= n2:
            for i in range(n1):
                if i in range(n2):
                    x = chain1[i].lstrip() + chain2[i]
                    if chain == "":
                        chain = x
                    else:
                        chain = chain + "\n" + x
                else:
                    x = chain1[i].lstrip()
                    if chain == "":
                        chain = x
                    else:
                        chain = chain + "\n" + x
        else:
            for i in range(n2):
                if i in range(n1):
                    x = chain1[i].lstrip() + chain2[i]
                    if chain == "":
                        chain = x
                    else:
                        chain = chain + "\n" + x
                else:
                    x = chain2[i].lstrip()
                    if chain == "":
                        chain = x
                    else:
                        chain = chain + "\n" + x

        return chain

    def add(self):
        chain1 = str(self.__chaines1).split("\n")
        chain2 = str(self.__chaines2)

        n1 = len(chain1)
        chain = ""

        for i in range(n1):
            x = chain1[i] + chain2
            if chain == "":
                chain = x
            else:
                chain = chain + "\n" + x

        return chain

    def find(self, andCondition=False, caseSensitive=False):
        chain1 = str(self.__chaines1).split("\n")
        chain2 = str(self.__chaines2)

        n1 = len(chain1)
        chain = ""

        # listInString
        for x in chain1:
            # ok = chain2 in x
            ok = listInString(chain2, x, andCondition, caseSensitive)
            if ok:
                if chain == "":
                    chain = x
                else:
                    chain = chain + "\n" + x
        return chain

    def create_file(self, numero_argument=3, nomfic=""):
        if numero_argument == 1:
            z = self.__chaines1

        elif numero_argument == 2:
            z = self.__chaines2

        elif numero_argument == 3:
            z = self.concatenate()

        else:
            z = self.add()

        return createFile(z,nomfic)

    def toString(self, numero_argument=1):
        if numero_argument == 1:
            chaine = self.__chaines1
        else:
            chaine = self.__chaines2
        return chaine

    def toList(self,separateur=","):
        return stringToList(self.__chaines1, separateur)

    def toSet(self,separateur=","):
        return stringToSet(self.__chaines1,separateur)

    def toTuple(self,separateur=","):
        return stringToTuple(self.__chaines1,separateur)

    def remonterCode(self):
        return remonter_code(self.__chaines1, self.__chaines2)

    def descendreCode(self):
        return descendre_code(self.__chaines1, self.__chaines2)

    def decoupeChaine(self,separateur="\t",create_file=False,nom_fic=""):
        list1=self.__chaines1.split("\n")
        n=len(list1)
        chaine=""
        for i in range(n):
            x=list1[i]
            ch=decoupe_chaine(x, self.__chaines2,separateur)
            if chaine=="":
                chaine=ch
            else:
                chaine=chaine + "\n" + ch

        if create_file:
            if nom_fic == "":
                today = str(datetime.now())
                today = today.replace("/", "")
                today = today.replace(":", "")
                today = today.replace(".", "")
                nomfic = "temp_" + today + ".txt"

            try:
                f = open(nomfic, "w")
                f.write(chaine)
                f.close()
            except (IOError):
                print("Nom de fichier invalide ou fichier deja ouvert")

        else:
            return chaine

class MyString(MyChains):
   pass


#***********************************************FONCTION EXTERNES*****************************************************

def valide_file(nomFichier):
    try:
        ext = ["txt", "py", "csv", "ini", "log"]

        # ext_ok = str(nomFichier).lower().split(".")[-1] in ext #Text files only
        ext_ok = True

        if os.path.isfile(str(nomFichier)) and ext_ok:
            return True
        else:
            return False

    except FileExistsError:
        return False

def createFile(chaine,nomfic=""):
    if nomfic == "":
        today = str(datetime.now())
        today = today.replace("/", "")
        today = today.replace(":", "")
        today = today.replace(".", "")
        nomfic = "temp_" + today + ".txt"

    try:
        f = open(nomfic, "w")
        f.write(chaine)
        f.close()
    except (IOError):
        print("Nom de fichier invalide ou fichier deja ouvert")


def listInString(str_List, chaine, andCondition=False, caseSensitive=False):
    if not caseSensitive:
        list_search = str_List.lower().split("\n")
        ch = chaine.lower()
    else:
        list_search = str_List.split("\n")
        ch = chaine

    if not andCondition:
        for x in list_search:
            if str(ch).count(x) > 0:
                return True
        return False
    else:
        ok = True
        for x in list_search:
            n = str(ch).count(x)
            ok = ok and (n > 0)
        if ok:
            return True
        else:
            return False


def listeToString(liste):
    typ = type(liste)
    if typ == list:
        ch = ""
        for x in liste:
            if ch == "":
                ch = x
            else:
                ch = ch + "\n" + x
        return ch
    else:
        return str(liste)


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset + amount]

def car_debut_block(car_fin_block):
    x = car_fin_block
    return {
        ')': '(',
        '}': '{',
        ']': '['
    }.get(x, '')


def car_paire_block(car_block):
    x = car_block
    return {
        '(': ')',
        '{': '}',
        '[': ']',
        ')': '(',
        '}': '{',
        ']': '['
    }.get(x, '')


def contient_car_block(chaine):
    ch0 = "(){}[]"
    n = len(str(ch0))
    for i in range(n):
        x = ch0[i]
        if x in str(chaine):
            return True
    return False


def trouver_car_debut_block(chaine):
    ch = str(chaine)
    n = len(ch)
    x0 = "([{"

    for i in range(n):
        x = ch[i]
        if x != "":
            if x in x0:
                return x
    return ''


def car_fin_block(car_debut):
    x = car_debut
    return {
        '(': ')',
        '{': '}',
        '[': ']'
    }.get(x, '')


def block_complet(Chaine, Car_Debut_Block=""):
    if Car_Debut_Block == "":
        Car_Debut_Block = trouver_car_debut_block(Chaine)
    valide = False

    x = car_fin_block(Car_Debut_Block)
    if (Car_Debut_Block == "" or x == ""):
        valide = False
    else:
        n1 = str(Chaine).count(Car_Debut_Block)
        n2 = str(Chaine).count(x)
        valide = not (Chaine == "") and (n1 == n2) and (n1 > 0)
        if not valide:
            return False

    ch0 = "([{}])"
    ch = str(Chaine)
    chh = ""
    pile = []

    for i in range(len(ch)):
        x = ch[i]
        if x in ch0:
            if len(pile) == 0:
                pile.append(x)
            else:
                y = pile[-1]
                c1 = x
                c2 = ""

                if x in "([{":
                    c2 = car_fin_block(c1)
                if x in ")]}":
                    c2 = car_debut_block(x)

                if y == c2:
                    # Depiler
                    pile = pile[:-1]
                else:
                    pile.append(x)

    if len(pile) == 0:
        return True

    q = len(chh)
    if q % 2 != 0:
        return False
    else:
        q = int(q / 2)
        n = len(chh) - 1

        for k in range(q):
            c1 = chh[k]
            c2 = car_fin_block(c1)
            c3 = chh[n - k]
            valide = (c2 == c3)
            if not valide:
                return False
        return True

def en_commentaire(chaine,liste_separator,debut):
    ch=str(chaine)
    x=mid(ch,debut,1)
    i=ch.find(liste_separator)
    x0='"'
    x1=liste_separator
    k=debut

    if (x==x0) and (i!=-1):
        c1=ch.find(x0,debut)
        c2=ch.find(x0,debut+1)
        if (i>=c1) and (i<=c2):
            c3=mid(chaine,i-1,1)
            c4=mid(chaine,i+1,1)
            if c3!=x0 and c4==x0:
                k=c1
            else:
                k=c2
    return k

def stringToSet(chaine,separateur=","):
    liste1=stringToList(chaine,separateur)
    n=len(liste1)
    set1={''}
    set1.clear()
    for i in range(n):
        set1.add(liste1[i])
    return set1

def stringToTuple(chaine,separateur=","):
    liste1=stringToList(chaine,separateur)
    n=len(liste1)

    if chaine == "":
        return "()"

    if n==1:
        return "(" + liste1[0] +")"

    tuple1=""
    for i in range(n):
        x=liste1[i]
        if i==0:
            tuple1="(" + x + separateur
        elif i==n-1:
            tuple1=tuple1 + " " + x + ")"
        else:
            tuple1=tuple1 +  " " + x + separateur

    return (tuple1)

def stringToList(liste, liste_separator=","):
    typ = type(liste)
    if typ == list:
        return liste
    #
    # elif typ == str:
    #     if liste_separator == "":
    #         list1 = []
    #         list1[:0] = liste
    #         return list1
    else:
        list1 = []
        ch = str(liste)

        if ch=="":
            return list1

        if (ch.find(",") == -1) and (ch.find("\n") >= 0):
            ch=ch.replace("\n",",")

        ch = ch.replace("\n", "")
        n = len(ch)
        x0 = liste_separator
        if not(x0 in ch):
            if not("\n" in ch):
                if ch[0]=="[" and ch[n-1]=="]":
                    x=mid(ch,1,n-2)
                    list1.append(x)
                    return list1

        ch = ch.strip()
        n = len(ch)
        k = ch.count(x0)
        if k == 0:
            list1.append(ch)
            return list1
        else:
            list1 = []
            chaine =str(ch)
            n=len(chaine)

            if chaine=="":
                return list1

            c1=trouver_car_debut_block(chaine)
            c2=car_fin_block(c1)
            if (chaine[0]==c1) and (chaine[n-1]==c2):
                chaine =mid(chaine,1,n-2).strip()

            n = len(chaine)
            i = 0
            debut_block = 0

            while i < n:
                # 'Verifier si on est au debut d'un block sur la ligne courante
                i1=chaine.find(x0,i)
                #verifier si le separateur n'est pas dans un commentaire "nom, prenoms" si oui l'ignoer et passer au suivant
                ii=en_commentaire(chaine,liste_separator,i)
                if ii>i1:
                    i1 = chaine.find(x0, ii)

                if i1==-1:
                    k=n-debut_block
                    if k>0:
                        x = mid(chaine, debut_block, k).strip()
                        list1.append(x)
                    return list1

                x=mid(chaine,debut_block,i1-debut_block).strip()
                if block_complet(x):
                    list1.append(x)
                    i = i1 +1
                    debut_block=i
                else :

                    if not contient_car_block(x):
                        list1.append(x)
                        i = i1+1
                        debut_block=i
                    else:
                        i = i1+1

            return list1



def block_remontable(chaine):
    if chaine == '':
        return False
    else:
        valide = False
        x0 = trouver_car_debut_block(chaine)
        if not x0 == '':
            valide = block_complet(chaine, x0)
        return valide


def remonter_block(chaine, Car_Remontee=","):
    ch = str(chaine)
    x = str(Car_Remontee)

    if ch.count(x) == 0:
        return ch
    else:
        x0 = "\n"
        while ch.count(x0) > 0:
            ch = ch.replace(x0, "")

        return ch

def remonter_code(chaine_code, car_remontee=","):
    List1 = []
    Lst_tmp = str(chaine_code).split("\n")
    k = len(Lst_tmp)
    for i in range(k):
        List1.append(Lst_tmp[i])

    List3 = []

    n = len(List1)
    i = 0
    while i < n:
        # 'Verifier si on est au debut d'un block sur la ligne courante
        C = str(List1[i])
        X = trouver_car_debut_block(C)
        if X == "":
            List3.append(List1[i].strip())
            i += 1
        elif block_complet(C, trouver_car_debut_block(C)):
            List3.append(List1[i].strip())
            i += 1
        else:
            # 'Trouver le block_Selectionne
            Block_Selectionne = ""
            k = i
            List2 = []
            X1 = ""
            #           Fin_Premier_Block = False
            stop = False
            while (k <= n - 1) and (not stop):
                Block_Selectionne = Block_Selectionne + List1[k].strip()
                List2.append(List1[k])

                # 'Verifier si on a attein la fin d'un block contigu
                if X1 == "":
                    X1 = trouver_car_debut_block(Block_Selectionne)
                    if X1 != "":
                        if block_complet(Block_Selectionne, X1):
                            stop = True
                else:
                    if block_complet(Block_Selectionne, X1):
                        Fin_Premier_Block = True
                        stop = True

                k = k + 1
                if not (k <= n - 1):
                    stop = True

            if block_remontable(Block_Selectionne):
                List3.append(remonter_block(Block_Selectionne, car_remontee).strip())
            else:
                List3.append(Block_Selectionne.strip())
            i = k
    ch = ""
    q = len(List3)

    for i in range(q):
        if i < q - 1:
            ch = ch + List3[i] + "\n"
        else:
            ch = ch + List3[i]

    return ch

def descendre_chaine(chaine,separateur=","):

    x1 = trouver_car_debut_block(chaine)
    chh=chaine
    prefixe=""
    sufixe=""
    if x1!="":
        i1=chaine.find(x1)
        i2=chaine.rfind(car_fin_block(x1))
        prefixe=mid(chaine,0,i1)
        chh = mid(chaine, i1, i2 - i1 + 1)

        n = len(chaine)
        if n-1-i2>0:
            i2=i2+1
            sufixe=mid(chaine,i2,len(chaine)-i2)

        #Transformer le block en format liste remplacer les accolades ou parentese de debut par des crochet
        if x1!="[":
            k1=1
            k2=len(chh)-2
            chh1="["+ mid(chh,k1,k2-k1+1) +"]"
            chh=chh1

    list1 = stringToList(chh, separateur)
    x0=mid(chh,0,1)
    borne_ok=x0 in "[{("
    if borne_ok:
        if len(list1)>1:
            ch= x1 + "\n"
        else:
            ch=x1
    else:
        ch=""

    n=len(list1)
    for i in range(n):
        if i<len(list1)-1:
            if len(list1)>1:
                ch=ch + list1[i] + " " + separateur + "\n"
            else:
                ch = ch + list1[i]
        else:
            ch=ch +list1[i]

    if borne_ok:
        if len(list1)>1:
            ch=ch  + "\n" + car_fin_block(x1)
        else:
            ch = ch + car_fin_block(x1)

    ch=prefixe +ch + sufixe
    return ch

def descendre_code(chaine_code, caractere_separation=","):
    List1 = []
    Lst_tmp = str(chaine_code).split("\n")
    k = len(Lst_tmp)
    for i in range(k):
        List1.append(Lst_tmp[i])

    List3 = []

    n = len(List1)
    i = 0
    while i < n:
        # 'Verifier si on est au debut d'un block sur la ligne courante
        C = str(List1[i])
        X = trouver_car_debut_block(C)
        if X == "":
            List3.append(List1[i].strip())
            i += 1
        else:
            # 'Trouver le block_Selectionne
            Block_Selectionne = ""
            k = i
            # List2 = []
            X1 = ""
            #           Fin_Premier_Block = False
            stop = False
            while (k <= n - 1) and (not stop):
                Block_Selectionne = Block_Selectionne + List1[k].strip()
                # List2.append(List1[k])

                # 'Verifier si on a attein la fin d'un block contigu
                if X1 == "":
                    X1 = trouver_car_debut_block(Block_Selectionne)
                    if X1 != "":
                        if block_complet(Block_Selectionne, X1):
                            stop = True
                else:
                    if block_complet(Block_Selectionne, X1):
                        Fin_Premier_Block = True
                        stop = True

                k = k + 1
                if not (k <= n - 1):
                    stop = True

            if block_remontable(Block_Selectionne):
                List3.append(descendre_chaine(Block_Selectionne,caractere_separation))
            else:
                List3.append(Block_Selectionne.strip())
            i = k
    ch = ""
    q = len(List3)

    for i in range(q):
        if i < q - 1:
            ch = ch +  List3[i] + "\n"
        else:
            ch = ch +  List3[i]

    return ch

def decoupe_chaine(chaine,plan_decoupe,separateur):
    if type(plan_decoupe)==list:
        list1=plan_decoupe
    else:
        list1=stringToList(plan_decoupe)

    ok=True
    list2 = []
    x0=separateur

    for i in range(len((list1))):
        ok=ok and list1[i].isdigit()
        if not ok :
            break
    if ok:
        for i in range(len(list1)):
            list2.append(int(list1[i]))
    else:
        for i in range(len(list1)):
            list2.append(len(list1[i]))

    ch=""
    for i in range(len(list2)):
        l=int(list2[i])
        n=len(chaine)
        if l<n:
            ch1=left(chaine,l)
            chaine=mid(chaine,l+1,len(chaine)-l)
            ch=ch + ch1 + x0
        else:
            ch=ch + chaine
            break
    if chaine!="":
        ch=ch + chaine

    return ch