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
            case 2:
            case 3:
            case 4:
            case 5:
            case _: