# Cajero automático en Python

## Descripción del proyecto

Este proyecto es un simulador de cajero automático hecho en **Python**, un lenguaje de programación.

Para entrar, la persona escribe su nombre de usuario y su contraseña. Después puede consultar su saldo, retirar dinero, depositar dinero y transferir fondos a otras cuentas registradas.

El objetivo es practicar lo básico de la programación: funciones, diccionarios, condiciones, ciclos, validación de datos y manejo de errores.

## Qué puede hacer

### 1. Iniciar sesión
- Pide el usuario y la contraseña.
- Comprueba que el usuario exista.
- Comprueba que la cuenta no esté bloqueada.
- Permite hasta tres intentos fallidos cada vez que se usa la función de autenticación.
- Bloquea la cuenta si se superan los tres intentos.
- Si los datos son correctos, muestra el menú principal.
- Permite escribir `salir` en lugar del usuario para cerrar el programa.

### 2. Consultar el saldo
- Muestra el dinero disponible en la cuenta del usuario.
- El saldo aparece en pesos dominicanos (RD$).

### 3. Retirar dinero
- Pide el monto que se quiere retirar.
- Comprueba que el monto sea mayor que cero.
- Comprueba que haya saldo suficiente.
- Resta el monto del saldo.
- Muestra un mensaje cuando el retiro se hace bien.

### 4. Depositar dinero
- Pide el monto que se quiere depositar.
- Comprueba que sea un número entero positivo.
- Suma el monto al saldo.
- Confirma el depósito.

### 5. Transferir dinero
- Muestra las cuentas disponibles para transferir.
- Pide el número de cuenta de la persona que recibirá el dinero.
- Comprueba que el número tenga exactamente nueve dígitos.
- Comprueba que la cuenta de destino exista.
- No permite transferir a la propia cuenta.
- Comprueba que haya fondos suficientes.
- Resta el monto de la cuenta de origen y lo suma a la cuenta de destino.

### 6. Cerrar sesión
- Cierra la sesión actual.
- Vuelve a la pantalla de inicio para que otra persona pueda entrar.

### 7. Salir del programa
- En la pantalla de inicio, escribe `salir` (da igual si usas mayúsculas o minúsculas).
- También puedes presionar `Ctrl+C` en cualquier momento: el programa se cierra con un mensaje de despedida, sin mostrar errores.

## Herramientas usadas

- **Lenguaje:** Python 3.10 o superior.
- **Pantalla:** consola o terminal.
- **Dónde se guardan los datos:** en diccionarios de Python, dentro de la memoria del programa. Un diccionario es una lista de datos con nombre.
- **Librerías externas:** no necesita ninguna.

## Cómo instalar y ejecutar

### Paso 1. Instalar Python

Descarga e instala Python desde su página oficial:

https://www.python.org/downloads/

### Paso 2. Descargar el código

El código está en el archivo:

`Cajero.py`

El nombre empieza con **C mayúscula**. En Linux y macOS las mayúsculas importan al escribir el nombre del archivo.

### Paso 3. Ejecutar el programa

Abre una terminal en la carpeta donde está el archivo y escribe:

```bash
python Cajero.py
```

En algunos sistemas debes escribir:

```bash
python3 Cajero.py
```

## Usuarios de prueba

El sistema ya trae cinco usuarios registrados.

| Usuario | Contraseña | Saldo inicial | Número de cuenta |
|---|---|---|---|
| Algoritmo | 1234 | RD$ 5,000 | 123456789 |
| Nathalia | 1111 | RD$ 6,000 | 987654321 |
| Miguel | 2222 | RD$ 7,000 | 456789123 |
| Laura | 3333 | RD$ 8,000 | 321654987 |
| Jose | 4444 | RD$ 9,000 | 789456123 |

**Nota:** Estas credenciales son solo para estudio y pruebas.

## Menú principal

Al iniciar sesión, la persona verá esto:

```text
===== Cajero Automático =====
Opciones disponibles:

1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Transferir a terceros
5. Cerrar sesión

Ingresa una opción (1-5):
```

### Menú de transferencias

```text
===== TRANSFERENCIAS =====

1. Ver cuentas disponibles
2. Transferir a terceros
3. Volver al menú principal

Seleccione una opción (1-3):
```

## Cómo está organizado el código

El programa se divide en estas funciones. Una función es un bloque de código que hace una tarea concreta.

| Función | Qué hace |
|---|---|
| `autenticar()` | Revisa los datos de acceso y controla la entrada. |
| `consultar_saldo(usuario)` | Muestra el saldo del usuario que inició sesión. |
| `retirar(usuario)` | Hace retiros y revisa que haya fondos. |
| `depositar(usuario)` | Hace depósitos. |
| `transferir(usuario)` | Maneja las transferencias entre cuentas. |
| `main()` | Controla el inicio de sesión, el menú principal y la salida del programa. |

El programa solo arranca cuando se ejecuta directamente (`python Cajero.py`), gracias a la línea `if __name__ == "__main__":`. Así, el archivo se puede importar desde otro archivo, por ejemplo para hacer pruebas, sin que se abra el cajero.

Además, el programa usa un diccionario llamado `RegistroUsuarios`, donde guarda los datos de las cuentas.

### Cómo es el diccionario

