lista=[]
while True:
    a=int(input('Dame un numero: '))
    if a<0:
        break
    lista.append(a)

lista.sort()
print(lista)
