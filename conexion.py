import mysql.connector
from mysql.connector import Error
import validaciones

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                user='root', 
                password='root',
                host='localhost', 
               # database='escuela',
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
                direccion VARCHAR(40),
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
            CREATE TABLE IF NOT EXISTS matriculas( 
                id INT AUTO_INCREMENT PRIMARY KEY,
                estudiantes_id INT,
                curso_id INT,
                fecha_matricula DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (estudiantes_id) REFERENCES estudiantes(id),
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )    
            ''')
           
            # Insertar datos en la tabla estudiantes si no existen
            self.insertar_datos_estudiantes(cursor)

            # Insertar datos en la tabla profesores si no existen
            self.insertar_datos_profesores(cursor)

            # Insertar datos en la tabla cursos si no existen
            self.insertar_datos_cursos(cursor)

            # Insertar datos en la tabla matriculas si no existen
            self.insertar_datos_matriculas(cursor)

            # Confirmar los cambios
            self.conexion.commit()
            # Confirmar los cambios
            self.conexion.commit()
                            
            # Cerrar el cursor
            cursor.close()
        except Error as e:
            print("Error al intentar la coneccion ala base de datos: ", e)    
    
    
    # cargar algunos datos por defecto al ejecutar el codigo
    def insertar_datos_estudiantes(self, cursor):
        estudiantes = [
            ('Juan', 'Pérez', '123456789', '2000-01-01', 'Calle Falsa 123', '5551234567', True),
            ('María', 'Gómez', '098765432', '1999-05-15', 'Avenida Siempre Viva 742', '5559876543', True),
            ('Carlos', 'López', '112233445', '2001-03-20', 'Boulevard 456', '5556543210', True)
        ]
        for estudiante in estudiantes:
            cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE documento = %s", (estudiante[2],))
            if cursor.fetchone()[0] == 0:  # Si no existe
                cursor.execute('''
                INSERT INTO estudiantes (nombre, apellido, documento, fecha_nacimiento, direccion, telefono, estado) VALUES
                (%s, %s, %s, %s, %s, %s, %s)
                ''', estudiante)

    def insertar_datos_profesores(self, cursor):
        profesores = [
            ('Ana', 'Martínez', '223344556', '5551112222', True),
            ('Luis', 'Fernández', '334455677', '5553334444', True)
        ]
        for profesor in profesores:
            cursor.execute("SELECT COUNT(*) FROM profesores WHERE documento = %s", (profesor[2],))
            if cursor.fetchone()[0] == 0:  # Si no existe
                cursor.execute('''
                INSERT INTO profesores (nombre, apellido, documento, telefono, estado) VALUES
                (%s, %s, %s, %s, %s)
                ''', profesor)

    def insertar_datos_cursos(self, cursor):
        cursos = [
            ('Matemáticas', 1, True),
            ('Historia', 2, True)
        ]
        for curso in cursos:
            cursor.execute("SELECT COUNT(*) FROM cursos WHERE nombre = %s", (curso[0],))
            if cursor.fetchone()[0] == 0:  # Si no existe
                cursor.execute('''
                INSERT INTO cursos (nombre, profesores_id, estado) VALUES
                (%s, %s, %s)
                ''', curso)

    def insertar_datos_matriculas(self, cursor):
        matriculas = [
            (1, 1, True),
            (2, 1, True),
            (3, 2, True)
        ]
        for matricula in matriculas:
            cursor.execute("SELECT COUNT(*) FROM matriculas WHERE estudiantes_id = %s AND curso_id = %s", (matricula[0], matricula[1]))
            if cursor.fetchone()[0] == 0:  # Si no existe
                cursor.execute('''
                INSERT INTO matriculas (estudiantes_id, curso_id, estado) VALUES
                (%s, %s, %s)
                ''', matricula)
   
   
    # mostrar todos los datos de la tabla estudiantes
    def listar_datos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()  
                cursor.execute("SELECT id, nombre, apellido, documento, fecha_nacimiento, direccion, telefono FROM estudiantes WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado      
            except Error as e:
                print("Error al intentar la coneccion en listar alumnos: ", e)   
            finally:
                if cursor:
                    cursor.close()
     
         
                    
    #  cargar los datos del estudiante                     
    def registrar_alumno(self, curso):
        if self.conexion.is_connected():  # para saber si estamos conectados ala bd
            try: 
                cursor = self.conexion.cursor()
                sql = "INSERT INTO estudiantes (nombre, apellido, documento, fecha_nacimiento, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (curso[0], curso[1], curso[2], curso[3], curso[4], curso[5]))
                self.conexion.commit()
                print("se cargo los datos")
            except Error as e:
                print("Error al intentar la coneccion cuando se carga los datos del alumno : ", e)   
            finally:
                if cursor:
                    cursor.close()  
    
    
    # Cargar los datos del profesor
    def registrar_profesor(self, profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO profesores (nombre, apellido, documento, telefono) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (profesor[0], profesor[1], profesor[2], profesor[3]))
                self.conexion.commit()
                print("Se cargaron los datos del profesor")
            except Error as e:
                print("Error al intentar la conexión cuando se cargan los datos del profesor: ", e)
            finally:
                if cursor:
                    cursor.close()  
                    
                    
    # Cargar los datos del curso manualmente
    def registrar_curso(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                nombre = validaciones.solicitar_nombre()
                profesor_id = int(input("Ingrese el ID del profesor: "))

                # Verificar si el profesor_id existe
                cursor.execute("SELECT id FROM profesores WHERE id = %s", (profesor_id,))
                if cursor.fetchone() is None:
                    print(f"El profesor con ID {profesor_id} no existe.")
                    return

                sql = "INSERT INTO cursos (nombre, profesores_id) VALUES (%s, %s)"
                cursor.execute(sql, (nombre, profesor_id))
                self.conexion.commit()
                print("Se cargaron los datos del curso")
            except Error as e:
                print("Error al intentar cargar los datos del curso: ", e)
            finally:
                if cursor:
                    cursor.close()

    # Cargar los datos de la matrícula manualmente
    def registrar_matricula(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                alumno_id = int(input("Ingrese el ID del alumno: "))
                curso_id = int(input("Ingrese el ID del curso: "))
                #fecha_matricula = input("Ingrese la fecha de matrícula (YYYY-MM-DD): ")

                # Verificar si el alumno_id existe
                cursor.execute("SELECT id FROM estudiantes WHERE id = %s", (alumno_id,))
                if cursor.fetchone() is None:
                    print(f"El alumno con ID {alumno_id} no existe.")
                    return

                # Verificar si el curso_id existe
                cursor.execute("SELECT id FROM cursos WHERE id = %s", (curso_id,))
                if cursor.fetchone() is None:
                    print(f"El curso con ID {curso_id} no existe.")
                    return

                sql = "INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula) VALUES (%s, %s, NOW())"
                cursor.execute(sql, (alumno_id, curso_id))
                self.conexion.commit()
                print("Se cargaron los datos de la matrícula")
            except Error as e:
                print("Error al intentar cargar los datos de la matrícula: ", e)
            finally:
                if cursor:
                    cursor.close()                
    
    
    # Listar todos los datos de la tabla profesores
    def listar_datos_profesores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT id, nombre, apellido, documento, telefono FROM profesores WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión al listar los profesores: ", e)
            finally:
                if cursor:
                    cursor.close()


    # Listar todos los datos de la tabla cursos
    def listar_cursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT nombre, profesores_id FROM cursos WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión al listar cursos: ", e)
            finally:
                if cursor:
                    cursor.close()                               
         
    # Mostrar todos los datos de la tabla matriculas
    def listar_matriculas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT estudiantes_id, curso_id, fecha_matricula FROM matriculas WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión al listar matriculas: ", e)
            finally:
                if cursor:
                    cursor.close()
                    
    def listar_cursos_completo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('''
                    SELECT 
                        e.nombre AS nombre_estudiante,
                        e.apellido AS apellido_estudiante,
                        c.nombre AS nombre_curso,
                        p.nombre AS nombre_profesor,
                        p.apellido AS apellido_profesor
                        FROM matriculas m
                        JOIN estudiantes e ON m.estudiantes_id = e.id
                        JOIN cursos c ON m.curso_id = c.id
                        JOIN profesores p ON c.profesores_id = p.id
                        ORDER BY e.nombre ASC;         
                ''')
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión al mostrar todos los cursos completos: ", e)
            finally:
                if cursor:
                    cursor.close()                
             
                    
      
    def modificar_estudiante(self, estudiante_id, nuevos_datos):
        if self.conexion.is_connected():
            try:
                with self.conexion.cursor() as cursor:
                    # Verificar si el registro existe
                    cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE id = %s", (estudiante_id,))
                    result = cursor.fetchone()
                    if result[0] == 0:
                        print(f"No existe un estudiante con ID {estudiante_id}.")
                        return

                    # Construir la consulta de actualización
                    update_query = '''
                        UPDATE estudiantes
                        SET nombre = %s, apellido = %s, documento = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s
                        WHERE id = %s
                    '''

                    # Ejecutar la consulta de actualización
                    cursor.execute(update_query, (
                        nuevos_datos['nombre'],
                        nuevos_datos['apellido'],
                        nuevos_datos['documento'],
                        nuevos_datos['fecha_nacimiento'],
                        nuevos_datos['direccion'],
                        nuevos_datos['telefono'],
                        estudiante_id
                    ))

                    # Confirmar los cambios
                    self.conexion.commit()

                    print(f"Estudiante con ID {estudiante_id} actualizado correctamente.")

            except Exception as e:
                print(f"Ocurrió un error al modificar el estudiante: {e}") 
    
    
    def modificar_profesor(self, profesor_id, nuevos_datos):
        if self.conexion.is_connected():
            try:
                with self.conexion.cursor() as cursor:
                    # Verificar si el registro existe
                    cursor.execute("SELECT COUNT(*) FROM profesores WHERE id = %s", (profesor_id,))
                    result = cursor.fetchone()
                    if result[0] == 0:
                        print(f"No existe un estudiante con ID {profesor_id}.")
                        return

                    update_query = '''
                        UPDATE profesores
                        SET nombre = %s, apellido = %s, documento = %s, telefono = %s
                        WHERE id = %s
                    '''

                    # Ejecutar la consulta de actualización
                    cursor.execute(update_query, (
                        nuevos_datos['nombre'],
                        nuevos_datos['apellido'],
                        nuevos_datos['documento'],
                        nuevos_datos['telefono'],
                        profesor_id
                    ))

                    # Confirmar los cambios
                    self.conexion.commit()

                    print(f"Profesor con ID {profesor_id} actualizado correctamente.")

            except Exception as e:
                print(f"Ocurrió un error al modificar al profesor: {e}")            
   
  
                             
    #  consulta de eliminacion logico solo cambiar el estado a false  
    def eliminar_logico(self, tabla, id_registro):
        if self.conexion.is_connected():
            try:
                with self.conexion.cursor() as cursor:
                    sql = f"UPDATE {tabla} SET estado = 0 WHERE id = %s"
                    cursor.execute(sql, (id_registro,))
                    self.conexion.commit()
                    print(f"Registro con ID {id_registro} eliminado lógicamente en la tabla {tabla}.")
            except Exception as e:
                print(f"Error al realizar el borrado lógico: {e}")
            finally:
                if cursor:
                    cursor.close()
                            
                            