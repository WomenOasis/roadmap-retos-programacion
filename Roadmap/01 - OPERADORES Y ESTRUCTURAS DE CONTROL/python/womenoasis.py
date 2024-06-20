# 1 Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

#Aritmeticos suma, resta, multiplicacion, dividir, rest
suma = 1 + 1
resta = 1 - 1
multiplicacion = 1 * 1
dividir = 1 / 1

print(suma)
print(resta)
print(multiplicacion)
print(dividir)

#Logicos (AND, OR, NOT)
# Y (and) = devuelve True si ambos operandos son True
# O (or) = devuelve True si al menos uno de los operando 
# No (not) = devuelve True si el operando es False y False si el operando es True
a = True
b = False

y_logicos = a and b # False
o_logicos = a or b # True
no_logico = not a # False
no_logico = not b # True 

print(y_logicos) # poner cada nombre de la variable

#Comparacion 
#igualdad (==) = comprueba si dos operandos son iguales 
#No igual (!=) = Comprueba si dos operandos son diferentes 
#Mayor que (>) = Comprueba si el primer operando es mayor que el segundo 
#Menor que (<) = Comprueba si el primer operando es menor que el segundo 
#Mayor o igual que (>=) = Comprueba si el primer operando es mayor o igual que el segundo 
#Menor o igual que (<=) = Comprueba si el primer operando es menor o igual que el segundo
x = 5
y = 10 

igualdad = x == y #False
no_igualdad = x != y # True 
mayor_que = x > y # False
menor_que = x < y # True
mayor_igual_que = x >= y # False 
menor_igual_que = x <= y #True

print(igualdad)
#Asignación 
#Asignacion (=) = Asigna un valor a una variable
#Asignacion con suma (+=) = suma el valor derecho el valor izquierdo y asigna el resultado a la variable izquierda 
#Asignacion con resta (-=) = Resta el valor derecho del valor izquierdo y asigna el resultado a la variable izquierda
#Asignacion con multiplicacion (*=) = Multiplica el valor derecho por el valor izquierdo y asigna el resultado a la variable izquierda
#Asignacion con division (/=) = Divide el valor izquierdo por el valor derecho y asigna el resultado a la variable izquierda
#Asignacion con division entera (//=) = Divide el valor izquierdo por el valor derecho, toma la parte entera y asigna el resultado a la variable izquierda
#Asignacion con modulo (%=) = Realiza la operacion de modulo en el valor izquierdo y el valor derecho y asigna el resultado a la variable izquierda 
#Asignacion con potencia (**=) = Eleva el valor izquierdo a la potencia del valor derecho y asigna el resultado a la izquierda 

#Es importante definir las variables antes de usarlas en operaciones abreviadas de asignación
x1 = 5
x2 = 5
x3 = 5
x4 = 5
x5 = 5
x6 = 5
x7 = 5
#La x vendria siendo el 5 
x1 += 3 # x + 3 es 8 
x2 -= 2 # x - 2 es 3 
x3 *= 4 # x * 4 es 24
x4 /= 3 # x /= 3 es 1.667 
x5 //= 2 # x // es 2
x6 %= 3 # x %/ es 2
x7 **= 2 # x ** es 25
# Estudiar como se hacen las operaciones

print(x7) # se va cambiando el x4 por el resto 

#Identidad is - is not
# es (is): Devuelve True si ambos operandos son el mismo objeto
#No es(is not):Devuelve True si los operandos no son el mismo objeti

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

mismo_objeto = lista1 is lista3 # True (es el mismo objeto ya que lista 3 no esta declarando nada)
diferente_obeto = lista1 is not lista2 # True (lista 1 y lista 2 aunque parezca que si no son iguales ya que 1 y 2 se stan guardando en diferente memorias)
print(diferente_obeto)

#pertenencia in- not in
# en (in): Devuelve True si el primer operando esta presente en el segundo operando (una secuencia)
#No es (nor in1): Devuelve True si el primer operando no esta presente en el segundo operando (una secuencia)
cadena = "Hola Mundo"
lista = [1, 2, 3]

esta_en_cadena = 'o' in cadena #True (la palabra o esta en la cadena que hola mundo)
no_esta_en_lista = 4 not in lista #True (en numero 4 no esta en la lista)

#bits
# AND a nivel del bits(&)
# OR a nivel de bits(|)
# XOR a nivel bits(^)
#Desplazamiento a la izquierda(<<)
#Desplazamiento a la derecha(>>)
#NOT a nivel de bits (~)
a = 60 #60 = 0011 1100 en binario 
b = 13 #13 = 0000 1101

AND = a & b # 12 = 0000 1100 en binario 
OR = a | b # 61 = 0011 1101 en binario 
XOR = a ^ b # 49 = 0011 00001 en binario 
desplazamiento_izquierda = a >> 2 # 240 = 1111 0000 en binario 
desplazamiento_derecha = a << 2 # 15 = 0000 1111 en binario
complemento_a_dos = ~a # -61
#Estudiar binario 
print(desplazamiento_izquierda)

# 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...+ que exista en python

#diferentes tipos de estructuras de control en Python
#condicionales (if, elif, else) 
x= 10 
if x > 5:
    print("x es mayor 5")
elif x == 5:
    print("x es igual 5")
else:
    print("x es menor que 5")

#iterativas (for y while)
#ciclo for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

#ciclo while
contador = 0
while contador < 5:
    print(contandor)
    contador += 1

#manejo de execepciones (try, except, finally)
try:
    numero = int(input("Ingrese un numero"))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Debe ingresar un numero valido")
finally:
    print("Fin del programa")

#Estos son ejemplos simples que representan cada tipo de estructura de control en Python. Las estructuras de control son esenciales para controlar el flujo de ejecución del programa, tomar decisiones, ejecutar código repetidamente y manejar situaciones inesperadas.


# 3. Debes hacer print por consola del resultado de todos los ejemplos.
# 4. 
# DIFICULTAD EXTRA (opcional): Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
#número es par (num % 2 == 0), se prueba asi
#si no es el 16 (num != 16) 
# y si no es múltiplo de 3 (num % 3 != 0). 