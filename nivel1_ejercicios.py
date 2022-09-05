#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:00:24 2021

@author: invitado
"""

def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    """ Tiempo de descarga
    Parámetros:
      velocidad (int): Velocidad de descarga de la red, en Mbps
      tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
      int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    gb_megas = tamanio_archivo * 1000
    v = velocidad * 8
    tiempo = gb_megas / v
    return round(tiempo)
tiempo_descarga = calcular_tiempo_descarga(150,0.23)
print(tiempo_descarga)

def calcular_iva_propina_total_factura (costo_factura: int) -> str:
    """ IVA y propina
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por coma
    """
    IVA = round (costo_factura*19/100)
    propina = round (costo_factura*10/100) 
    total = round (costo_factura + propina + IVA)
    return str(IVA) + "," + str(propina) + "," + str(total)
costo_total = calcular_iva_propina_total_factura(1728201202)
print(costo_total)

"""
Enunciado: El volumen de un cilindro se puede calcular multiplicando el área de su base
circular por su altura. Cree una función que reciba el radio de la base y la altura del
cilindro, y calcule su volumen. Retorne el resultado redondeado a un solo decimal.
"""
def calcular_volumen_cilindro(radio:float, altura: float)-> float:
    return round((3.14159 * (radio**2) * altura),1)
volumen_cilindro = calcular_volumen_cilindro(3, 6)
print (volumen_cilindro)

"""
Enunciado: Cree una función que pueda calcular el índice de masa corporal (BMI) de una
persona a partir de su peso en libras y su altura en pulgadas. La fórmula para calcular
el BMI es la siguiente: 𝐵𝑀𝐼=𝑝𝑒𝑠𝑜/(𝑎𝑙𝑡𝑢𝑟𝑎2), pero para que la fórmula funcione 𝑝𝑒𝑠𝑜 debe
estar en kilogramos y 𝑎𝑙𝑡𝑢𝑟𝑎 en metros. Recuerde que 1 libra corresponde a 0.454 kg, y 
que 1 pulgada corresponde a 0.0254 metros. El valor de retorno debe estar redondeado a dos decimales.
"""


def calcularBMI(peso_libras:float, altura_pulgadas: float)-> float:
    peso_kg = peso_libras/2.205
    altura_metro = altura_pulgadas/39.37
    return (peso_kg/(altura_metro**2))
BMI = calcularBMI(138.8, 60.62)
print(BMI)


