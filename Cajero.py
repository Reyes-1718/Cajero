inicio = False
RegistroUsuarios = {
    "Algoritmo": {"clave": "1234", "saldo":5000},
    "Nathalia": {"clave": "1111", "saldo":6000},
    "Miguel": {"clave": "2222", "saldo":7000},
    "Laura": {"clave": "3333", "saldo":8000},
    "Jose": {"clave": "4444", "saldo":9000}
}


while True:
    if inicio == False:
        print("\n===== AUTENTICACION =====")
        print("Bienvenido al cajero automático")
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu clave: ")

        if usuario in RegistroUsuarios and RegistroUsuarios[usuario]["clave"] == clave:
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

        try:
            opcion = int(input("Ingresa una opción (1-5): "))
        except ValueError:
            print("\nOpción inválida. Por favor, seleccione una opción válida (1-5).")
            continue
        match opcion:
            case 1:
                saldo = RegistroUsuarios[usuario]["saldo"]
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