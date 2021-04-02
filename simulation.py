# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:07:28 2021

@author: MSI


Simulation électrique du circuit Weemove
"""
import numpy as np
import matplotlib.pyplot as plt

# Attribution des variables

Rb = 10**4
Rf = 1200
Ramp = 5600
Rc = 270 # ou 560
pRb = int(input('Valeur de pRb : '))
pRamp = int(input('Valeur de pRamp : '))
pRef = int(input('Valeur de pRef : '))
Cf = 1 * 10**(-6)
L = 1 * 10**(-3)
Vcc = 5 

# Calcul de Vl

def Vl():
    pass

# Calcul de Vamp

def Vamp(pRamp,Ramp, Vl):
    G = 1 + (pRamp/Ramp)
    Vamp = G * Vl
    return Vamp

# Calcul de Vf

def Vf(Vamp):
    return Vamp

# Calcul de Vref

def Vref():
    pass

# Calcul de Vcomp

def Vcomp(Vref, Vf):
    pass
    
# Calcul de Vb

def Vb(Vcomp):
    if Vcomp == 0:
        return 5
    if Vcomp == 5:
        return 4.3

# Calcul de Ib

def Ib(Vcc,Rb,pRb):
    Ib = (Vcc-0.7)/(Rb + pRb)
    return Ib

# Plot des graphiques



