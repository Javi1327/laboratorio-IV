from prettytable import PrettyTable    #pip install prettytable
import validaciones

#  muestar los datos del estudiante en un tabla 
def listar_cursos(cursos):
    print("\t\tDATOS DEL ALUMNO")
    tabla = PrettyTable()
    tabla.field_names = ["#","NOMBRE", "APELLIDO", "FECHA-NACIMIENTO", "DIRECCION", "TELEFONO"]
    for index, cur in enumerate(cursos, start=1):
        tabla.add_row([index] + list(cur))
    print(tabla)
    
# pido al usuario que los cargue    
def pedir_datos():
    nombre = validaciones.solicitar_nombre()  
    apellido = input("ingrese el apellido : ") #falta hacer la validacion del apellido
    fecha_nacimiento = validaciones.solicitar_fecha()
    direccion = validaciones.solicitar_direccion()    
    telefono = input("ingrese el numero de telfono: ") #falta hacer la validacoin de telefono    
    
    curso = (nombre, apellido, fecha_nacimiento, direccion, telefono)
    return curso