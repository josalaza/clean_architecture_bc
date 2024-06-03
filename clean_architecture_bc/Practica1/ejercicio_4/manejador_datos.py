class ManejadorDatos:
    def procesar(self, base_datos):
        base_datos.guardar("Datos guardados en la base de datos")
        datos_leidos = base_datos.leer()
        print("Datos leídos:", datos_leidos)