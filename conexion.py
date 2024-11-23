import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                user='root', 
                password='root',
                host='localhost', 
                database='escuela',
                port='3306'
            )
        except Error as e:
            print("Error al intentar la coneccion: ", e)    
    
    # mostrar todos los datos de la la tabla estudiantes
    def listar_datos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()  
                cursor.execute("SELECT nombre, apellido, fecha_nacimiento, direccion, telefono FROM estudiantes WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado      
            except Error as e:
                print("Error al intentar la coneccion: ", e)   
            finally:
                if cursor:
                    cursor.close()
     
                    
    #  cargar los datos del estudiantes                     
    def registrar_curso(self, curso):
        if self.conexion.is_connected():  # para saber si estamos conectados ala bd
            try: 
                cursor = self.conexion.cursor()
                sql = "INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (curso[0], curso[1], curso[2], curso[3], curso[4]))
                self.conexion.commit()
                print("se cargo los datos")
            except Error as e:
                print("Error al intentar la coneccion: ", e)   
            finally:
                if cursor:
                    cursor.close()   
                    
         
    #aqui va la consulta de modificacion del estudiante
    
    
                             
    #aqui va la consulta de eliminacion logico solo cambiar el estado a false                        