import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
def visualizar_estadisticas_vector(vector):
    """
    Calcula estadísticas descriptivas de un vector numérico y genera
    un panel de visualización con histograma (KDE) y boxplot.
   
    Parámetros:
    -----------
    vector : list o numpy.ndarray
        Vector de datos numéricos a analizar.
   
    Retorna:
    --------
    dict
        Diccionario con las métricas estadísticas calculadas.
    """
    # Convertir a arreglo de NumPy para operaciones eficientes
    v = np.asarray(vector, dtype=float)
   
    # 1. Cálculo de estadísticas descriptivas
    stats = {
        "Media": np.mean(v),
        "Mediana": np.median(v),
        "Desviación Estándar": np.std(v, ddof=1),
        "Varianza": np.var(v, ddof=1),
        "Mínimo": np.min(v),
        "Máximo": np.max(v),
        "Rango": np.ptp(v),
        "Q1 (25%)": np.percentile(v, 25),
        "Q3 (75%)": np.percentile(v, 75),
        "IQR (Rango Intercuartílico)": np.percentile(v, 75) - np.percentile(v, 25)
    }
   
    # Imprimir resumen tabular en consola
    print("=" * 40)
    print(" RESUMEN DE ESTADÍSTICAS DESCRIPTIVAS ")
    print("=" * 40)
    for clave, valor in stats.items():
        print(f"{clave:<30}: {valor:.4f}")
    print("=" * 40)
   
    # 2. Configuración de la visualización
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
   
    # Gráfico izquierdo: Histograma + Curva de Densidad (KDE)
    sns.histplot(v, kde=True, ax=axes[0], color="skyblue", bins="auto")
    axes[0].axvline(stats["Media"], color="red", linestyle="--", linewidth=1.5, label=f"Media: {stats['Media']:.2f}")
    axes[0].axvline(stats["Mediana"], color="green", linestyle="-", linewidth=1.5, label=f"Mediana: {stats['Mediana']:.2f}")
    axes[0].set_title("Distribución de Frecuencia y KDE", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Valores")
    axes[0].set_ylabel("Frecuencia")
    axes[0].legend()
   
    # Gráfico derecho: Diagrama de Caja (Boxplot) para dispersión y valores atípicos
    sns.boxplot(y=v, ax=axes[1], color="lightgreen", width=0.4)
    axes[1].set_title("Diagrama de Caja (Boxplot)", fontsize=12, fontweight="bold")
    axes[1].set_ylabel("Valores")
   
    # Ajustar diseño general
    plt.tight_layout()
    plt.show()
   
    return stats
 
# ==========================================
# Ejemplo de uso
# ==========================================
if __name__ == "__main__":
    # Generar un vector de datos de prueba (ej. distribución normal con algo de ruido)
    np.random.seed(42)
    datos_ejemplo = np.random.normal(loc=65, scale=12, size=1000)
   
    # Ejecutar la función con el vector
    resultados = visualizar_estadisticas_vector(datos_ejemplo)