
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