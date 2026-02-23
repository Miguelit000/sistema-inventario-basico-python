# Sistema de Gestión de Inventario Básico (CLI)

Este es un sistema de gestión de inventario basado en la Interfaz de Línea de Comandos (CLI), desarrollado completamente en Python. 

## 🎯 ¿Qué problema resuelve?

Muchos pequeños negocios y emprendedores llevan el control de su mercancía de forma manual en libretas o en hojas de cálculo desorganizadas, lo que lleva a errores de captura y pérdida de información. 

Este script soluciona ese problema proporcionando un entorno rápido, estructurado y a prueba de errores para administrar el stock. Permite a los usuarios realizar las operaciones fundamentales (CRUD) con validación de datos estricta, asegurando que el inventario esté siempre preciso y disponible.

### Características Principales:
* **Persistencia de Datos:** El inventario se guarda automáticamente en un archivo `Inventario.json`. No se pierde la información al cerrar el programa.
* **Validación de Entradas:** El sistema previene caídas y colapsos validando que el usuario ingrese el tipo de dato correcto (ej. números en lugar de letras para precios y cantidades).
* **Búsqueda Eficiente:** Permite consultar productos específicos a través de su ID sin tener que imprimir toda la base de datos.

---

## 🚀 Cómo ejecutar el proyecto

Para correr este programa, necesitas tener instalado **Python 3.x** en tu dispositivo. Puedes descargarlo gratis desde [python.org](https://www.python.org/).

### En Windows
1. Descarga o clona este repositorio en tu computadora.
2. Abre la terminal (Símbolo del sistema o PowerShell).
3. Navega hasta la carpeta donde guardaste el archivo usando el comando `cd` (ej. `cd Documentos/Inventario`).
4. Ejecuta el script con el siguiente comando:
   ```bash
   python main.py

### En macOS / Linux
1. Descarga o clona este repositorio.
2. Abre tu aplicaion de Terminal.
3. Navega hasta la carpeta del proyecto usando cd.
4. Ejecuta el script (nota que en estos sistemas suele usarse python3)
   ```bash
   python3 main.py

### En Dispositivos Moviles (Android/iOS)
Si no tienes una computadora a la mano, tambien puedes ejecutar este codigo desde tu celular o tablet:
* **Opcion web (Recomendada):** Sube el codigo a plataformas como Replit o [Github CodeSpaces] para ejecutarlo directamente desde el navegador de tu movil.
* **Android:** Descarga la aplicacion Pydroid 3 desde la Play Store. Abre la app, pega el codigo o abre el arhcivo main.py y presiona el boton amarillo de "Play"
* **iOS:** Puedes usar apliaciones como Pythonista 3 o carnets para ejecutar el codigo localmene en tu iPhone o iPad

### 🛠️ Tecnologías Utilizadas
* **Python 3:** Logica principal y control de flujo
* **JSON(Libreria estandar):** Para la serializacion y persistencia de datos
