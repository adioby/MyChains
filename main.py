from MyChains import MyChains,MyChain


x = "self.__Nom\nself.__Prenoms\nself.__CodeUser\nself.__Matriculate"
# \nself.__CAI\nself.__Sexe\nself.__Telephone\nself" \    ".__Email "

y = "=Nom\n=Prenoms\n=CodeUser\n=Matriculate\n=CAI\n=Sexe\n=Telephone\n=Email"

f1 = "fred1.txt"
f2 = "fred2.txt"
nom_fic = "fred4.txt"

# ch = MyChains(fic1, fic2)
#
# ch = MyChains(x, y)
# # print(ch.concatenate())
# # ch.generer_fichier(nom_fic)
# x1=ch.valeur(5)
# print(x1)


# ch = MyChain(f1)
print(MyChain("fred2.txt").valeur())

# print(ch.concatenate())
# ch.generer_fichier(nom_fic)
# x1=ch.valeur(3)
# print(x1)




#
# ch=MyChain(x,y)
# ch.generer_fichier(nom_fic)

# f1 = open("fred1.txt", "r")
# fichier1 = f1.readlines()
# f1.close()
#
# ch=""
# for x in fichier1:
#     ch +=x
#
# print(fichier1)
# print(ch)
