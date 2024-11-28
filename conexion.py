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
                            
            # Insertar datos en la tabla estudiantes
            cursor.execute('''
            INSERT INTO estudiantes (nombre, apellido, documento, fecha_nacimiento, direccion, telefono, estado) VALUES
            ('Juan', 'Pérez', '123456789', '2000-01-01', 'Calle Falsa 123', '5551234567', TRUE),
            ('María', 'Gómez', '098765432', '1999-05-15', 'Avenida Siempre Viva 742', '5559876543', TRUE),
            ('Carlos', 'López', '112233445', '2001-03-20', 'Boulevard 456', '5556543210', TRUE);
            ''')

            # Insertar datos en la tabla profesores
            cursor.execute('''
            INSERT INTO profesores (nombre, apellido, documento, telefono, estado) VALUES
            ('Ana', 'Martínez', '223344556', '5551112222', TRUE),
            ('Luis', 'Fernández', '334455677', '5553334444', TRUE);
            ''')

            # Insertar datos en la tabla cursos
            cursor.execute('''
            INSERT INTO cursos (nombre, profesores_id, estado) VALUES
            ('Matemáticas', 1, TRUE),  
            ('Historia', 2, TRUE);      
            ''')

            # Insertar datos en la tabla matriculas
            cursor.execute('''
            INSERT INTO matriculas (estudiante_id, curso_id, estado) VALUES
            (1, 1, TRUE),   
            (2, 1, TRUE),   
            (3, 2, TRUE);        
            ''') 
                        
            # Cerrar el cursor
            cursor.close()
            
        except Error as e:
            print("Error al intentar la coneccion: ", e)    
    
    
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
                print("\nREGISTRAR A UN ALUMNO.")
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
                print("\nREGISTRAR UN PROFESOR.")
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
                print("\nREGISTRAR CURSO.")
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
                print("\nREGISTRAR MATRICULA.")
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
                print("Error al intentar la conexión: ", e)
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
                print("Error al intentar la conexión: ", e)
            finally:
                if cursor:
                    cursor.close()                               
         
    # Mostrar todos los datos de la tabla matriculas
    def listar_matriculas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT estudiante_id, curso_id, fecha_matricula FROM matriculas WHERE estado = true")
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión: ", e)
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
                        JOIN estudiantes e ON m.estudiante_id = e.id
                        JOIN cursos c ON m.curso_id = c.id
                        JOIN profesores p ON c.profesores_id = p.id
                        ORDER BY e.nombre ASC;         
                ''')
                resultado = cursor.fetchall()
                return resultado
            except Error as e:
                print("Error al intentar la conexión: ", e)
            finally:
                if cursor:
                    cursor.close()                
             
                    
                    
                         
    #aqui va la consulta de modificacion del estudante o profesor
    def modificar_datos(self, tabla, id_registro, nuevos_datos):
        try:
            conexion = self.conexion()  # Asegúrate de que este método esté correctamente definido
            cursor = conexion.cursor()
            
            # Construir la consulta UPDATE dinámicamente según los campos proporcionados
            set_clause = ", ".join([f"{campo} = %s" for campo in nuevos_datos.keys()])
            valores = list(nuevos_datos.values())
            valores.append(id_registro)  # Agregar el ID al final de la lista de valores

            consulta = f"UPDATE {tabla} SET {set_clause} WHERE id = %s"
            cursor.execute(consulta, tuple(valores))
            
            conexion.commit()  # Confirmar los cambios
            cursor.close()
            conexion.close()
            print(f"Registro con ID {id_registro} actualizado correctamente.")
        except Exception as e:
            print(f"Error al modificar los datos: {e}")


    # Verificar la existencia de un registro
    def registro_existe(self, tabla, id_registro):
        try:
            conexion = self.conexion()  # Llamamos correctamente a la función de conexión
            if conexion is None:
                raise Exception("No se pudo establecer conexión con la base de datos.")
            
            cursor = conexion.cursor()
            
            consulta = f"SELECT COUNT(*) FROM {tabla} WHERE id = %s"
            cursor.execute(consulta, (id_registro,))
            existe = cursor.fetchone()[0]
            
            cursor.close()
            conexion.close()
            
            return existe > 0  # Retorna True si existe, False si no

        except Exception as e:
            print(f"Error al verificar la existencia del registro: {e}")
            return False

    #modificacion de profesores
    

    def modificar_datos_profesor(self, id_profesor, nuevos_datos):
        try:
            # Establecer la conexión con la base de datos
            self.conexion
            cursor = self.conexion.cursor
            
            # Construir la consulta SQL para actualizar los datos
            set_clause = ", ".join([f"{campo} = %s" for campo in nuevos_datos.keys()])
            values = tuple(nuevos_datos.values())
            
            # Consulta SQL para actualizar los datos
            consulta = f"UPDATE profesores SET {set_clause} WHERE id = %s"
            cursor.execute(consulta, (*values, id_profesor))
            
            # Verificar si se actualizó algún registro
            if cursor.rowcount == 0:
                print(f"No existe un registro con el ID {id_profesor} en profesores.")
            else:
                # Guardar cambios y cerrar la conexión
                conexion.commit()
                print("Datos del profesor actualizados correctamente.")
            
            cursor.close()
            conexion.close()
        except Exception as e:
            print(f"Error al modificar los datos del profesor: {e}")

  
                             
    #aqui va la consulta de eliminacion logico solo cambiar el estado a false
    
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
                            
                            