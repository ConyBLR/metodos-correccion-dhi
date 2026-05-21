# Corrección de Radiación Difusa (DHI) - Métodos Drummond y LeBaron

## Descripción
Este repositorio contiene la implementación en **Python** de los métodos clásicos de corrección para mediciones de Irradiancia Horizontal Difusa (DHI) registradas con banda sombreadora. 

El script permite corregir la subestimación intrínseca del piranómetro debida a la obstrucción de la banda, aplicando los modelos de:
*   **Drummond (1956)**
*   **LeBaron (1990)**

Este desarrollo fue validado y presentado en las **Actas de ASADES 2024**, proporcionando una base metodológica sólida para la caracterización de la radiación difusa en la región del NOA, Argentina.

## Características Técnicas
- Procesamiento de series temporales de radiación solar.
- Cálculo de factores de corrección geométrica y anisotrópica.
- Compatible con flujos de trabajo de análisis de datos científicos (Pandas/NumPy).

## Requisitos
- Python 3.x
- Bibliotecas: `pandas`, `numpy`, `matplotlib`

## Referencias y Validación
López Ruiz, C. B. (2024). "ANÁLISIS DE RADIACIÓN SOLAR DIFUSA MEDIDA USANDO BANDA SOMBREADORA. CASO DE ESTUDIO: CIUDAD DE SALTA". Actas de la XLVI Reunión de Trabajo de la Asociación Argentina de Energías Renovables y Ambiente (ASADES).

## Autor
**Constanza Belén Lopez Ruiz**  
Profesional del Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET).  
Instituto de Investigaciones en Energía No Convencional (INENCO).

## Licencia
Este proyecto está bajo la Licencia MIT.
