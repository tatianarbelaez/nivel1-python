#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:21:58 2021

@author: invitado
"""

# Esto está en el archivo interfaz_saludar.py
import logica_saludar as logica

nombre = input("¿Cuál es su nombre? ")
saludo = logica.saludar(nombre)
print(saludo)