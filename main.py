try:
    # El mensaje se mostrara en la pantalla y el valor ingresado se almacena en X
    X = float(input("Numero: "))

    #El proceso se ejecuta: 1/X
    inverse = 1.0 / X

except ValueError:
    # Este error se activa si se ingresa algun caracter no numerico
    print("Debe ser un int o float")

except ZeroDivisionError:
    # Este error se activa si se ingresa el valor 0 para X
    print("Infinito")

finally:
    # Este mensaje se imprime al finalizar el programa
    print("Puede que haya habido una excepcion o no.")

