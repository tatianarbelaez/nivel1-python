
"""
MODULO 1: Nivel 1
VALORES Y TIPOS DE DATOS

*a
números enteros (int)
números decimales (float)
cadenas de caracteres (str)
la funcion type permite consultar de qué tipo es un determinado valor. 
*b
Conversion de tipos de datos
int(x): convierte el valor x a un entero
float(x): convierte el valor x a un número decimal. 
str(x):convierte el valor x a una cadena de caracteres
""" 
nombre = 'Tatiana'
type(1290)
type(234.48)
type('tatiana')

int(1)
int(1.1)
int(-3)
int(a)

float(3)
float(2.86)
float(2,86)
float(3.4)
float(-3.4)

str(3)
str(12.98)

#Definir 4 variables (v1 hasta v4)
v1 = 5
v2 = 1 + 2
v3 = v1 + v2
v4 = v3 / (4+1)
print("v4:", v4) #Muestra el valor de la variable v4

""" 
*** Operadores matematicos 

Suma (+) ejemplo: 10 + 3 = 13

Resta (-) ejemplo: 10-3 =7 

Exponenciación (**)  ejemplo: 10 ** 3 = 1000

Cambio de signo (-) ejemplo: -(-2) = +2

Multiplicación (*) ejmplo: 10 * 3 = 30

División (/)  ejemplo: 10 / 3 = 3.3333

División entera (//) ejemplo: 10 // 3 = 3

Módulo (%) ejemplo: 10 % 3 = 1

***Operadores cadena de caracteres

Concatenación ejemplo: ‘abc’ + ‘def’ = ‘abcdef’

Repetición ejemplo:  ‘ab’ * 3 ‘ababab’

***expresiones con tipos de datos distintos
""" 

'A ' + nombre + ' le gusta bailar ' +  str(v2) + ' veces por semana'

'EJERCICIOS'

z = 7
z += 2
z *= 2
z //= 2
z -= 2
z %= 2
'a' * 3 + '/*' * 5 + 2 * 'abc' + '+'

""" 
***Funciones
-abs(x) --> sacar el valor absoluto
-round(n, digits) --> sirve para redondear un número para que sólo tenga la 
cantidad de decimales que nosotros le indiquemos
- round(n) --> redondea y convierte a entero
-min y max 
-pow(x,y)= x**y --> eleva x a la y
-print --> Cuando se invoca la función, ella se encarga de imprimir el valor de
cada uno de los parámetros separándolos con un espacio
-input
"""

def area_cuadrado(lado: int)-> int:
    """
    calcula el area de un cuadrado dada la medida de su lado
    """
    return lado * lado


def area_triangulo(base: int, altura: int)-> float:
    """
        Calcula el área de un triángulo dada la medida de la base y de la altura.
    """   
    return (base * altura) / 2


def area_casa(frente: int, techo: int)-> float:
    """
        Calcula el área del dibujo de una casa que se forma con un cuadrado
        y un triángulo encima (el techo).
        El frente de la casa será igual al lado del cuadrado y a la base del triángulo.
        La altura del techo será la altura del triángulo.
    """
    cuadrado = area_cuadrado(frente)
    triangulo = area_triangulo(frente, techo)
    return cuadrado + triangulo
    
medida_frente = 7
medida_techo = 5
resultado = area_casa(medida_frente, medida_techo)
print("El área de una casa con", medida_frente, "metros de frente y un techo de",
       medida_techo, "metros de alto es ", round(resultado, 2), "metros")
"""
1.Se invocará a la función area_cuadrado usando el valor 7 como valor para el parámetro lado.

2.Se calculará y retornará el valor de la expresión lado * lado que se encuentran en el cuerpo de area_cuadrado. En este caso, el valor retornado será 49 y ese valor se almacenará en la variable temporal cuadrado.

3.Se invocará a la función area_triangulo usando los valores 7 y 5 como valores para los parámetros base y altura.

4.Se calculará y retornará el valor de la expresión (base * altura) / 2 que se encuentran en el cuerpo de area_triangulo . En este caso, el valor retornado será 17.5 y ese valor se almacenará en la variable temporal triangulo.

5.Se calculará la suma de cuadrado y triangulo y se retornará el valor. Las variables cuadrado y triangulo dejan de existir en este momento porque terminó la ejecución de la función en la que fueron definidas.

6.El valor retornado se almacenará en la variable resultado.
"""
def saludar(nombre: str)-> str:
   return "Hola " + nombre + "!"

