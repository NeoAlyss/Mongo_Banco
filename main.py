from datetime import datetime
from pprint import pprint

from conexion import conectar
from seed_data import cargar_datos_iniciales


# ---------- Funciones auxiliares ----------

def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje + " (dd-mm-aaaa): ").strip()
        try:
            return datetime.strptime(texto, "%d-%m-%Y")
        except ValueError:
            print("Formato inválido, intenta de nuevo (ej: 15-03-1994).")


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje + ": ").strip())
        except ValueError:
            print("Debes ingresar un número válido.")


def pedir_bool(mensaje):
    return input(mensaje + " (s/n): ").strip().lower() == "s"


# ---------- Creación de un nuevo documento (cliente) ----------

def crear_cliente(coleccion):
    print("\n--- Crear nuevo cliente ---")
    rut = input("RUT (o vacío si es extranjero sin RUT): ").strip() or None
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    fecha_nacimiento = pedir_fecha("Fecha de nacimiento")

    extranjero = None
    if pedir_bool("¿Es extranjero?"):
        print("-- Datos de extranjero (subdocumento) --")
        nacionalidad = input("Nacionalidad: ").strip()
        extranjero = {
            "pais": input("País de origen: ").strip(),
            "dni": input("DNI: ").strip(),
            "pasaporte": input("Pasaporte: ").strip(),
        }
    else:
        nacionalidad = "Chileno"

    sucursal = input("Sucursal: ").strip()

    print("-- Datos de contacto --")
    contacto = {
        "telefono": input("Teléfono: ").strip(),
        "domicilio": input("Domicilio: ").strip(),
        "comuna": input("Comuna: ").strip(),
        "region": input("Región: ").strip(),
        "email": input("Email: ").strip(),
    }

    etiquetas = [e.strip() for e in input("Etiquetas separadas por coma: ").split(",") if e.strip()]

    productos = []
    print("-- Productos --")
    while True:
        tipo = input("Tipo de producto (vista/ahorro/corriente): ").strip().lower()
        producto = {
            "tipo": tipo,
            "numero_cuenta": input("Número de cuenta: ").strip(),
            "fecha_apertura": pedir_fecha("Fecha de apertura"),
            "bloqueo": pedir_bool("¿Cuenta bloqueada?"),
            "saldo_disponible": pedir_float("Saldo disponible"),
            "linea_credito": pedir_float("Línea de crédito") if tipo == "corriente" else None,
            "transacciones": [],
        }
        if pedir_bool("¿Agregar una transacción inicial?"):
            producto["transacciones"].append({
                "numero_transaccion": 1,
                "fecha": pedir_fecha("Fecha de la transacción"),
                "monto": pedir_float("Monto"),
                "tipo_transaccion": input("Tipo de transacción (cargo/abono/reversa): ").strip(),
            })
        productos.append(producto)
        if not pedir_bool("¿Agregar otro producto?"):
            break

    documento = {
        "rut": rut,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "nacionalidad": nacionalidad,
        "sucursal": sucursal,
        "contacto": contacto,
        "extranjero": extranjero,
        "etiquetas": etiquetas,
        "productos": productos,
    }

    resultado = coleccion.insert_one(documento)
    print(f"Cliente creado con _id: {resultado.inserted_id}")


# ---------- Listar todos los clientes ----------

def listar_clientes(coleccion):
    print("\n--- Listado de clientes ---")
    proyeccion = {
        "nombre": 1,
        "apellido": 1,
        "rut": 1,
        "sucursal": 1,
        "productos.tipo": 1,
        "productos.numero_cuenta": 1,
        "productos.saldo_disponible": 1,
    }
    cursor = coleccion.find({}, proyeccion)
    for doc in cursor:
        print(f"{doc['_id']} | {doc.get('nombre')} {doc.get('apellido')} | "
              f"RUT: {doc.get('rut')} | Sucursal: {doc.get('sucursal')}")

        productos = doc.get("productos", [])
        if productos:
            for producto in productos:
                print(f"      · {producto.get('tipo', '-'):<10} "
                      f"cuenta {producto.get('numero_cuenta', '-'):<12} "
                      f"saldo ${producto.get('saldo_disponible', 0):,.0f}")
        else:
            print("      (sin productos)")
        print()


# ---------- Operador de comparación ----------

def buscar_por_comparacion(coleccion):
    print("\n--- Búsqueda por saldo disponible ---")
    print("Puedes usar un solo operador, o dos para definir un rango (ej: > 0 y < 1000).")

    operador1 = input("Primer operador ($gt, $lt, $gte, $lte, $ne): ").strip()
    valor1 = pedir_float("Valor de referencia")
    condiciones = {operador1: valor1}

    if pedir_bool("¿Agregar un segundo operador para acotar el rango?"):
        operador2 = input("Segundo operador ($gt, $lt, $gte, $lte, $ne): ").strip()
        valor2 = pedir_float("Segundo valor de referencia")
        condiciones[operador2] = valor2

    filtro = {"productos.saldo_disponible": condiciones}
    resultados = coleccion.find(filtro, {"nombre": 1, "apellido": 1, "productos.saldo_disponible": 1})
    for doc in resultados:
        pprint(doc)


# ---------- Operación con regex ----------

def buscar_por_regex(coleccion):
    print("\n--- Búsqueda por apellido ---")
    texto = input("Texto a buscar en el apellido: ").strip()
    filtro = {"apellido": {"$regex": texto, "$options": "i"}}
    for doc in coleccion.find(filtro):
        print(f"{doc['nombre']} {doc['apellido']} ({doc.get('rut')})")


# ---------- Operación con rango de fechas ----------

