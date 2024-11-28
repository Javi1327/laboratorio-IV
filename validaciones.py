import datetime

def solicitar_fecha():
    while True:
        fecha_str = input("Ingrese la fecha de nacimiento (formato YYYY-MM-DD): ")
        
        # Validar el formato de la fecha
        # strptime() significa que se utiliza para analizar (parsear) una cadena de texto que representa una fecha y hora, y convertirla en un objeto datetime.
        try:
            fecha_ingresada = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date() # con el date solo obtengo (año, mes, dia)
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, use el formato YYYY-MM-DD.")
            continue # hace que el bucle vuelva al inicio, solicitando al usuario que ingrese unanuea fecha
        
        # Validar que la fecha no sea futura
        fecha_actual = datetime.date.today()
        if fecha_ingresada > fecha_actual:
            print("La fecha no puede ser futura. Ingrese una fecha válida.")
            continue
        
        # Si pasa todas las validaciones, salir del bucle
        return fecha_ingresada



def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre: ").strip()  # Eliminar espacios en blanco al inicio y al final

        # Verificar si el nombre está vacío
        if not nombre:
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")
            continue

        # Verificar que el nombre no exceda los 20 caracteres
        if len(nombre) > 20:
            print("El nombre es muy largo. Inténtalo de nuevo.")
            continue

        # Verificar que cada carácter sea una letra o un espacio
        if all(char.isalpha() or char.isspace() for char in nombre):
            return nombre
        else:
            print("El nombre solo puede contener letras y espacios. Inténtalo de nuevo.")
 


def solicitar_apellido():
    while True:
        apellido = input("Ingrese el apellido: ").strip()  # Eliminar espacios en blanco al inicio y al final

        # Verificar si el nombre está vacío
        if not apellido:
            print("El apellido no puede estar vacío. Inténtalo de nuevo.")
            continue

        # Verificar que el nombre no exceda los 20 caracteres
        if len(apellido) > 30:
            print("El apellido es muy largo. Inténtalo de nuevo.")
            continue

        # Verificar que cada carácter sea una letra o un espacio
        if all(char.isalpha() or char.isspace() for char in apellido):
            return apellido
        else:
            print("El apellido solo puede contener letras y espacios. Inténtalo de nuevo.") 
 

 
def solicitar_direccion():
    while True:
        direccion = input("Ingrese la dirección (debe contener letras y números): ").strip()

        # Verificar si la dirección está vacía
        if not direccion:
            print("La dirección no puede estar vacía. Inténtalo de nuevo.")
            continue
        
         # Verificar que el nombre no exceda los 20 caracteres
        if len(direccion) > 40: 
            print("La direccion es muy largo. Inténtalo de nuevo.")
            continue
        elif len(direccion) < 5:
            print("La direccion es muy corta. Inténtalo de nuevo.")
            continue

        # Inicializar las banderas
        contiene_letras = False
        contiene_numeros = False

        # Verificar cada carácter en la dirección
        for char in direccion:
            if char.isalpha():
                contiene_letras = True
            elif char.isdigit():
                contiene_numeros = True

        # Validar que contenga al menos una letra y un número
        if contiene_letras and contiene_numeros:
            return direccion
        else:
            print("La dirección debe contener al menos un nombre (letras) y números. Inténtalo de nuevo.") 
            
        
            
def solicitar_documento():
    while True:
        documento = input("Ingrese su número de documento: ").strip()  # Eliminar espacios en blanco al inicio y al final

        # Verificar si el documento está vacío
        if not documento:
            print("El documento no puede estar vacío. Inténtalo de nuevo.")
            continue

        # Verificar que el documento no exceda los 20 caracteres
        if len(documento) > 9: 
            print("La documento es muy largo. Inténtalo de nuevo.")
            continue
        elif len(documento) < 7:
            print("La documento es muy corto. Inténtalo de nuevo.")
            continue

        # Verificar que cada carácter sea un dígito
        if documento.isdigit():
            return documento
        else:
            print("El documento solo puede contener dígitos. Inténtalo de nuevo.")
    
       

def solicitar_telefono():
    while True:
        telefono = input("Ingrese su número de teléfono: ").strip()  # Eliminar espacios en blanco al inicio y al final

        # Verificar si el teléfono está vacío
        if not telefono:
            print("El teléfono no puede estar vacío. Inténtalo de nuevo.")
            continue

        # Verificar que el teléfono no exceda los 11 caracteres
        if len(telefono) > 11: 
            print("El número de teléfono es demasiado largo. Inténtalo de nuevo.")
            continue
        elif len(telefono) < 9:
            print("El número de teléfono es demasiado corto. Inténtalo de nuevo.")
            continue

        # Verificar que cada carácter sea un dígito
        if telefono.isdigit():
            return telefono
        else:
            print("El teléfono solo puede contener dígitos. Inténtalo de nuevo.")