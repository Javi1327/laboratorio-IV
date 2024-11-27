from prettytable import PrettyTable    #pip install prettytable
import validaciones

#  muestar los datos del estudiante en un tabla 
def listar_cursos(cursos):
    print("\t\tDATOS DEL ALUMNO")
    tabla = PrettyTable()
    tabla.field_names = ["#","NOMBRE", "APELLIDO", "DOCUMENTO", "FECHA-NACIMIENTO", "DIRECCION", "TELEFONO"]
    for index, cur in enumerate(cursos, start=1):
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