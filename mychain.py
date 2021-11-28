class MyChain:
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