def buscar_por_rango_fechas(coleccion):
    print("\n--- Búsqueda de clientes por fecha de nacimiento ---")
    desde = pedir_fecha("Desde")
    hasta = pedir_fecha("Hasta")
    filtro = {"fecha_nacimiento": {"$gte": desde, "$lte": hasta}}
    for doc in coleccion.find(filtro):
        print(f"{doc['nombre']} {doc['apellido']} - nacimiento: {doc['fecha_nacimiento'].strftime('%d-%m-%Y')}")


# ---------- Búsqueda dentro de subdocumento/array ----------

def buscar_en_subdocumento_array(coleccion):
    print("\n--- Búsqueda de productos por tipo y estado ---")
    tipo = input("Tipo de producto (vista/ahorro/corriente): ").strip().lower()
    bloqueado = pedir_bool("¿Desea ver solo productos bloqueados?")
    filtro = {"productos": {"$elemMatch": {"tipo": tipo, "bloqueo": bloqueado}}}
    for doc in coleccion.find(filtro):
        print(f"{doc['nombre']} {doc['apellido']} - tiene producto {tipo} (bloqueo={bloqueado})")


# ---------- Actualización de campo raíz ----------

def actualizar_campo_raiz(coleccion):
    print("\n--- Actualización de sucursal de un cliente ---")
    numero_cuenta = input("Número de cuenta de alguno de sus productos: ").strip()
    filtro = {"productos.numero_cuenta": numero_cuenta}
    antes = coleccion.find_one(filtro)
    if not antes:
        print("No se encontró ningún cliente con esa cuenta.")
        return
    print("Antes:")
    pprint(antes)
    nueva_sucursal = input("Nueva sucursal: ").strip()
    coleccion.update_one(filtro, {"$set": {"sucursal": nueva_sucursal}})
    despues = coleccion.find_one(filtro)
    print("Después:")
    pprint(despues)


# ---------- Actualización de subdocumento o array ----------

def actualizar_subdocumento_array(coleccion):
    print("\n--- Actualización de teléfono de contacto o saldo de producto ---")
    numero_cuenta = input("Número de cuenta del cliente: ").strip()
    filtro_cliente = {"productos.numero_cuenta": numero_cuenta}
    opcion = input("¿Actualizar (1) teléfono de contacto o (2) saldo de esta cuenta?: ").strip()

    if opcion == "1":
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        resultado = coleccion.update_one(filtro_cliente, {"$set": {"contacto.telefono": nuevo_telefono}})
    else:
        nuevo_saldo = pedir_float("Nuevo saldo disponible")
        resultado = coleccion.update_one(
            filtro_cliente,
            {"$set": {"productos.$.saldo_disponible": nuevo_saldo}},
        )

    if resultado.matched_count == 0:
        print("No se encontró ningún cliente con esa cuenta.")
        return

    despues = coleccion.find_one(filtro_cliente)
    print("Documento actualizado:")
    pprint(despues)


# ---------- Eliminación  ----------

def eliminar_documento(coleccion):
    print("\n--- Eliminación de cliente por número de cuenta ---")
    numero_cuenta = input("Número de cuenta de alguno de sus productos: ").strip()
    filtro = {"productos.numero_cuenta": numero_cuenta}
    doc = coleccion.find_one(filtro)
    if not doc:
        print("No se encontró ningún cliente con esa cuenta.")
        return
    print("Documento a eliminar:")
    pprint(doc)
    if pedir_bool("¿Confirmar eliminación?"):
        resultado = coleccion.delete_one(filtro)
        print(f"Documentos eliminados: {resultado.deleted_count}")
    else:
        print("Operación cancelada.")


# ---------- Pipeline de agregación ----------

def reporte_agregacion(coleccion):
    print("\n--- Reporte de cuentas por tipo y saldo total ---")
    pipeline = [
        {"$unwind": "$productos"},
        {"$group": {
            "_id": "$productos.tipo",
            "saldo_total": {"$sum": "$productos.saldo_disponible"},
            "cantidad_cuentas": {"$sum": 1},
        }},
        {"$sort": {"saldo_total": -1}},
    ]
    for fila in coleccion.aggregate(pipeline):
        print(f"Tipo: {fila['_id']:<10} | Cuentas: {fila['cantidad_cuentas']:<3} | "
              f"Saldo total: ${fila['saldo_total']:,.0f}")


# ---------- Menú principal ----------

def mostrar_menu():
    print("\n === .✦ ݁˖ Banco Tío Rico McPato .✦ ݁˖ ===")
    print("1.  Crear cliente")
    print("2.  Listar todos los clientes")
    print("3.  Buscar por saldo disponible")
    print("4.  Buscar por apellido")
    print("5.  Buscar por fecha de nacimiento")
    print("6.  Buscar productos por tipo y estado")
    print("7.  Actualizar sucursal")
    print("8.  Actualizar teléfono de contacto o saldo de producto")
    print("9.  Eliminar cliente por número de cuenta")
    print("10. Reporte de cuentas por tipo y saldo total")
    print("0.  Salir")


def main():
    coleccion = conectar()
    cargar_datos_iniciales(coleccion)

    acciones = {
        "1": crear_cliente,
        "2": listar_clientes,
        "3": buscar_por_comparacion,
        "4": buscar_por_regex,
        "5": buscar_por_rango_fechas,
        "6": buscar_en_subdocumento_array,
        "7": actualizar_campo_raiz,
        "8": actualizar_subdocumento_array,
        "9": eliminar_documento,
        "10": reporte_agregacion,
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "0":
            print("Adiós!")
            break
        funcion = acciones.get(opcion)
        if funcion:
            try:
                funcion(coleccion)
            except Exception as error:
                print(f"Ocurrió un error ejecutando la operación: {error}")
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()