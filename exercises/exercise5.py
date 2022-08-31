"""For, Sum, Reduce."""

"""Devuelve la suma de los números de 1 a N.
    Restricción: Utilizar un bucle FOR.
    """

def sumatoria_basico(n: int) -> int:
    suma=0
    for i in range(n):
        suma = suma + (i+1)
    return suma

# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

"""Re-Escribir utilizando la función sum.
    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """

def sumatoria_sum(n: int) -> int:
    return sum(range(1+n))

# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

"""Toma un lista de números y devuelve el producto de todos los númereos. Si
    la lista está vacia debe devolver 0.
    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
def multiplicar_basico(numeros: Iterable[float]) -> float:
    producto = 1
    if numeros=[]:
        return 0

    for i in range(numeros):
        producto = producto * (i+1)
    return producto
    


numeros = [5, 6, 7, 8, 9]

print(multiplicar_basico(numeros))
print(multiplicar_basico([]))
# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN