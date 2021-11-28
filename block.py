from mychains import MyChains,MyString, remonter_code,descendre_code

# read the data from the URL and print it
# #
# import urllib.request
# # open a connection to a URL using urllib
# webUrl  = urllib.request.urlopen('https://docs.python.org/3/library/urllib.request.html')
#
# #get the result code and print it
# print ("result code: " + str(webUrl.getcode()))
#
# # read the data from the URL and print it
# data = webUrl.read()
# print (data)

# from urllib.request import urlopen
#
# link = "https://numpy.org/doc/stable/user/basics.broadcasting.html"
#
# try:
#     f = urlopen(link)
#     myfile = f.read()
#     print(myfile)
# except(IOError):
#     pass

# x=myString("fred3.text").value(1)
# print(x)

# x = myChains("fred3.txt",",")
# # # l=list(x.split(","))
# # # print((l))
# print("********************************")
# # print(Descendre_Code(x))
# # print("********************************")
# # print(remonter_code(x))
# print(x.descendreCode())
# print("********************************")
# print(x.remonterCode())
# # print(descendre_code(x))

x = MyString("fred3.txt")
y=x.toString()
# x.decoupeChaine("\t",True)
print(y)
x.create_file(2)

# print(type(y))
# z=["a","b","c"]
# print(z)
# a=y+z
# print(a)
# print(type(y))
# print("Nombre d'éléments de la lsite : " + str(len(y)))

# y=x.toSet()
# print(y)
# print(type(y))
# print("Nombre d'éléments de la lsite : " + str(len(y)))

# y=x.toTuple()
# print(y)
# print(type(y))
# print("Nombre d'éléments de la lsite : " + str(len(y)))

