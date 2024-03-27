import mysql.connector
from mysql.connector import Error
#DAO= data access object(objeto de acceso a datos)

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='universidad',
            charset='latin1'
            )
        except Error as ex:
            print("Error de conexión:", ex) 
            self.conexion = None  

    def listarCursos(self):
        if self.conexion is not None:  # Verificar si la conexión está establecida
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al ejecutar la consulta:", ex)
                return None
        else:
            print("La conexión no está establecida.")
            return None

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES('{0}', '{1}',{2})"
                cursor.execute(sql.format(curso[0],curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso registrado! \n")
            except Error as ex:
                print("error de conexion: {0}".format(ex))
    
    def actualizarCurso(self,curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = {1} where codigo = '{2}'"
                cursor.execute(sql.format(curso[1],curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado! \n")
            except Error as ex:
                print("error de conexion: {0}".format(ex))
    


    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

