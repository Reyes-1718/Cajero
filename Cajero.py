def autenticar():
    print("\n===== AUTENTICACION =====")
    print("Bienvenido al cajero automático")

    usuario = input("Ingresa tu usuario: ")

    if usuario not in RegistroUsuarios:
        print("Credenciales incorrectas")
        return None

    if RegistroUsuarios[usuario]["bloqueado"]:
        print("Su cuenta está bloqueada")
        return None

    intentos = 0

    while intentos < 3:
        clave = input("Ingresa tu clave: ")

        if RegistroUsuarios[usuario]["clave"] == clave:
            print("\nBienvenido", usuario)
            return usuario

        intentos += 1
        print("Credenciales incorrectas")

        if intentos < 3:
            print(f"Le quedan {3 - intentos} intentos")
        else:
            RegistroUsuarios[usuario]["bloqueado"] = True
            print("Su cuenta ha sido bloqueada por exceder los intentos permitidos")

    return None
def consultar_saldo(usuario):
    saldo = RegistroUsuarios[usuario]["saldo"]
    print("\nSu saldo actual es de RD$", saldo)
def retirar(usuario):
    print("\nHa seleccionado retirar dinero")
    try:
        monto = int(input("Digite el monto a retirar: "))

        if monto <= 0:
            print("El monto ingresado no es válido")
        elif monto > RegistroUsuarios[usuario]["saldo"]:
            print("No cuenta con saldo suficiente")
        else:
            RegistroUsuarios[usuario]["saldo"] -= monto
            print(f"Retiro de RD$ {monto} realizado con éxito")

    except ValueError:
        print("El monto ingresado no es válido")
def depositar(usuario):
    print("\nHa seleccionado depositar dinero")
    try:
        monto = int(input("Digite el monto a depositar: "))

        if monto <= 0:
            print("El monto ingresado no es válido")
        else:
            RegistroUsuarios[usuario]["saldo"] += monto
            print(f"Depósito de RD$ {monto} realizado con éxito")

    except ValueError:
        print("El monto ingresado no es válido")
def transferir(usuario):
    while True:
        print("\n===== TRANSFERENCIAS =====")
        print("1. Ver cuentas disponibles")
        print("2. Transferir a terceros")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción (1-3): "))
        except ValueError:
            print("Opción inválida.")
            continue

        match opcion:
            case 1:
                print("\n===== CUENTAS DISPONIBLES =====")

                for nombre, datos in RegistroUsuarios.items():
                    if nombre != usuario:
                        print(f"Nombre: {nombre} | Cuenta: {datos['cuenta']}")

            case 2:
                print("\nHa seleccionado transferir")
                cuenta = input("Digite la cuenta a transferir: ")

                if len(cuenta) == 9 and cuenta.isdigit():

                    for destino in RegistroUsuarios:

                        if RegistroUsuarios[destino]["cuenta"] == cuenta:

                            if destino == usuario:
                                print("No puede transferirse dinero a usted mismo")
                                break

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

                            break

                    else:
                        print("La cuenta no existe")

                else:
                    print("El número de cuenta no es válido")

            case 3:
                print("\nRegresando al menú principal...")
                return

            case _:
                print("Opción inválida. Seleccione una opción válida (1-3).")

inicio = False
RegistroUsuarios = {
    "Algoritmo": {"clave": "1234", "saldo": 5000, "cuenta": "123456789", "bloqueado": False},
    "Nathalia": {"clave": "1111", "saldo": 6000, "cuenta": "987654321", "bloqueado": False},
    "Miguel": {"clave": "2222", "saldo": 7000, "cuenta": "456789123", "bloqueado": False},
    "Laura": {"clave": "3333", "saldo": 8000, "cuenta": "321654987", "bloqueado": False},
    "Jose": {"clave": "4444", "saldo": 9000, "cuenta": "789456123", "bloqueado": False}
}


while True:
    if inicio == False:
        usuario = autenticar()

        if usuario is None:
            continue

        inicio = True

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
                consultar_saldo(usuario)
            case 2:
                retirar(usuario)
            case 3:
                depositar(usuario)
            case 4:
                transferir(usuario)
            case 5:
                print("\nCerrando sesión...")
                inicio = False
                break
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción válida (1-5).")