nombre = input("¿Cuál es su nombre? ")
saludo = saludar(nombre)
print(saludo)

#EJERCICIOS
"""
Cree el módulo “cuadrados.py” y defina una función que calcula el perímetro de un cuadrado y otra que calcula su área. Agregue al archivo las instrucciones para preguntarle al usuario por el lado de un cuadrado y luego 
mostrarle el perímetro y el área de un cuadrado con esa medida.
"""

def perimetro_cuadrado(medida_lado: float)-> float:
    return "El perimetro del cuadrado es igual a " + str(medida_lado * 4)
medida_lado = float(input("¿Cual es la medida del lado? "))
perimetro = perimetro_cuadrado(medida_lado)
print(perimetro)

def area_cuadrad(medida_lado: float)-> float:
    return "El area del cuadrado es igual a " + str(medida_lado * medida_lado)
medida_lado = float(input("¿Cual es la medida del lado? "))
area = area_cuadrad(medida_lado)
print(area)

"""
1. Defina una función que permita convertir de grados Celsius a grados Fahrenheit.

2. Defina una función que permita convertir de grados Fahrenheit a grados Celsius.

3. Escriba un programa que le pida al usuario una temperatura en grados Celsius y le informe a cuánto equivaldría esa temperatura en grados Fahrenheit.

4. Escriba un programa que le pida a un usuario una cantidad de días y le muestre la cantidad de años, meses y días equivalentes. Suponga que todos los meses tienen 30 días.
"""
#1 y 3
def convertirCelsius_Fah(grados_celsius: float)-> float:
    return grados_celsius * (9/5) + 32
grados_celsius = float(input("grados que quieres convertir a Fahrenheit "))
celsius_Fahrenheit = convertirCelsius_Fah(grados_celsius)
print(celsius_Fahrenheit)

#2 
def convertirFah_Celsius(grados_Fah: float)->float:
    return (grados_Fah - 32) * (5/9)
grados_Fah = float(input("grados que desea convertir a celsius "))
farenheit_celsius = convertirFah_Celsius(grados_Fah)
print(farenheit_celsius)

#4
def cantidad_tiempo(cantidad_dias:int)-> float:
    """
    calcula la cantidad de tiempo en años, meses y dias que representa un numero de dias, este numero de dias 
    es decidido mediante la pregunta 'cantidad de dias transcurridos desde que empezo a trabajar', la cantidad de dias
    que ingrese el usuario es un numero entero, el resultado es una concatenacion. 
    """
    return str(int(cantidad_dias/365)) + ' años ' + str(int(cantidad_dias/30)) + " meses y " + str(cantidad_dias) + " dias."
cantidad_dias = int(input("cantidad de dias transcurridos desde empezo a trabajar "))
tiempo = cantidad_tiempo(cantidad_dias)
print(tiempo)

"""
Revise detenidamente la siguiente función para descubrir su objetivo. Reescríbalo 
"""
def vc(r, a) :
    b = 3.14159 * (r**2)
    return round(b * a,2)

def volumen_cilindro(radio:float, altura:float)-> float:
    """
    Calcula el volumen de un cilindro a partir de su radio y su altura. 
    Tanto el radio como la altura deben ser números decimales.
    El resultado es un número decimal.
    """ 
    area_circulo = 3.14159 * (radio**2)
    return round(area_circulo * altura, 2)

"""
Construya un programa que le pida al usuario la medida del lado del cuadrado y le informe al usuario el tamaño del área de la zona negra.
es un cudrado con un circulo dentro, la parte negra es la parte por fuera del circulo. 
"""
def obtener_area_cuadrado(lado: float)-> float:
    return lado * lado

def obtener_area_circulo(radio: float)-> float:
    pi = 3.14159
    return pi * radio * radio 

def obtener_radio_desde_el_lado(lado: float)-> float:
    return lado / 2 

def obtener_area_zona_negra_cuadrado_circulo(lado: float)-> float:
    area_cuadrado = obtener_area_cuadrado(lado)
    radio = obtener_radio_desde_el_lado(lado)
    area_circulo = obtener_area_circulo(radio)
    return area_cuadrado - area_circulo


medida_lado = float(input("¿Cual es medida del lado del cuadrado? "))
area_zona_negra = obtener_area_zona_negra_cuadrado_circulo(medida_lado)
print("El area de la zona negra de la imagen es:", area_zona_negra)

    
