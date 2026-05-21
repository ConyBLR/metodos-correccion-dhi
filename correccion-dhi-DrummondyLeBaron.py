# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:22:30 2024

@author: Cony
"""

import pandas as pd
import numpy as np
import math 

class LeBaron:
    def __init__(self):
            self.b = 0.12 # mts
            self.r = 0.329 #mts
            self.Io = 1361
            self.lat = math.radians(-24.72888)
             
    
    def correccion_dhi(self, dfa):
        
        coef = pd.DataFrame()
        coef['TIMESTAMP'] = dfa.TIMESTAMP
        coef['CTZ'] = (dfa.CTZ).values
        coef['glo_h'] = (dfa.ghi).values
        coef['dif_hu'] = (dfa.dhi).values
        coef['am'] = (dfa.Mak).values
        coef['decli'] =  (dfa.deltaRad).values
        coef['w0'] = (dfa.ws).values
        coef['TZ_grad'] = np.degrees(np.arccos(coef.CTZ))
        coef['dir_nu'] = (coef['glo_h']- coef['dif_hu'])/(np.cos(coef.TZ_grad))
        coef['epsilon'] = (coef['dif_hu'] + coef['dir_nu']) / coef['dif_hu']
        coef['delta'] = coef['dif_hu'] * (coef.am/self.Io)

        a0 = (2*self.b*np.cos(coef.decli)**3)/(self.r*np.pi)
        a1 = (np.cos(self.lat) * np.cos(coef.decli) * np.sin(coef.w0))
        a2 = (coef.w0 * np.sin(self.lat) * np.sin(coef.decli))

        f0 = (1 / (1 - (a0*(a1+a2))))

        coef['geometric'] =  f0


        # Matrices
        m11 = [
            [1.051, 1.082, 1.117, 1.173],
            [1.051, 1.104, 1.115, 1.163],
            [1.069, 1.082, 1.119, 1.140],
            [1.047, 1.063, 1.074, 1.030]
        ]

        m21 = [
            [1.051, 1.082, 1.117, 1.248],
            [1.051, 1.082, 1.117, 1.184],
            [1.161, 1.161, 1.147, 1.168],
            [1.076, 1.078, 1.104, 1.146]
        ]

        m31 = [
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.187, 1.167, 1.139, 1.191]
        ]

        m41 = [
            [1.051, 1.082, 1.117, 1.181],
            [1.051, 1.082, 0.990, 1.104],
            [1.015, 1.016, 0.946, 1.027],
            [0.925, 0.967, 0.977, 1.150]
        ]

        m12 = [
            [1.051, 1.082, 1.117, 1.176],
            [1.051, 1.095, 1.130, 1.162],
            [1.073, 1.089, 1.115, 1.142],
            [1.058, 1.076, 1.117, 1.156]
        ]

        m22 = [
            [1.051, 1.082, 1.117, 1.211],
            [1.051, 1.082, 1.186, 1.194],
            [1.086, 1.130, 1.168, 1.177],
            [1.074, 1.102, 1.118, 1.174]
        ]

        m32 = [
            [1.051, 1.082, 1.117, 1.237],
            [1.051, 1.082, 1.203, 1.212],
            [1.080, 1.195, 1.211, 1.185],
            [1.140, 1.098, 1.191, 1.181]
        ]

        m42 = [
            [1.051, 1.082, 1.117, 1.217],
            [1.051, 1.082, 1.120, 1.180],
            [1.182, 1.115, 1.081, 1.111],
            [1.057, 1.119, 1.133, 1.033]
        ]


        m13 = [
            [1.051, 1.082, 1.117, 1.182],
            [1.051, 1.082, 1.128, 1.159],
            [1.076, 1.088, 1.131, 1.129],
            [1.060, 1.085, 1.103, 1.156]
        ]

        m23 = [
            [1.051, 1.082, 1.117, 1.221],
            [1.051, 1.171, 1.180, 1.213],
            [1.135, 1.148, 1.176, 1.197],
            [1.092, 1.119, 1.143, 1.182]
        ]


        m33 = [
            [1.051, 1.082, 1.117, 1.238],
            [1.051, 1.160, 1.207, 1.230],
            [1.169, 1.191, 1.193, 1.210],
            [1.150, 1.133, 1.180, 1.156]
        ]

        m43 = [
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.089, 1.194, 1.216, 1.064]
        ]


        m14 = [
            [1.051, 1.082, 1.117, 1.191],
            [1.051, 1.105, 1.143, 1.168],
            [1.085, 1.093, 1.117, 1.156],
            [1.069, 1.082, 1.117, 1.156]
        ]

        m24 = [
            [1.051, 1.082, 1.117, 1.238],
            [1.051, 1.148, 1.195, 1.230],
            [1.132, 1.160, 1.183, 1.210],
            [1.118, 1.116, 1.150, 1.185]
        ]

        m34 = [
            [1.051, 1.082, 1.117, 1.232],
            [1.051, 1.206, 1.210, 1.238],
            [1.144, 1.178, 1.226, 1.216],
            [1.117, 1.155, 1.178, 1.167]
        ]

        m44 = [
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.051, 1.082, 1.117, 1.156],
            [1.024, 1.025, 1.162, 1.142]
        ]

        #
        # Classification mapping
        def classify_parameters(value, ranges):
            for category, (lower, upper) in ranges.items():
                #print(category, lower, upper)
                if lower <= value < upper:
                    return category
                else:
                    if value < 0:
                        category = 4
            return category

        # Define parameter ranges
        TZ_ranges = {1: (0.0, 35.0), 2: (35.0, 50.0), 3: (50.0, 60.0)}
        geometric_ranges = {1: (1.000, 1.068), 2: (1.068, 1.100), 3: (1.100, 1.132)}
        epsilon_ranges = {1: (0.000, 1.253), 2: (1.253, 2.134), 3: (2.134, 5.980)}
        delta_ranges = {1: (0.000, 0.120), 2: (0.120, 0.200), 3: (0.200, 0.300)}

        # Apply classification
        coef['TZ_categoria'] = coef['TZ_grad'].apply(
            lambda x: classify_parameters(x, TZ_ranges))
        
        coef['geometric_categoria'] = coef['geometric'].apply(
            lambda x: classify_parameters(x, geometric_ranges))
        
        coef['epsilon_categoria'] = coef['epsilon'].apply(
            lambda x: classify_parameters(x, epsilon_ranges))
        
        coef['delta_categoria'] = coef['delta'].apply(
            lambda x: classify_parameters(x, delta_ranges))

        # Crear una lista de matrices
        matrices = [[m11, m12, m13, m14],
                    [m21, m22, m23, m24],
                    [m31, m32, m33, m34],
                    [m41, m42, m43, m44]]

        for index, row in coef.iterrows():
            a = row['TZ_categoria'] -1
            b = row['geometric_categoria'] -1
            c = row['epsilon_categoria']-1
            d = row['delta_categoria']-1
            e = row['dif_hu'] # valor a corregir 
            elemento = matrices[a][b][c][d]
            # Verificamos que los índices estén dentro del rango
            if 0 <= a < len(matrices) and 0 <= b < len(matrices[0]) and 0 <= c < len(matrices[0][0]) and 0 <= d < len(matrices[0][0][0]):
                elemento = matrices[a][b][c][d]
                coef.loc[index, 'factor'] = elemento
               # print(f"Elemento en la matriz ({a+1}, {b+1}) en la posición ({c+1}, {d+1}): {elemento}")
               # Aumenta 'e' por el porcentaje
                dif_corr = e * elemento
               # Agrega el resultado a una nueva columna llamada 'dato_modificado'
                coef.loc[index, 'dif_corregida'] = dif_corr
            else:
                print(f"Índices fuera de rango para ({a}, {b}, {c}, {d})")   

            
        return coef

class Drummond:
    def __init__(self):
            self.b = 0.12 # mts
            self.r = 0.329 #mts
            self.Io = 1361
            self.lat = math.radians(-24.72) 
             
    
    def correccion_dhi(self, dfa):
        
        coef = pd.DataFrame()
        coef['TIMESTAMP'] = dfa.TIMESTAMP
        coef['CTZ'] = (dfa.CTZ).values
        coef['glo_h'] = (dfa.ghi).values
        coef['dif_hu'] = (dfa.dhi).values
        coef['am'] = (dfa.Mak).values
        coef['decli'] =  (dfa.deltaRad).values
        coef['w0'] = (dfa.ws).values
        coef['TZ_grad'] = np.degrees(np.arccos(coef.CTZ))
        coef['dir_nu'] = (coef['glo_h']- coef['dif_hu'])/(np.cos(coef.TZ_grad))
        coef['epsilon'] = (coef['dif_hu'] + coef['dir_nu']) / coef['dif_hu']
        coef['delta'] = coef['dif_hu'] * (coef.am/self.Io)

        a0 = (2*self.b*np.cos(coef.decli)**3)/(self.r*np.pi)
        a1 = (np.cos(self.lat) * np.cos(coef.decli) * np.sin(coef.w0))
        a2 = (coef.w0 * np.sin(self.lat) * np.sin(coef.decli))

        f0 = (1 / (1 - (a0*(a1+a2))))
        
        coef['geometric'] =  f0
        coef['dif_corregida'] = f0*coef.dif_hu

        
        return coef