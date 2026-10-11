def transferir(usuario):
    print("Ha seleccionado transferir")
    cuenta = input("Digite la cuenta a transferir: ")

    if len(cuenta) == 9 and cuenta.isdigit():

        for destino in RegistroUsuarios:

            if RegistroUsuarios[destino]["cuenta"] == cuenta:

                if destino == usuario:
                    print("No puede transferirse dinero a usted mismo")
                    return

                try:
                    monto = int(input("Digite el monto a transferir: "))

                    if monto <= 0:
                        print("El monto ingresado no es válido")

                    elif monto > RegistroUsuarios[usuario]["saldo"]:
                        print("No cuenta con saldo suficiente")

                    else:
                        RegistroUsuarios[usuario]["saldo"] -= monto
                        RegistroUsuarios[destino]["saldo"] += monto

                        print(f"Transferencia de RD$ {monto} realizada a {destino}")

                except ValueError:
                    print("El monto ingresado no es válido")

                return

        print("La cuenta no existe")

    else:
        print("El número de cuenta no es válido")

inicio = False
RegistroUsuarios = {
    "Algoritmo": {"clave": "1234", "saldo":5000, "cuenta": "123456789"},
    "Nathalia": {"clave": "1111", "saldo":6000, "cuenta": "987654321"},
    "Miguel": {"clave": "2222", "saldo":7000, "cuenta": "456789123"},
    "Laura": {"clave": "3333", "saldo":8000, "cuenta": "321654987"},
    "Jose": {"clave": "4444", "saldo":9000, "cuenta": "789456123"}
}


while True:
    if inicio == False:
        print("\n===== AUTENTICACION =====")
        print("Bienvenido al cajero automático")
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu clave: ")

        if usuario in RegistroUsuarios and RegistroUsuarios[usuario]["clave"] == clave:
            print("\nBienvenido", usuario)
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
                transferir(usuario)
            case 5:
                print("\nCerrando sesión...")
                print("Saliendo del sistema...")
                inicio = False
                break
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción válida (1-5).")