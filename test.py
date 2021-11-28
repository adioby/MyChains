from myChains import myChains, myChain, valide_file,listeToString,stringToList

x = "self.__Nom\nself.__Prenoms\nself.__CodeUser\nself.__Matricule \nself.__CAI\nself.__Sexe\nself.__Telephone\nself.__Email "
y = "om\nPrenom" #"\n=CodeUser\n=Matriculate\n=CAI\n=Sexe\n=Telephone\n=Email"
# z=["om","nom"]
z0="om , nom"
f1 = "fred1.txt"
f2 = "fred2.txt"
nom_fic = "fred3.txt"
# f4 = "myChains.py"
# f5="C:\Temp\jde_log\ACS.splf-331176694244807445.txt"
# f6="C:\Temp\jde_log\ACS.splf-3204451050875517401.txt"
# search="Total size :"
#
z=stringToList(z0)
ch=myChains(x,listeToString(z)).find()

# ch=myChains(x,stringToList(z)).find()

print(ch)

# Python code to convert string to list character-wise
# str1="aDIOBY, alfred"
# print(str1.count("a"))
