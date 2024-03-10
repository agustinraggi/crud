from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("====== MENU PRINCIPAL ======")
            print("|1| Listar curso")
            print("|2| Registrar curso")
            print("|3| Actualizar curso")
            print("|4| Eliminar curso")
            print("|5| Salir")
            print("===========================")
            opcion = str(input ("seleccione una opccion: "))
            if opcion < "1" or opcion > "5":
                print("opccion incorrecta ingrese una opccion valida..... ")
            elif opcion == "5":
                continuar = False
                print("hasta luego....😊")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def  ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == "1":
        try:
            cursos = dao.listarCursos()    
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")
    elif opcion == "2":
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrio un error")
    elif opcion == "3":
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("codigo del curso a actualizar no encontrado.... \n")
            else:
                print("Código de curso no encontrado...\n")
        except:
            print("Ocurrió un error...")
    elif opcion == "4":
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")
menuPrincipal()