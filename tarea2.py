telefonos = {
    "Pepe": 659331013,
    "Pepe Martín": 633743551,
    "Juan": 123321313
}
consultando = True

while consultando:
    print()
    print("Mis telefonos")
    print("-------------")
    print("1. Consultar")
    print("2. Añadir")
    print("3. Salir")  # Added option to exit
    print("--------------")
    opcion = ""
    while opcion not in ("1", "2", "3"):  # Updated input validation
        opcion = input("->")

    if opcion == "1":
        nombre = input("Nombre: ")
        matches = [n for n in telefonos if nombre.lower() in n.lower()]
        if len(matches) == 0:
            print("No se encontraron resultados para el nombre ingresado.")
        else:
            for match in matches:
                tel = telefonos[match]
                print(match, ":", tel)

    elif opcion == "2":  # Added indentation
        nombre = input("Nombre: ")
        if nombre in telefonos:
            print("Ese nombre ya está en la agenda")
        else:
            tel = int(input("Teléfono: "))  # Added a missing colon
            telefonos[nombre] = tel
            print("El teléfono se ha añadido correctamente")

    elif opcion == "3":  # Added option to exit
        consultando = False
