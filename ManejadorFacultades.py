from Facultad import Facultad
from Carrera import Carrera
import csv

class ManejadorFacultad:
    def __init__(self):
        self.__lista = []

    def agregarComponente(self, unaFacultad):
        self.__lista.append(unaFacultad)
    
    def test(self):
        archivo = open("facultad.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            if "Facultad" in fila[1]:
                print("Se esta cargando una Facultad")
                codigo = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telefono = fila[4]
                carrera = None
                unaFacultad = Facultad(codigo, nombre, direccion, localidad, telefono, carrera)
                self.agregarComponente(unaFacultad)
            else:
                cod = fila[1]
                nom = fila[2]
                fecha_inicio = fila[3]
                duracion = fila[4]
                titulo = fila[5]
                carrera = (cod, nom, fecha_inicio, duracion, titulo)
                unaFacultad = Facultad(codigo, nombre, direccion, localidad, telefono, carrera)
                self.agregarComponente(unaFacultad)
                print("Se esta cargando una carrera")
        archivo.close()

    def leerCarreras(self, indice):
        while indice < len(self.__lista):
            if str(Facultad.getCarrera(self.__lista[indice])) != "None":
                print(str(Facultad.getCarrera(self.__lista[indice])))
            else:
                return
            indice += 1

    def punto1(self, codigo):
        indice = 0
        while indice < len(self.__lista):
            if str(Facultad.getCodigo(self.__lista[indice]))== codigo:
                print("Se encontro")
                self.leerCarreras(indice+1)
                return
            indice += 1

    def punto2(self, nombre):
        indice = 0
        while indice < len(self.__lista):
            if str(nombre) in str(Facultad.getCarrera(self.__lista[indice])):
                print("Se encontro")
                print(f"Codigo Facultad: {Facultad.getCodigo(self.__lista[indice])}, Nombre: {Facultad.getNombre(self.__lista[indice])} , Direccion: {Facultad.getDireccion(self.__lista[indice])}")
            indice += 1

        
    def __str__(self):
        cadena = ""
        indice = 0
        while indice < len(self.__lista):
            if str(Facultad.getCarrera(self.__lista[indice])) == "None":
                cadena += str(Facultad.getFacultad(self.__lista[indice]))+"\n"
            else:
                cadena += str(Facultad.getCarrera(self.__lista[indice]))+"\n"
            indice += 1
        return cadena
