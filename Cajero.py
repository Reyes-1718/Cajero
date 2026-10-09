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
        print("===== AUTENTICACION =====")
        print("Bienvenido al cajero automático")
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu clave: ")

        if usuario in RegistroUsuarios and RegistroUsuarios[usuario] == clave:
            print("Bienvenido", usuario)
            inicio = True
        else:
            print("Credenciales incorrectas")
            continue