# proyecto 1 matematica discreta
# Antony David Saz 24710


from itertools import product

# Conjuntos definidos
U = {'a','b','c','d','e','f','g','h','i','j','k',1,2,3,4,5}
A = {'a', 1, 3, 'd', 'g', 'h', 4, 5}
B = {2, 1, 4, 'e', 'f', 'g', 'k'}
C = {'b', 'd', 'f', 'h', 'k', 2, 4}
D = set()
E = {(1, 'a'), (2, 'b'), (3, 'c')}

# Función para imprimir resultados
def mostrar_operacion(nombre, resultado):
    print(f"{nombre} = {resultado}")

# Verificar si una relación es una función
def es_funcion(rel):
    dominio = [x[0] for x in rel]
    return len(dominio) == len(set(dominio))

# Operaciones sin símbolos especiales
mostrar_operacion("A union C", A | C)
mostrar_operacion("A interseccion C", A & C)
mostrar_operacion("A diferencia B", A - B)
mostrar_operacion("Complemento de A (U menos A)", U - A)
mostrar_operacion("(A union B) interseccion C", (A | B) & C)
mostrar_operacion("D diferencia U", D - U)
mostrar_operacion("Complemento de D (U menos D)", U - D)

# Producto cartesiano
cartesiano = set(product(A, B))
mostrar_operacion("A x B (producto cartesiano)", cartesiano)
print("A x B es funcion?:", es_funcion(cartesiano))

# Función E
mostrar_operacion("Relación E", E)
print("E es funcion?:", es_funcion(E))



