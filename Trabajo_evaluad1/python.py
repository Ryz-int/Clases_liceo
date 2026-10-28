while True:
    print("Actividades escolares")
    print("1) Registrar estudiante")
    print("2) calificacion")
    print("3) Calcular costo de materiales")
    print("4) Salir")
    
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        print("Bienvenido", nombre)
        
    elif opcion == 2:
        calificacion = float(input("Ingrese la nota: "))
        if calificacion >= 4.0:
            print("Aprueba")
        else:
            print("No aprueba")
            
    elif opcion == 3:
        material = input("Ingrese el nombre del material: ")
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        total = precio * cantidad
        print("El total a pagar por", material, "es: $", total)
        
    elif opcion == 4:
        print("Programa finalizado")
        break
        
    else:
        print("opcion no valida")


