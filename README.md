# Mi Paquete de Estadística (mi_paquete1)
 
Paquete de Python diseñado para calcular métricas de estadística descriptiva y generar visualizaciones gráficas rápidas (histogramas con KDE y diagramas de caja) a partir de vectores numéricos.
 
---
 
## Características
 
- Cálculo automatizado de media, mediana, desviación estándar, varianza, cuartiles y rango intercuartílico (IQR).
- Generación de paneles gráficos limpios utilizando `matplotlib` y `seaborn`.
- Estructura moderna de empaquetado con `pyproject.toml`.
 
---
 
## Requisitos previos
 
Asegúrate de tener instalado Python (versión 3.8 o superior). Las siguientes librerías se instalarán automáticamente al instalar el paquete:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
 
---
 
## Instalación
 
Puedes instalar el paquete directamente desde el repositorio de GitHub usando `pip`:
 
```bash
pip install git+https://github.com/msmejia/mi_paquete1.git
 
Ejemplo de uso
Una vez instalado el paquete, puedes importar la función en cualquier script de Python de la siguiente manera:
import numpy as np
from mi_paquete import visualizar_estadisticas_vector
 
# 1. Generar datos de prueba
np.random.seed(42)
datos = np.random.normal(loc=65, scale=12, size=1000)
 
# 2. Ejecutar la función
resultados = visualizar_estadisticas_vector(datos)
 
# 3. Ver los resultados estadísticos en consola
print("\nResultados obtenidos:")
print(f"Media: {resultados['Media']:.2f}")
print(f"Desviación Estándar: {resultados['Desviación Estándar']:.2f}")
 
Autor
Ing. Edwin Mejia - Trabajo inicial - Espoch