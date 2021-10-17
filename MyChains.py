import os.path

class MyChain :
    def __init__(self, chaines_liste):
            try:
                f = open(str(chaines_liste).lower(), "r")
                x = f.readlines()
                ch = ""
                for x0 in x:
                    ch += x0
                self.__chaines_liste = ch
                f.close()
            except(IOError):
                self.__chaines_liste = str(chaines_liste)

    def valeur(self):
        return self.__chaines_liste

    def Fic_lower(self):
        return str(self.__chaines_liste).lower()

    def Fic_uper(self):
        return str(self.__chaines_liste).upper()

class MyChains:
    def __init__(self, chaines_liste1, chaines_liste2):
        self.__chaines_liste1 = MyChain(chaines_liste1).valeur()
        self.__chaines_liste2 = MyChain(chaines_liste2).valeur()

    def valeur(self,numero_argument):
        if (numero_argument==1):
            return self.__chaines_liste1

        elif (numero_argument==2):
            return self.__chaines_liste2
        else:
            return self.concatenate()


    def concatenate(self):
        chaines1 = str(self.__chaines_liste1).split("\n")
        chaines2 = str(self.__chaines_liste2).split("\n")
        n1 = len(chaines1)
        n2 = len(chaines2)
        chaine = ""

        if n1 >= n2:
            for i in range(n1):
                if i in range(n2):
                    x = chaines1[i].lstrip() + chaines2[i]
                    if chaine == "":
                        chaine = x
                    else:
                        chaine = chaine + "\n" + x
                else:
                    x = chaines1[i].lstrip()
                    if chaine == "":
                        chaine = x
                    else:
                        chaine = chaine + "\n" + x
        else :
            for i in range(n2):
                if i in range(n1):
                    x = chaines1[i].lstrip() + chaines2[i]
                    if chaine == "":
                        chaine = x
                    else:
                        chaine = chaine + "\n" + x
                else:
                    x = chaines2[i].lstrip()
                    if chaine == "":
                        chaine = x
                    else:
                        chaine = chaine + "\n" + x

        return chaine

    def generer_fichier(self, nomfic):
        z = self.concatenate()
        if nomfic == "":
            nomfic = "temp.txt"
        f = open(nomfic, "w")
        f.write(z)
        f.close()

def valide_file_name(nomFichier):
    try:
        if os.path.isfile(str(nomFichier)) and str(nomFichier).lower()[-4] == ".txt":
            return True
        else:
            return False
    except (FileExistsError):
        return False

