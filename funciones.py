from prettytable import PrettyTable    #pip install prettytable
import validaciones

#  muestar los datos del estudiante en un tabla 
def listar_alumnos(cursos):
    print("\t\t\tDATOS DEL LOS ALUMNOS")
    tabla = PrettyTable()
    tabla.field_names = ["#", "ID", "NOMBRE", "APELLIDO", "DOCUMENTO", "FECHA-NACIMIENTO", "DIRECCION", "TELEFONO"]
    for index, cur in enumerate(cursos, start=1):
        tabla.add_row([index] + list(cur))
    print(tabla)
    

#  muestar los datos del profesor en un tabla 
def listar_profesores(profes):
    print("\t\tDATOS DEL LOS PROFESORES")
    tabla = PrettyTable()
    tabla.field_names = ["#","ID", "NOMBRE", "APELLIDO", "DOCUMENTO", "TELEFONO"]
    for index, cur in enumerate(profes, start=1):
        tabla.add_row([index] + list(cur))
    print(tabla)  
    

#  muestar los datos del cursos en un tabla 
def listar_curso(curso):
    print("\t\tDATOS DEL LOS CURSOS")
    tabla = PrettyTable()
    tabla.field_names = ["#","NOMBRE_CURSO", "ID_PROFESOR",]
    for index, cur in enumerate(curso, start=1):
        tabla.add_row([index] + list(cur))
    print(tabla)  
        

# listar las matriculas
def listar_matricula(curso):
    print("\t\tDATOS DEL LAS MATRICULAS") 
    tabla = PrettyTable()
    tabla.field_names = ["#", "ESTUDIANTE_ID", "CURSO_ID", "FECHA"]
    for index, cur in enumerate(curso, start=1):
        tabla.add_row([index] + list(cur))
    print(tabla) 
    
#  muestar los datos del cursos completo en un tabla 
def listar_curso_conpleto(curso):
    print("\t\tDATOS DEL LOS CURSO COMPLETO ASECENDENTE")
    tabla = PrettyTable()
    tabla.field_names = ["#","NOMBRE_ESTUDIANTE","APELLIDO_ESTUDIANTE","NOMBRE_CURSO", "NOMBRE_PROFESOR","APELLIDO_PROFESOR"]
    for index, cur in enumerate(curso, start=1):    
        tabla.add_row([index] + list(cur))
    print(tabla)      
        
    
# pido al usuario que los cargue los datos del alumno
def pedir_datos():
    nombre = validaciones.solicitar_nombre()  
    apellido =  validaciones.solicitar_apellido()
    documento = validaciones.solicitar_documento()
    fecha_nacimiento = validaciones.solicitar_fecha()
    direccion = validaciones.solicitar_direccion()    
    telefono = validaciones.solicitar_telefono()    
    
    curso = (nombre, apellido, documento, fecha_nacimiento, direccion, telefono)
    return curso


# pido al usuario que los cargue los datos del profesor
def pedir_datos_profe():
    nombre = validaciones.solicitar_nombre()  
    apellido =  validaciones.solicitar_apellido()
    documento = validaciones.solicitar_documento()
    #fecha_nacimiento = validaciones.solicitar_fecha()
   # direccion = validaciones.solicitar_direccion()    
    telefono = validaciones.solicitar_telefono()    
    
    profesor = (nombre, apellido, documento, telefono)
    return profesor


def pedir_datos_curso():
    nombre = validaciones.solicitar_nombre()  
    id_profesor = int(input("ingrese el ID del profesor: "))
    
    curso = (nombre, id_profesor)
    return curso

def pedir_datos_matricula():
    id_alumno = int(input("INgree el ID del alumno: "))
    id_curso = int(input("ingrese el ID del curso: "))
   # fecha = validaciones.solicitar_fecha()
    
    matricula = (id_alumno, id_curso)
    return matricula


# nuevos datos del estudiante 
def obtener_datos_estudiante():
    nombre = validaciones.solicitar_nombre()  
    apellido =  validaciones.solicitar_apellido()
    documento = validaciones.solicitar_documento()
    fecha_nacimiento = validaciones.solicitar_fecha()
    direccion = validaciones.solicitar_direccion()    
    telefono = validaciones.solicitar_telefono()

    nuevos_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'fecha_nacimiento': fecha_nacimiento,
        'direccion': direccion,
        'telefono': telefono
    }

    return nuevos_datos

# nuevos datos del profesor
def obtener_datos_profesor():
    nombre = validaciones.solicitar_nombre()  
    apellido =  validaciones.solicitar_apellido()
    documento = validaciones.solicitar_documento()  
    telefono = validaciones.solicitar_telefono()

    nuevos_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'telefono': telefono
    }

    return nuevos_datos