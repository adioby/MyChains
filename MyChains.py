import os.path
from datetime import datetime

class myChain:
    def __init__(self, chaine):
        try:
            f = open(str(chaine).lower(), "r")
            x = f.readlines()
            ch = ""
            for x0 in x:
                ch += x0
            self.__chaine = str(ch)
            f.close()

        except (IOError):
            self.__chaine = str(chaine)

    def value(self):
        return self.__chaine


class myChains:
    def __init__(self, chaines1, chaines2=""):
        self.__chaines1 = myChain(chaines1).value()
        self.__chaines2 = myChain(chaines2).value()
        # self.__chaines3 = self.add()

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

    def create_str(self, numero_argument=1):
        my_list = str("")

        if numero_argument == 1:
            z = self.__chaines1

        else:
            z = self.__chaines2

        return z

    def create_list(self, numero_argument=1):
        my_list = [" "]
        if numero_argument == 1:
            z = self.__chaines1
        else:
            z = self.__chaines2

        ch = str(z).split("\n")

        my_list.remove(" ")
        for x in ch:
            my_list.append(x)

        return my_list

    def create_set(self, numero_argument=1):
        my_set = {" "}

        if numero_argument == 1:
            z = self.__chaines1

        else:
            z = self.__chaines2
        ch = str(z).split("\n")

        my_set.remove(" ")
        for x in ch:
            my_set.add(x)

        return my_set

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

        if nomfic == "":
            today = str(datetime.now())
            today = today.replace("/", "")
            today = today.replace(":", "")
            today = today.replace(".", "")
            nomfic = "temp_" + today + ".txt"

        try:
            f = open(nomfic, "w")
            f.write(z)
            f.close()
        except (IOError):
            print("Nom de fichier invalide ou fichier deja ouvert")

    def toList(self):
        return stringToList(self.__chaines1, self.__chaines2)


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


def stringToList(liste, liste_separator=""):
    typ = type(liste)
    if typ == str:
        if liste_separator == "":
            list1 = []
            list1[:0] = liste
            return list1
        else:
            return str(liste).split(liste_separator)
    else:
        return str(liste).split(liste_separator)