```python
RegistroUsuarios = {
    "Algoritmo": {
        "clave": "1234",
        "saldo": 5000,
        "cuenta": "123456789",
        "bloqueado": False
    }
}
```

Cada usuario tiene cuatro datos:

- `clave`: la contraseña para entrar.
- `saldo`: el dinero disponible en la cuenta.
- `cuenta`: el número de cuenta.
- `bloqueado`: indica si la cuenta tiene el acceso bloqueado.

### Diagrama de flujo

El recorrido completo del programa, desde el inicio de sesión hasta la salida, está en el diagrama [`cajero_automatico.mmd`](cajero_automatico.mmd). Haz clic en el nombre para abrirlo.

El archivo está escrito en **Mermaid**, un formato que convierte texto en diagramas. Si al abrirlo solo ves texto, copia su contenido y pégalo en [mermaid.live](https://mermaid.live) para ver el dibujo.

## Controles de errores

El sistema revisa los datos para evitar operaciones incorrectas.

| Situación | Qué pasa |
|---|---|
| El usuario no existe | Muestra que las credenciales son incorrectas. |
| La contraseña es incorrecta | Suma un intento fallido. |
| Tres contraseñas incorrectas | Bloquea la cuenta. |
| La cuenta está bloqueada | No deja iniciar sesión. |
| El monto es cero o menor | Rechaza la operación. |
| El monto no es un número | Muestra un mensaje de error. |
| El saldo no alcanza | No permite el retiro ni la transferencia. |
| La cuenta de destino no existe | Cancela la transferencia. |
| El número de cuenta no es válido | Pide una cuenta válida. |
| Transferencia a la propia cuenta | No la permite. |
| Opción de menú incorrecta | Muestra un mensaje de opción inválida. |
| Se presiona `Ctrl+C` o se corta la entrada | Cierra el programa con un mensaje de despedida, sin errores. |

## Ejemplos de uso

### Iniciar sesión

```text
===== AUTENTICACION =====
Bienvenido al cajero automático

Ingresa tu usuario (o escribe 'salir' para terminar): Algoritmo
Ingresa tu clave: 1234

Bienvenido Algoritmo
```

### Salir del programa

```text
===== AUTENTICACION =====
Bienvenido al cajero automático
Ingresa tu usuario (o escribe 'salir' para terminar): salir

Gracias por usar el cajero automático. ¡Hasta luego!
```

### Consultar el saldo

```text
===== Cajero Automático =====

1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Transferir a terceros
5. Cerrar sesión

Ingresa una opción (1-5): 1

Su saldo actual es de RD$ 5000
```

### Hacer un retiro

```text
Ingresa una opción (1-5): 2

Ha seleccionado retirar dinero
Digite el monto a retirar: 1000

Retiro de RD$ 1000 realizado con éxito
```

### Hacer una transferencia

```text
===== TRANSFERENCIAS =====

1. Ver cuentas disponibles
2. Transferir a terceros
3. Volver al menú principal

Seleccione una opción (1-3): 2

Ha seleccionado transferir
Digite la cuenta a transferir: 987654321
Digite el monto a transferir: 500

Transferencia de RD$ 500 realizada a Nathalia
```

## Limitaciones

El programa es una simulación para aprender, y tiene algunas limitaciones:

1. **Los datos no se guardan:** los cambios de saldo y los bloqueos duran solo mientras el programa está abierto.
2. **Contraseñas sin protección:** las claves están escritas tal cual en el diccionario y se ven en pantalla al escribirlas con `input()`.
3. **Sin historial:** no se guardan los movimientos de los usuarios.
4. **Control de intentos:** los intentos fallidos vuelven a cero cada vez que se llama otra vez a la función de autenticación.
5. **Solo números enteros:** las operaciones no aceptan centavos.
6. **Sin base de datos:** los usuarios y las cuentas están escritos directamente en el código.

## Mejoras posibles

- Guardar los datos de forma permanente con JSON o SQLite.
- Agregar un historial de movimientos.
- Mejorar el control de intentos fallidos.
- Ocultar la contraseña al escribirla.
- Permitir crear cuentas nuevas.
- Permitir cambiar la contraseña.
- Crear una interfaz con ventanas y botones.
- Guardar la fecha y la hora de cada operación.

## Objetivo de aprendizaje

Con este proyecto se practican estos temas de programación:

- Crear y usar funciones.
- Trabajar con diccionarios.
- Usar condiciones con `if`, `elif` y `else`.
- Elegir opciones con `match-case`.
- Usar ciclos `while` y `for`, que repiten instrucciones.
- Manejar errores con `try-except`.
- Revisar lo que escribe el usuario.
- Hacer operaciones con números.
- Controlar el flujo del programa y las sesiones.

## Conclusión

El simulador de cajero automático en Python muestra las operaciones bancarias básicas en una aplicación de consola.

Para hacerlo se usan estructuras de datos, código dividido en partes y validaciones que controlan lo que hacen los usuarios.

Es una simulación y no un sistema bancario real. Aun así, sirve como base que se puede ampliar con almacenamiento permanente, mejor seguridad y más funciones.

---

**Proyecto:** Simulador de cajero automático

**Lenguaje de programación:** Python

**Tipo de aplicación:** Aplicación de consola

**Finalidad:** Educativa y académica
