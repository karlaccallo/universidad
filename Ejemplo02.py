# Declaracion de variables y asignaciones de valores
a = 10
b = 9

try:
    # Condicional para evaluar que ambos valores sean mayores a 0

    if a < 0 or b < 0:

        #Lanzar una excepcion con cierto nombre (raise NombreEception)
        raise ZeroDivisionError

    #Imprimir en pantalla el resultado de a/b en caso no se cumpla la condicion
    print(a/b)

except ZeroDivisionError:

    #En caso suceda el error, se imprime el mensaje
    print("por favor, ingrese un valor valido")
