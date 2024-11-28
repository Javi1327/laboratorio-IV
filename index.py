from conexion import DAO
import funciones


def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print("\t\t\t SISTEMA DE GESTION DE ALUMNOS.\n")
            print("=========== MENU PRINCIPAL ==========")
            print("1__ Listar Alumnos.")
            print("2__ Registrar Alumnos.")
            print("3__ Resgistrar Profesores.")
            print("4__ Listar Profesores.")
            print("5__ Registrar Cursos")
            print("6__ Listar Cursos.")
            print("7__ Registar Matriculas.")
            print("8__ Listar Matriculas.")
            print("9__ Mostrar curso Completo.")
            print("10__ Eliminar Alumnos/Profesores.")
            print("11__ Modificar Alumnos.")
            print("12__ Modificar Profesores.")
            print("13__ Salir")
            print("--------------------------------------------------------------------------")
            try:
                opcion = int(input("Seleccione una opción: ")) 
            except ValueError:
                print("Opcion no válida. Por favor, ingrese un número.")
                continue  # Vuelve a pedir la opción

            if opcion < 1 or opcion > 13: 
                print("Opción incorrecta, Ingrese una opción válida...")
            elif opcion == 13:
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
                funciones.listar_alumnos(cursos) 
            else:
                print("No se encontraron los datos del estudiante.")                                   
        except Exception as e:
            print(f"Ocurrió un error al mostrar los datos de los estudiantes: {e}")    
    elif opcion == 2:
        cursos = funciones.pedir_datos()
        try:
            dao.registrar_alumno(cursos)
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos del estudiante: {e}")   
    elif opcion == 3:
        profesor = funciones.pedir_datos_profe()
        try:
            dao.registrar_profesor(profesor)
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos del profesor: {e}")
    elif opcion == 4:
        try:
            prefes = dao.listar_datos_profesores()
            if len(prefes) > 0:
                funciones.listar_profesores(prefes) 
            else:
                print("No se encontraron los datos del profesor.")                                   
        except Exception as e:
            print(f"Ocurrió un error al mostrar los datos de los profesores: {e}") 
    elif opcion == 5:
        dao.registrar_curso()
    elif opcion == 6:
        try:
            curso = dao.listar_cursos()
            if len(curso) > 0:
                funciones.listar_curso(curso) 
            else:
                print("No se encontraron los datos de los cursos.")                                   
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos de los cursos: {e}")
    elif opcion == 7:
        dao.registrar_matricula()
    elif opcion == 8:
        try:
            matricula = dao.listar_matriculas()
            if len(matricula) > 0:
                funciones.listar_matricula(matricula) 
            else:
                print("No se encontraron las matrículas.")                                   
        except Exception as e:
            print(f"Ocurrió un error al mostrar los datos de las matrículas: {e}")
    elif opcion == 9:
        try:
            curso = dao.listar_cursos_completo()
            if len(curso) > 0:
                funciones.listar_curso_conpleto(curso) 
            else:
                print("No se encontraron los datos de los cursos.")                                   
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos de los cursos: {e}")           
    elif opcion == 10:
        print("Seleccione qué desea eliminar:")
        print("1. Alumno")
        print("2. Profesor")
        try:
            sub_opcion = int(input("Ingrese una opción: "))
            if sub_opcion == 1:
                id_alumno = int(input("Ingrese el ID del alumno a eliminar: "))
                dao.eliminar_logico("alumnos", id_alumno)
            elif sub_opcion == 2:
                id_profesor = int(input("Ingrese el ID del profesor a eliminar: "))
                dao.eliminar_logico("profesores", id_profesor)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar un número.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el registro: {e}")         
    
   
    elif opcion == 11: 
       
        tabla = 'estudiantes' 

        try:
            # Pedir el ID del registro a modificar
            id_registro = int(input(f"Ingrese el ID del {tabla} que desea modificar: "))
            
            # Verificar que el ID existe en la base de datos
            if not dao.registro_existe(tabla, id_registro):
                print(f"No existe un registro con el ID {id_registro} en {tabla}.")
                return

            # Pedir datos nuevos al usuario
            nuevos_datos = {}
            while True:
                campo = input("Ingrese el nombre del campo a modificar (o 'salir' para finalizar): ").lower()
                if campo == 'salir':
                    break
                if campo not in ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'direccion', 'telefono']:  # Asegúrate de que los campos sean válidos
                    print(f"Campo '{campo}' no es válido.")
                    continue
                valor = input(f"Ingrese el nuevo valor para {campo}: ")
                nuevos_datos[campo] = valor

            # Modificar los datos en la base de datos
            if nuevos_datos:
                dao.modificar_datos(tabla, id_registro, nuevos_datos)
                print(f"Datos del {tabla} con ID {id_registro} modificados correctamente.")
            else:
                print("No se ingresaron nuevos datos para modificar.")
                
        except ValueError:
            print("El ID debe ser un número válido.")
        except Exception as e:
            print(f"Error al modificar los datos: {e}")
    elif opcion == 12: 
       
        id_profesor = int(input("Ingrese el ID del profesor que desea modificar: "))
        
        # Pedir los nuevos datos
        nuevos_datos = {}
        while True:
            campo = input("Ingrese el nombre del campo a modificar (o 'salir' para finalizar): ").lower()
            if campo == 'salir':
                break
            valor = input(f"Ingrese el nuevo valor para {campo}: ")
            nuevos_datos[campo] = valor
        
        # Llamar al método para modificar los datos
        try:
            dao.modificar_datos_profesor(id_profesor, nuevos_datos)
        except Exception as e:
            print(f"Error al modificar los datos del profesor: {e}")


# Llamamos a la función para iniciar el menú
menu_principal()

                        