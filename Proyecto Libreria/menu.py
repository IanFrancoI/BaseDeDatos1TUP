from conexion import BaseDeDatos
from entidades.libro import Libro
from entidades.usuario import Usuario
from entidades.prestamo import Prestamo
from entidades.pago import Pago
import datetime

def biblioteca_menu(db):
    import datetime
    usuario = Usuario(db)
    prestamo = Prestamo(db)
    pago = Pago(db)
    libro = Libro(db)
    

    def gestionar_usuarios():
        print("\n--- Gestión de usuarios ---")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Ver usuario por ID")
        print("6. Ver usuario por nombre")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario:")
            direccion = input("Ingrese la dirección del usuario:")
            telefono = input("Ingrese el teléfono del usuario:")
            fecha = input("Ingrese la fecha en la que se registró el usuario:")
            estado = input("Ingrese el estado de la cuota del usuario (Paga/Impago):")
            mensaje = usuario.registrar_usuario(nombre,direccion,telefono,fecha,estado)
            print(mensaje)
        elif opcion == "2":
            usuarios = usuario.ver_usuarios()
            for i in usuarios:
                print(i)
        elif opcion == "3":
            id = input("ingrese el id del usuario que desea actualizar:")
            nombre = input("Ingrese el nuevo nombre del usuario:")
            direccion = input("Ingrese la nueva direccion del usuario:")
            telefono = input("Ingrese el nuevo telefono del usuario:")
            fecha = input("Ingrese la nueva fecha en la que se registro el usuario:")
            estado = input("Ingrese el nuevo estado de la cuota del usuario (Paga/Impago):")
            mensaje = usuario.actualizar_usuario(id,nombre,direccion,telefono,fecha,estado)
            print (mensaje)
        elif opcion == "4":
            id = input("Ingrese el id del usuario que desea eliminar:")
            mensaje = usuario.eliminar_usuario(id)
            print(mensaje)
        elif opcion == "5":
            id = input("Ingrese el id del usuario que desea ver:")
            mensaje = usuario.ver_usuario(id)
            print (mensaje)
        elif opcion == "6":
            nombre = input("Ingrese el nombre del usuario que desea ver:")
            mensaje = usuario.buscar_usuario_por_nombre(nombre)
            print(mensaje)

    def gestionar_libros():
        print("\n--- Gestión de libros ---")
        print("1. Registrar nuevo libro")
        print("2. Ver libro por su ID")
        print("3. Actualizar información de un Libro")
        print("4. Eliminar libro")
        print("5. Ver todos los libros")
        print("6. Ver libro por su título")
        print("7. Ver libro por su autor")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            titulo = input("Ingrese el título del libro:")
            autor = input("Ingrese el autor del libro:")
            anio = input("Ingrese el año de creacion del libro:")
            categoria = input("Ingrese la categoría del libro:")
            estado = input("Ingrese el estado del libro (Disponible/No disponible):")
            mensaje = libro.registrar_libro(titulo,autor,anio,categoria,estado)
            print(mensaje)
        elif opcion == "2":
            id = input("Ingrese el id del libro que desea ver:")
            mensaje = libro.ver_libro(id)
            print(mensaje)
        elif opcion == "3":
            id = input("Ingrese el id del libro que desea actualizar:")
            titulo = input("Ingrese el título actualizado del libro:")
            autor = input("Ingrese el autor actualizado del libro:")
            anio = input("Ingrese el año actualizado de creación del libro:")
            categoria = input("Ingrese la categoría actualizada del libro:")
            estado = input("Ingrese el estado actualizado del libro (Disponible/No disponible):")
            mensaje = libro.actualizar_libro(id,titulo,autor,anio,categoria,estado)
            print (mensaje)
        elif opcion == "4":
            id = input("Ingrese el id del libro que desea eliminar: ")
            mensaje = libro.eliminar_libro(id)
            print(mensaje)
        elif opcion == "5":
            libros = libro.ver_libros() 
            if libros:
                for i in libros:
                    print(i)
        elif opcion == "6":
            titulo = input("Ingrese el título del libro que desea buscar: ")
            mensaje = libro.buscar_libro_por_titulo(titulo)
            print(mensaje)
        elif opcion == "7":
            autor = input("Ingrese el autor del libro que desea buscar: ")
            mensaje = libro.buscar_libro_por_autor(autor)
            print(mensaje)       
                 
    def manejar_prestamos():
        print("\n--- Manejo de préstamos ---")
        print("1. Calcular multa")
        print("2. Registrar nuevo préstamo")
        print("3. Actualizar préstamo")
        print("4. Eliminar préstamo")
        print("5. Ver préstamos")
        print("6. Ver préstamo")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":            
          dias_retraso = int(input("Ingrese los días de retraso: "))
          cuota_mensual = float(input("Ingrese la cuota mensual del usuario: "))
          multa = dias_retraso * (0.03 * cuota_mensual)
          print(f"La multa por {dias_retraso} días de retraso es: ${multa:.2f}")
        elif opcion == "2":
            id1 = input("Ingrese el id del usuario:")
            id2 = input("Ingrese el id del libro:")
            fechaP = input("Ingrese la fecha en que se realizó el préstamo:")
            fechaD = input("Ingrese la fecha en la que se devolvió el libro:")
            multa = input("Ingrese el valor de la multa:")
            mensaje = prestamo.registrar_prestamo(id1,id2,fechaP,fechaD,multa)
            print(mensaje)
        elif opcion == "3":
            id = input("Ingrese el id del préstamo que desea modificar:")
            id1 = input("Ingrese el id actualizado del usuario:")
            id2 = input("Ingrese el id actualizado del libro:")
            fechaP = input("Ingrese la fecha actualizada en que se realizó el préstamo:")
            fechaD = input("Ingrese la fecha actualizada de devolución del libro:")
            multa = input("Ingrese el valor actualizado de la multa:")
            mensaje = prestamo.actualizar_prestamo(id,id1,id2,fechaP,fechaD,multa)
            print(mensaje)
        elif opcion == "4":
            id = input("Ingrese el id del préstamo que desea eliminar: ")
            mensaje = prestamo.eliminar_prestamo(id)
            print(mensaje)
        elif opcion == "5":
            prestamos = prestamo.ver_prestamos()
            for i in prestamos:
                print(i)
        elif opcion == "6":
            id = input("Ingrese el id del péstamo que quiere ver:")
            mensaje = prestamo.ver_prestamo(id)
            print (mensaje)

    def manejar_pagos():
        print("\n--- Manejo de Pagos ---")
        print("1. Registrar Nuevo Pago")
        print("2. Actualizar Pago")
        print("3. Eliminar Pago")
        print("4. Ver Pagos")
        print("5. Ver Pago")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id = input("Ingrese el id del usuario:")
            fechaP = input("Ingrese la fecha en que se realizó el pago:")
            monto = input("Ingrese el valor de la multa (si no tiene multa es 0):")
            mensaje = pago.registrar_pago(id,fechaP,monto)
            print(mensaje)
        elif opcion == "2":
            id = input("Ingrese el id del pago que desea modificar:")
            id1 = input("Ingrese el id actualizado del usuario:")
            fechaP = input("Ingrese la fecha actualizada en que se realizó el pago:")
            monto = input("Ingrese el monto actualizado del pago:")
            mensaje = pago.actualizar_pago(id,id1,fechaP,monto)
            print(mensaje)
        elif opcion == "3":
            id = input("Ingrese el id del pago que desea eliminar: ")
            mensaje = pago.eliminar_pago(id)
            print(mensaje)
        elif opcion == "4":
            pagos = pago.ver_pagos()
            for i in pagos:
                print(i)
        elif opcion == "5":
            id = input("Ingrese el id del pago que quiere ver:")
            mensaje = pago.ver_pago(id)
            print(mensaje)

    def reporte_morosos():
        impagos = usuario.ver_fecha_usuarios()
        if len(impagos) == 0:
            print("No hay socios con cuotas impagas.")
        else:
            total_meses = 0
            for i in impagos:
              fecha_registro = i[0]
              diferencia_meses = (datetime.datetime.now().year  - fecha_registro.year) * 12 + (datetime.datetime.now().month - fecha_registro.month)
              total_meses += diferencia_meses
            promedio_meses = total_meses / len(i)
            print(f"El promedio de meses de los socios con cuotas impagas es: {promedio_meses:.2f} meses.")

        
        
#MENU
    while True:
        print("\n=== Menú de la Biblioteca ===")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Libros")
        print("3. Gestión de Préstamos")
        print("4. Gestión de Pagos")
        print("5. Reporte de morosos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_usuarios()
        elif opcion == "2":
            gestionar_libros()
        elif opcion == "3":
            manejar_prestamos()
        elif opcion == "4":
            manejar_pagos() 
        elif opcion == "5":
            reporte_morosos()               
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")



if __name__ == "__main__":
    print("Ingrese los datos de conexión:")
    host = input("Host: ")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    database = input("Base de datos: ")
 
    db = BaseDeDatos(host, user, password, database)
    db.conectar()

    biblioteca_menu(db)

    db.desconectar()
