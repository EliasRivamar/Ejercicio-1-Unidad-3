class Carrera:
    __cod = ""
    __nom = ""
    __fecha_inicio = ""
    __duracion = ""
    __titulo = ""

    def __init__(self, cod, nom, fecha_inicio, duracion, titulo):
        self.__cod = cod
        self.__nom = nom
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo

    def getNombre(self):
        return str(self.__nom)
    
    def getCodigo(self):
        return str(self.__cod)

    def __str__(self):
        cadena = f"Codigo: {self.__cod}, Nombre: {self.__nom}, Fecha Inicio: {self.__fecha_inicio}, Duracion: {self.__duracion}, Titulo: {self.__titulo}" + "\n"
        return cadena
    