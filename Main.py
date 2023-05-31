from ManejadorFacultades import ManejadorFacultad

if __name__=="__main__":
    MF = ManejadorFacultad()
    MF.test()
    print(str(MF))
    while 1  != 0:
        print("1: Dado un codigo de una facultad y se le mostrara informacion")
        print("2: Dado un nombre de una carrera, mostrar informacion")
        print("3: Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            codigo = input("Ingrese el codigo de una facultad: ")
            MF.punto1(codigo)
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la carrera: ")
            MF.punto2(nombre)
        elif opcion == 3:
            exit()
        else:
            print("....Opcion Incorrecta....")

    