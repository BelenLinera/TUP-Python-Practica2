"""Bloque IF, operadores lógicos, función max y operador ternario."""
 
print("Ejercicio 1:")
def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor.
 
    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """
a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))
 
mayor=a
if b > a:
    mayor = b
print("El mayor es:")
print(mayor)    
 
maximo_basico(a, b)
 
# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN
 
 
###############################################################################
 
print("Ejercicio 2:")
def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """
 
a = float(input("Ingrese el 1er número: "))
b = float(input("Ingrese el 2do número: "))
 
print("El mayor es:")
print(max(a,b))
maximo_libreria(a,b)
 
# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN
 
 
###############################################################################
 
print("Ejercicio 3:")
def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """
 
a = float(input("Ingresar el primer número: "))
b = float(input("Ingresar el segundo número: "))
 
if a > b:
    mayor_numero = a
else:
    mayor_numero = b
 
print("El mayor número es el", mayor_numero)
 
maximo_ternario(a,b)
 
# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
 
