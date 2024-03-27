from BD.conexion import DAO
import funciones
import os

os.system("cls")

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def menuPrincipal():
    print("============================")
    print("        MENÚ PRINCIPAL")
    print("============================")
    print("| 1. Ventas                |")
    print("| 2. Porcentaje Cajas      |")
    print("| 0. Salir                 |")
    print("============================")

def subMenuVenta():
    print("============================")
    print("        MENÚ VENTA")
    print("============================")
    print("| 1. Listar Ventas         |")
    print("| 2. Registrar Venta       |")
    print("| 3. Modificar Venta       |")
    print("| 4. Eliminar Venta        |")
    print("| 0. Volver al Menú        |")
    print("============================")

def subMenuPorcentaje():
    print("============================")
    print("        MENÚ VENTA")
    print("============================")
    print("| 1. Listar Porcentajes     |")
    print("| 2. Registrar Porcentaje   |")
    print("| 3. Modificar Porcentaje   |")
    print("| 4. Eliminar Porcentaje    |")
    print("| 0. Volver al Menú         |")
    print("============================")

dao = DAO()  # Inicializar DAO fuera del bucle principal
menuPrincipal()
opcion = input("Seleccione una opción: ")
clear()
while opcion != "0":
    if opcion == "1":
        while True:
            subMenuVenta()
            opcionVenta = input("Seleccione una opción: ")
            clear()
            if opcionVenta == "1":
                try:
                    ventas = dao.listaVentas()
                    if ventas:
                        funciones.listaVentas(ventas)
                    else:
                        print("No se encontraron ventas.")
                except Exception as e:
                    print("Ocurrió un error:", e)
            elif opcionVenta == "2":
                venta = funciones.pedirDatosRegistrados(dao)
                if venta:
                    try:
                        dao.registrarVenta(venta)
                    except Exception as e:
                        print("Ocurrió un error al registrar la venta:", e)
            elif opcionVenta == "3":
                try:
                    ventas = dao.listaVentas()
                    venta = funciones.pedirDatosActualizacion(ventas)
                    if venta:
                        dao.actualizarVenta(venta)
                        print("Venta actualizada exitosamente.")
                    else:
                        print("La venta no fue encontrada")
                except Exception as e:
                    print("Ocurrió un error:", e)
            elif opcionVenta == "4":
                try:
                    ventas = dao.listaVentas()
                    ventaEliminar = funciones.pedirDatosEliminacion(ventas)
                    if ventaEliminar:
                        dao.eliminarVenta(ventaEliminar)
                        print("Venta eliminada exitosamente.")
                    else:
                        print("El ID ingresado no fue encontrado")
                except Exception as e:
                    print("Ocurrió un error:", e)
            elif opcionVenta == "0":
                clear()
                break  # Salir del bucle interno y volver al menú principal
            else:
                print("Opción inválida.")
    elif opcion == "2":
        while True:
            subMenuPorcentaje()
            opcionPorcentaje = input("seleccione una opccion: ")
            clear()
            if opcionPorcentaje == "1":
                try:
                    ventas = dao.listaPorcentaje()
                    if ventas:
                        funciones.listaPorcentaje(ventas)
                    else:
                        print("No se encontraron ventas.")
                except Exception as e:
                    print("Ocurrió un error:", e)
            elif opcionPorcentaje == "2":
                try:
                    fecha = str(input("Ingrese la fecha desde la cual desea calcular los porcentajes (formato: dd/mm/aaaa): "))
                    fecha = fecha.replace(' ', '/')
                    totalVentas = sum(venta[4] for venta in dao.obtenerVentasDesdeFecha(fecha))  # Suma de los totales de ventas
                    totalVentasAcumulado = dao.obtenerTotalVentasAcumulado(fecha)
                    totalVentasAcumulado = float(totalVentasAcumulado)  # Convertir a float
                    ganancia, proveedores, gastoFijo, empleados, total = funciones.cajaPorcentaje(totalVentas, totalVentasAcumulado)
                    # Guardar los porcentajes de caja en la tabla correspondiente
                    dao.porcentajeCaja(fecha, ganancia, proveedores, gastoFijo, empleados, total)
                    print("Porcentajes de caja calculados y guardados correctamente.")
                except Exception as e:
                    print("Ocurrió un error:", e)
            elif opcionPorcentaje == "3":
                print("")
            elif opcionPorcentaje == "4":
                print("")
            elif opcionVenta == "0":
                clear()
                break  # Salir del bucle interno y volver al menú principal
            else:
                print("Opción inválida.")
    else:
        print("Opción inválida.")
    menuPrincipal()
    opcion = input("Seleccione una opción: ")
    clear()
