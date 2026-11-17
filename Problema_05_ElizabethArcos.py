# ------------------------------------------------------------
# Nombre del estudiante: Elizabeth Dayanna Arcos Parada
# Grupo: 213022_400
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Problema 5: Horas semanales trabajadas y clasificación de la jornada
# Código fuente: autoría propia
# ------------------------------------------------------------

# Constantes del problema
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
LIMITE_HORAS_SEMANA = 40      # Más de 40 horas se clasifica como "Sobretiempo"
MAXIMO_HORAS_DIA = 24         # Un día no puede tener más de 24 horas

# Matriz: [Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo_trabajo = [
    ["Ana Gómez", 8, 8, 8, 8, 8],
    ["Carlos Ruiz", 9, 10, 8, 9, 7],
    ["Laura Peña", 7, 8, 6, 8, 7],
    ["Jorge Díaz", 10, 9, 9, 8, 9]
]


def calcular_total_horas(fila_recurso):
    """Suma las horas de los cinco días de un recurso (columnas 1 a 5)."""
    total_horas = 0
    for posicion in range(1, len(fila_recurso)):
        total_horas = total_horas + fila_recurso[posicion]
    return total_horas


def clasificar_jornada(total_horas):
    """Retorna la clasificación según el total de horas semanales."""
    if total_horas > LIMITE_HORAS_SEMANA:
        return "Sobretiempo"
    else:
        return "Horario estándar"


def leer_horas(mensaje):
    """Pide un número de horas hasta que sea válido (entre 0 y 24)."""
    horas_validas = -1
    while horas_validas < 0:
        texto_horas = input(mensaje)
        try:
            numero_horas = float(texto_horas)
            if 0 <= numero_horas <= MAXIMO_HORAS_DIA:
                horas_validas = numero_horas
            else:
                print(f"Error: las horas deben estar entre 0 y {MAXIMO_HORAS_DIA}.")
        except ValueError:
            print("Error: debe ingresar un número.")
    return horas_validas


def mostrar_informe(matriz):
    """Procedimiento: muestra el total de horas y la clasificación de cada recurso."""
    print("\n================ INFORME SEMANAL DE HORAS ================")
    print(f"{'Recurso':<15}{'Total horas':>12}   Clasificación")
    print("-" * 58)
    for fila_recurso in matriz:
        total_horas = calcular_total_horas(fila_recurso)
        clasificacion = clasificar_jornada(total_horas)
        print(f"{fila_recurso[0]:<15}{total_horas:>12g}   {clasificacion}")
    print("-" * 58)


def actualizar_horas(matriz):
    """Procedimiento: permite cambiar las horas diarias de un recurso."""
    print("\nRecursos registrados:")
    for numero in range(len(matriz)):
        print(f"{numero + 1}. {matriz[numero][0]}")

    numero_recurso = 0
    while numero_recurso < 1 or numero_recurso > len(matriz):
        texto_recurso = input(f"Seleccione el recurso (1-{len(matriz)}): ")
        if texto_recurso.isdigit() and 1 <= int(texto_recurso) <= len(matriz):
            numero_recurso = int(texto_recurso)
        else:
            print("Error: opción de recurso no válida.")

    fila_recurso = matriz[numero_recurso - 1]
    for posicion in range(len(DIAS_SEMANA)):
        fila_recurso[posicion + 1] = leer_horas(f"Horas del {DIAS_SEMANA[posicion]}: ")
    print(f"Horas de {fila_recurso[0]} actualizadas correctamente.")


def menu_principal():
    """Muestra el menú y se repite hasta que el usuario elija salir."""
    opcion_menu = ""
    while opcion_menu != "3":
        print("\n===== CONTROL DE HORAS DEL EQUIPO =====")
        print("1. Mostrar informe semanal")
        print("2. Actualizar horas de un recurso")
        print("3. Salir")
        opcion_menu = input("¿Cuál es su opción? ").strip()

        if opcion_menu == "1":
            mostrar_informe(equipo_trabajo)
        elif opcion_menu == "2":
            actualizar_horas(equipo_trabajo)
        elif opcion_menu == "3":
            print("¡Gracias por usar el sistema!")
        else:
            print("Opción no válida. Ingrese 1, 2 o 3.")


if __name__ == "__main__":
    menu_principal()
