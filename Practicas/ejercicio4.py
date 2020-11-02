#¿Que escribe este programa?

def myfunction(a, b):
    a += 1
    b.append(0)

x = 1
y = [2, 1]
myfunction(x, y)
print(x, y)

#Lo que pasa es que la lista si se modifica, mientras el entero no, apunta al mismo sitio