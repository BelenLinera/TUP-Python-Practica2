"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad.
"""
 
print("Ejercicio 1:")
def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.
 
    Restricciones:
        - Utilizar comparaciones encadenadas.
        - Utilizar UNICAMENTE dos IFs
        - No utilizar ELSE
        - No utilizar AND, OR o NOT
 
    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons # noqa: E501
    """
a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))
c = float(input("Ingresar el tercer número: "))
 
mayor=a
if b > a:
    mayor = b
if c > b > a:
    mayor = c
print("El mayor es", mayor)                        
max(a,b,c)
 
##preguntar!!!
 
# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(5, 10, 1) == 10
assert maximo_encadenado(5, 10, 5) == 10
 
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(9, 4, 18) == 18
assert maximo_encadenado(9, 9, 18) == 18
 
assert maximo_encadenado(24, 9, 18) == 24
assert maximo_encadenado(24, 18, 9) == 24
assert maximo_encadenado(24, 18, 18) == 24
# NO MODIFICAR - FIN
 
 
###############################################################################
 
print("Ejercicio 2:")
def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    """Re-escribir para que tome 4 parámetros, utilizar la función max.
 
    Referencia: https://docs.python.org/3/library/functions.html#max"""
 
a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))
c = float(input("Ingresar el tercer número: "))
d = float(input("Ingresar el cuarto número: "))
 
mayor = max(a, b, c, d)
print("El mayor es", mayor)
 
 
# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
 
 
###############################################################################
 
 
def maximo_arbitrario(*args) -> float:
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists # noqa: E501
    """

 
# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
 
##preguntar!!!
