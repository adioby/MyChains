from MyChains import MyChains, MyChain, valide_file

x = "self.__Nom\nself.__Prenoms\nself.__CodeUser\nself.__Matricule \nself.__CAI\nself.__Sexe\nself.__Telephone\nself.__Email "
y = "=Nom\n=Prenoms\n=CodeUser\n=Matriculate\n=CAI\n=Sexe\n=Telephone\n=Email"

f1 = "fred1.txt"
f2 = "fred2.txt"
nom_fic = "fred3.txt"
f4 = "MyChains.py"
# print(valide_file(f4))

# print(MyChains("MyChains.py").valeur().lower())
ch = MyChains(x, y)
# print("************************************************")
#
# ch=MyChains(f1,f2)
# print((ch.value().upper()))
# print(len(ch))

# MyChains(f1," = ").add()


# print(ch.valeur(4))

#
# ch = MyChains(x, y)
# print(ch)
# ch.generer_fichier(nom_fic)
# x1=ch.valeur(5)
# print(x1)

#
#  ch = MyChain(f1)
# print(MyChain("fred2.txt").valeur())
#
# # print(ch.concatenate())
# # ch.generer_fichier(nom_fic)
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

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.get("year"))

# set1 = {"apple", "banana", "cherry"}
# set2 = {3, 5, 7, 9, 3}
# set3 = {True, False, False}
# ch=str(set1)
# print(ch)
#
# set1.remove("banana")
# ch=str(set1)
# print(ch)

xx = MyChains("fred1.txt").create_str()
print(xx)