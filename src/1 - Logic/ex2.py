#considerando que a string vai ser dada pelo usuario!

str_ = input('digite a palavra a ser invertida: ')

nvlista = [] 

b = -1
a = True

while a == True:
    nvlista.append(str_[b])
    b -= 1
    if len(nvlista) == len(str_):
        a = False

print(nvlista)