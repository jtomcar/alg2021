#Escribe un programa que:
#  * Cree un diccionario con el nombre de tres amigos y asocie a cada uno su edad.
#  * Pida el nombre de un amigo y escriba su edad. Si el nombre no está en el diccionario que escriba: 'No sé su edad'.

diccionario = {'Antonio':24,'Jesus':30,'Pepe':27}

a = input("Dime el nombre de tu amigo para saber su edad: ")
if a in diccionario:
    print(diccionario[a])
else:
    print("No sé su edad")