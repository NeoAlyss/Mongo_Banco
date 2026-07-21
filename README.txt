================================================================
SISTEMA CRUD — BANCO (MongoDB + PyMongo)
================================================================

Sistema de consola en Python para gestionar clientes de un banco,
desarrollado para la Evaluación Unidad Integradora N°3 (Bases de
Datos No Estructuradas — INACAP). Caso de estudio: Banco.

----------------------------------------------------------------
DESCRIPCIÓN
----------------------------------------------------------------
El sistema administra una colección "clientes" en MongoDB, donde
cada cliente tiene datos de contacto, datos de extranjería
(opcional), etiquetas, y un array de productos bancarios (cuentas
vista, ahorro o corriente), cada uno con su propio historial de
transacciones.

----------------------------------------------------------------
REQUISITOS PREVIOS
----------------------------------------------------------------
  - Python 3.10 o superior
  - MongoDB Community Server corriendo LOCALMENTE en el puerto 27017
  - Librería PyMongo

----------------------------------------------------------------
INSTALACIÓN
----------------------------------------------------------------
1. Clona este repositorio:
   git clone https://github.com/javilass/mongo_banco.git

2. Instala las dependencias:
   pip install pymongo

3. Verifica que el servicio de MongoDB esté corriendo en tu equipo
   (localhost:27017). En Windows, revisa en "Servicios" que
   "MongoDB Server" aparezca como "En ejecución".

----------------------------------------------------------------
EJECUCIÓN
----------------------------------------------------------------
Desde la raíz del proyecto:

   python main.py

La primera vez que se ejecuta, el sistema carga automáticamente 8
clientes de ejemplo en la colección "clientes" (base de datos
"banco"), solo si esta está vacía. En ejecuciones posteriores no
se duplican los datos.

----------------------------------------------------------------
ESTRUCTURA DEL PROYECTO
----------------------------------------------------------------
  main.py         -> Menú principal y las 10 funcionalidades del sistema
  conexion.py      -> Conexión a MongoDB local
  seed_data.py      -> Datos de ejemplo (8 clientes) para precargar la colección
  README.txt        -> Este archivo

----------------------------------------------------------------
MENÚ DEL SISTEMA
----------------------------------------------------------------
1.  Crear cliente
2.  Listar todos los clientes
3.  Buscar por saldo disponible
4.  Buscar por apellido
5.  Buscar por fecha de nacimiento
6.  Buscar productos por tipo y estado
7.  Actualizar sucursal
8.  Actualizar teléfono de contacto o saldo de producto
9.  Eliminar cliente por número de cuenta
10. Reporte de cuentas por tipo y saldo total
0.  Salir

** NOTA SOBRE IDENTIFICACIÓN DE CLIENTES:
Las operaciones 7, 8 y 9 buscan al cliente por el NÚMERO DE CUENTA
de alguno de sus productos. Esto es porque el
modelo permite clientes extranjeros sin RUT (campo rut = null),
mientras que todo cliente tiene garantizado al menos un producto
con número de cuenta.

----------------------------------------------------------------
MODELO DE DATOS (colección "clientes")
----------------------------------------------------------------
- Campos raíz:
  rut, nombre, apellido, fecha_nacimiento, nacionalidad, sucursal

- Subdocumento "contacto":
  telefono, domicilio, comuna, region, email

- Subdocumento "extranjero" (opcional, null si es chileno):
  pais, dni, pasaporte

- Array "etiquetas":
  ej. ["vip", "premium"]

- Array de subdocumentos "productos":
  tipo, numero_cuenta, fecha_apertura, bloqueo, saldo_disponible,
  y un array anidado "transacciones"
  (numero_transaccion, fecha, monto, tipo_transaccion)

----------------------------------------------------------------
AUTORES
----------------------------------------------------------------
  - Andrea Diaz
  - Javiera Lasseube
