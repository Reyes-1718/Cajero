inicio = False
RegistroUsuarios = {
    "Algoritmo": "1234",
    "Nathalia": "1111",
    "Miguel": "2222",
    "Laura": "3333",
    "José": "4444"
}

while True:
    if inicio == False:
        print("\n===== AUTENTICACION =====")
        print("Bienvenido al cajero automático")
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu clave: ")

        if usuario in RegistroUsuarios and RegistroUsuarios[usuario] == clave:
            print("Bienvenido", usuario)
            inicio = True
        else:
            print("Credenciales incorrectas")
            continue
            
    while True:
        print("\n===== Cajero Automático =====")
        print("Opciones disponibles:")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Transferir a terceros")
        print("5. Cerrar sesión")
        saldo = 5000
        opcion = int(input("Ingresa una opción (1-5): "))
        match opcion:
            case 1:
                print("\nSu saldo actual es de RD$", saldo)
            case 2:
                print("\nHa seleccionado retirar dinero")
            case 3:
                print("\nHa seleccionado retirar Depositar dinero")
            case 4:
                print("\nHa seleccionado transferir a terceros")
            case 5:
                print("\nCerrando sesión...")
                print("Saliendo del sistema...")
                exit()
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción válida (1-5).")