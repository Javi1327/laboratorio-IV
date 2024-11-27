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
            # Crear un cursor
            cursor = self.conexion.cursor()
            
            # Crear la base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS escuela2")
            
            # Seleccionar la base de datos
            cursor.execute("USE escuela2")

            # Crear la tabla estudiantes si no existe
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(20),
                apellido VARCHAR(30),
                documento VARCHAR(10),
                fecha_nacimiento DATE,
                direccion VARCHAR(30),
                telefono VARCHAR(15),
                estado BOOLEAN DEFAULT TRUE
            )
            ''')
            # Crear la tabla profesores si no existe
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS profesores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(20),
                apellido VARCHAR(30),
                documento VARCHAR(10),
                telefono VARCHAR(15),
                estado BOOLEAN DEFAULT TRUE
            )
            ''')

            # Crear la tabla cursos si no existe
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(30),
                profesores_id INT,
                estado BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (profesores_id) REFERENCES profesores(id)
            )
            ''')

            # Crear la tabla matriculas si no existe
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS matriculas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                estudiante_id INT,
                curso_id INT,
                fecha_matricula DATE,
                estado BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )
            ''')
            # Cerrar el cursor
            cursor.close()
            
        except Error as e:
            print("Error al intentar la coneccion: ", e)    
    
    
    # mostrar todos los datos de la la tabla estudiantes
    def listar_datos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()  
                cursor.execute("SELECT nombre, apellido, documento, fecha_nacimiento, direccion, telefono FROM estudiantes WHERE estado = true")
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
                sql = "INSERT INTO estudiantes (nombre, apellido, documento, fecha_nacimiento, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (curso[0], curso[1], curso[2], curso[3], curso[4], curso[5]))
                self.conexion.commit()
                print("se cargo los datos")
            except Error as e:
                print("Error al intentar la coneccion cuando se carga los datos : ", e)   
            finally:
                if cursor:
                    cursor.close()   
                    
         
    #aqui va la consulta de modificacion del estudiante
    
    
                             
    #aqui va la consulta de eliminacion logico solo cambiar el estado a false                        