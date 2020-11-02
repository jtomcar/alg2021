class Estudiante:
    def __init__(self, nombre : str):
        self.nombre = nombre
        self.asignaturas = {}

    def califica(self, nombre: str, nota: int):
        self.asignaturas[nombre] = nota

    def nota(self, nombre : str):
        return self.asignaturas[nombre]

    def media(self):
        suma=0
        i=0
        for asignatura, calificacion in self.asignaturas.items():
            suma=suma+calificacion
            i+=1
        return (suma/i)

    def muestra_expediente(self):
        for asignatura, calificacion in self.asignaturas.items():
            print(asignatura, ":", calificacion)



e = Estudiante("Juan Gomez Martinez")
e.califica('EI1022', 8)
e.califica('EI1035', 7)
print(e.nota('EI1022'))
print(e.media())
e.muestra_expediente()
