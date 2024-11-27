from conexion import DAO
import funciones
#import pandas

def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print("=========== MENU PRINCIPAL ==========")
            print("""
                  1__ Listar curso.
                  2__ Registra curso.
                  3__ Actualizar curso.
                  4__ Eliminar curso.
                  5__ Salir.
                  """)
            print("--------------------------------------------------------------------------")
            try:
                opcion = int(input("Seleccione una opción: ")) 
            except ValueError:
                print("Opcion no válida. Por favor, ingrese un número.")
                continue  # Vuelve a pedir la opción

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, Ingrese una opción válida...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este Sistema!")
                break
            else:
                opcion_correcta = True
                ejecute_opcion(opcion)  # Asegúrate de que esta función esté definida
                    
def ejecute_opcion(opcion):
    dao = DAO()
    
    if opcion == 1:
        try:
            cursos = dao.listar_datos()
            if len(cursos) > 0:
                funciones.listar_cursos(cursos) 
            else:
                print("No se encontraron los datos del estudiante.")                                   
        except:
            print("ocurrio un error al mostra los datos", cursos)    
    elif opcion == 2:
        cursos = funciones.pedir_datos()
        try:
            dao.registrar_curso(cursos)
        except Exception as e:
            print(f"Ocurrió un error al mostrar los datos: {e}")   
    elif opcion == 3:
        print("actualizacion") 
    elif opcion == 4:
        print("eliminacion")  
    else:
        print("opcion no valida...")           
    
    
menu_principal()    
                        