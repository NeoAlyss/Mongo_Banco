from datetime import datetime


CLIENTES_DUMMY = [
    {
        "rut": "18.234.567-8",
        "nombre": "Camila",
        "apellido": "Torres",
        "fecha_nacimiento": datetime(1994, 3, 12),
        "nacionalidad": "Chilena",
        "sucursal": "Puente Alto",
        "contacto": {
            "telefono": "+56912345678",
            "domicilio": "Av. Concha y Toro 1234",
            "comuna": "Puente Alto",
            "region": "Metropolitana",
            "email": "camila.torres@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["vip", "premium"],
        "productos": [
            {
                "tipo": "vista",
                "numero_cuenta": "V-000123",
                "fecha_apertura": datetime(2020, 6, 1),
                "bloqueo": False,
                "saldo_disponible": 150000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 6, 1), "monto": 50000.0, "tipo_transaccion": "abono"},
                    {"numero_transaccion": 2, "fecha": datetime(2026, 6, 15), "monto": 20000.0, "tipo_transaccion": "cargo"},
                ],
            },
            {
                "tipo": "corriente",
                "numero_cuenta": "C-000456",
                "fecha_apertura": datetime(2022, 1, 10),
                "bloqueo": False,
                "saldo_disponible": -30000.0,
                "linea_credito": 200000.0,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 7, 2), "monto": 80000.0, "tipo_transaccion": "cargo"},
                ],
            },
        ],
    },
    {
        "rut": "12.456.789-0",
        "nombre": "Matías",
        "apellido": "Rojas",
        "fecha_nacimiento": datetime(1988, 11, 5),
        "nacionalidad": "Chilena",
        "sucursal": "Providencia",
        "contacto": {
            "telefono": "+56987654321",
            "domicilio": "Los Leones 456",
            "comuna": "Providencia",
            "region": "Metropolitana",
            "email": "matias.rojas@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["normalito"],
        "productos": [
            {
                "tipo": "ahorro",
                "numero_cuenta": "A-000789",
                "fecha_apertura": datetime(2019, 3, 20),
                "bloqueo": False,
                "saldo_disponible": 850000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 5, 10), "monto": 100000.0, "tipo_transaccion": "abono"},
                ],
            },
        ],
    },
    {
        "rut": None,
        "nombre": "John",
        "apellido": "Smith",
        "fecha_nacimiento": datetime(1979, 7, 22),
        "nacionalidad": "Estadounidense",
        "sucursal": "Las Condes",
        "contacto": {
            "telefono": "+56911223344",
            "domicilio": "Isidora Goyenechea 3000",
            "comuna": "Las Condes",
            "region": "Metropolitana",
            "email": "john.smith@mail.com",
        },
        "extranjero": {"pais": "Estados Unidos", "dni": "N/A", "pasaporte": "US4488221"},
        "etiquetas": ["premium", "supervip"],
        "productos": [
            {
                "tipo": "corriente",
                "numero_cuenta": "C-000901",
                "fecha_apertura": datetime(2021, 9, 14),
                "bloqueo": False,
                "saldo_disponible": 2300000.0,
                "linea_credito": 500000.0,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 6, 20), "monto": 300000.0, "tipo_transaccion": "abono"},
                    {"numero_transaccion": 2, "fecha": datetime(2026, 6, 25), "monto": 150000.0, "tipo_transaccion": "cargo"},
                ],
            },
            {
                "tipo": "vista",
                "numero_cuenta": "V-000902",
                "fecha_apertura": datetime(2021, 9, 14),
                "bloqueo": False,
                "saldo_disponible": 40000.0,
                "linea_credito": None,
                "transacciones": [],
            },
        ],
    },
    {
        "rut": "9.876.543-2",
        "nombre": "Francisca",
        "apellido": "Muñoz",
        "fecha_nacimiento": datetime(2001, 1, 30),
        "nacionalidad": "Chilena",
        "sucursal": "Puente Alto",
        "contacto": {
            "telefono": "+56922334455",
            "domicilio": "Camino El Alto 890",
            "comuna": "La Florida",
            "region": "Metropolitana",
            "email": "francisca.munoz@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["vip"],
        "productos": [
            {
                "tipo": "ahorro",
                "numero_cuenta": "A-001102",
                "fecha_apertura": datetime(2023, 4, 2),
                "bloqueo": True,
                "saldo_disponible": 12000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 4, 18), "monto": 12000.0, "tipo_transaccion": "abono"},
                ],
            },
        ],
    },
    {
        "rut": "15.111.222-3",
        "nombre": "Pedro",
        "apellido": "Contreras",
        "fecha_nacimiento": datetime(1995, 9, 9),
        "nacionalidad": "Chilena",
        "sucursal": "Providencia",
        "contacto": {
            "telefono": "+56933445566",
            "domicilio": "Suecia 220",
            "comuna": "Providencia",
            "region": "Metropolitana",
            "email": "pedro.contreras@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["normalito"],
        "productos": [
            {
                "tipo": "corriente",
                "numero_cuenta": "C-001203",
                "fecha_apertura": datetime(2024, 2, 11),
                "bloqueo": False,
                "saldo_disponible": -85000.0,
                "linea_credito": 100000.0,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 7, 1), "monto": 85000.0, "tipo_transaccion": "cargo"},
                ],
            },
        ],
    },
    {
        "rut": None,
        "nombre": "Maria",
        "apellido": "Gonzalez",
        "fecha_nacimiento": datetime(1985, 12, 3),
        "nacionalidad": "Argentina",
        "sucursal": "Las Condes",
        "contacto": {
            "telefono": "+56944556677",
            "domicilio": "Apoquindo 4500",
            "comuna": "Las Condes",
            "region": "Metropolitana",
            "email": "maria.gonzalez@mail.com",
        },
        "extranjero": {"pais": "Argentina", "dni": "34987654", "pasaporte": "AR2201133"},
        "etiquetas": ["premium"],
        "productos": [
            {
                "tipo": "vista",
                "numero_cuenta": "V-001304",
                "fecha_apertura": datetime(2020, 10, 25),
                "bloqueo": False,
                "saldo_disponible": 500000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 3, 5), "monto": 500000.0, "tipo_transaccion": "abono"},
                    {"numero_transaccion": 2, "fecha": datetime(2026, 6, 30), "monto": 90000.0, "tipo_transaccion": "cargo"},
                ],
            },
        ],
    },
    {
        "rut": "20.345.678-9",
        "nombre": "Valentina",
        "apellido": "Soto",
        "fecha_nacimiento": datetime(1999, 4, 17),
        "nacionalidad": "Chilena",
        "sucursal": "Puente Alto",
        "contacto": {
            "telefono": "+56955667788",
            "domicilio": "Los Pajaritos 780",
            "comuna": "Puente Alto",
            "region": "Metropolitana",
            "email": "valentina.soto@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["vip", "premium"],
        "productos": [
            {
                "tipo": "ahorro",
                "numero_cuenta": "A-001405",
                "fecha_apertura": datetime(2018, 8, 30),
                "bloqueo": False,
                "saldo_disponible": 2100000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 1, 12), "monto": 400000.0, "tipo_transaccion": "abono"},
                    {"numero_transaccion": 2, "fecha": datetime(2026, 5, 22), "monto": 60000.0, "tipo_transaccion": "cargo"},
                ],
            },
            {
                "tipo": "corriente",
                "numero_cuenta": "C-001406",
                "fecha_apertura": datetime(2022, 11, 3),
                "bloqueo": False,
                "saldo_disponible": 180000.0,
                "linea_credito": 300000.0,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 6, 18), "monto": 220000.0, "tipo_transaccion": "abono"},
                ],
            },
        ],
    },
    {
        "rut": "16.789.012-4",
        "nombre": "Ignacio",
        "apellido": "Fuentes",
        "fecha_nacimiento": datetime(2003, 6, 8),
        "nacionalidad": "Chilena",
        "sucursal": "Las Condes",
        "contacto": {
            "telefono": "+56966778899",
            "domicilio": "El Bosque Norte 150",
            "comuna": "Las Condes",
            "region": "Metropolitana",
            "email": "ignacio.fuentes@mail.com",
        },
        "extranjero": None,
        "etiquetas": ["normalito"],
        "productos": [
            {
                "tipo": "vista",
                "numero_cuenta": "V-001507",
                "fecha_apertura": datetime(2025, 2, 14),
                "bloqueo": True,
                "saldo_disponible": 5000.0,
                "linea_credito": None,
                "transacciones": [
                    {"numero_transaccion": 1, "fecha": datetime(2026, 2, 14), "monto": 5000.0, "tipo_transaccion": "abono"},
                ],
            },
        ],
    },
]


def cargar_datos_iniciales(coleccion):
    """
    Inserta los datos dummy solo si la colección está vacía,
    para no duplicar documentos cada vez que se ejecuta el programa.
    """
    if coleccion.count_documents({}) == 0:
        resultado = coleccion.insert_many(CLIENTES_DUMMY)
        print(f"Se cargaron {len(resultado.inserted_ids)} clientes de ejemplo.")
    else:
        total = coleccion.count_documents({})
        print(f"La colección ya tiene {total} documentos. No se recargaron datos.")

