def listarCursos(cursos):
    print("cursos: ")
    contador = 1
    for cur in cursos:
        datos = "{0}. codigo: {1} | nombre: {2} ({3} creditos)"
        print(datos.format(contador, cur[0],cur[1],cur[2]))
        contador+=1
    print("")

def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = str(input("Ingrese el código del curso (debe tener 6 dígitos): "))
        if len(codigo) == 6 :
            codigoCorrecto = True
        else:
            print("¡Código incorrecto! Debe tener exactamente 6 dígitos.")
    nombre = str(input("Ingrese el nombre del curso: "))
    CreditosCorrecto = False
    while(not CreditosCorrecto):
        creditos = str(input("Ingrese la cantidad de créditos del curso: "))
        if creditos.isnumeric():
            if int(creditos) > 0:
                CreditosCorrecto = True
                creditos = int(creditos)
            else:
                print("\nlos creditos no pueden ser cero o negativos\n")
        else:
            print("\ncreditos incorrecto, debe ser numeros")
    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el código a modificar: ")
    for cur in cursos:
        if cur[0] == int(codigoEditar):
            existeCodigo = True
            break
    if existeCodigo:
        nombre = str(input("Ingrese el nombre a modificar: "))
        CreditosCorrecto = False
        while(not CreditosCorrecto):
            creditos = str(input("Ingrese la cantidad de créditos a modificar: "))
            if creditos.isnumeric():
                if int(creditos) > 0:
                    CreditosCorrecto = True
                    creditos = int(creditos)
                else:
                    print("\nlos creditos no pueden ser cero o negativos\n")
            else:
                print("\ncreditos incorrecto, debe ser numeros")
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None
    return curso


def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == int(codigoEliminar):
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""
    return codigoEliminar

