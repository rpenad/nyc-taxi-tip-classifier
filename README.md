# NYC Taxi Tip Classifier

Este proyecto construye un modelo de clasificación para predecir si una propina en un viaje en taxi en Nueva York será alta o baja.

## Estructura del Proyecto

- `data/`
  - `external/`: Datos de terceras partes.
  - `interim/`: Datos intermedios transformados.
  - `processed/`: Datos finales listos para el modelado.
  - `raw/`: Datos crudos originales.

- `models/`: Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos.

- `notebooks/`: Jupyter notebooks.
  - Convención de nombres: `<step>-<ghuser>-<description>.ipynb`

- `references/`: Diccionarios de datos, manuales y otros materiales explicativos.

- `reports/`: Análisis generados en HTML, PDF, LaTeX, etc.
  - `figures/`: Gráficos y figuras generadas para ser usadas en los informes.

- `src/`: Código fuente del proyecto.
  - `data/`: Scripts para descargar o generar datos.
    - `make_dataset.py`
  - `features/`: Scripts para transformar datos crudos en características para el modelado.
    - `build_features.py`
  - `models/`: Scripts para entrenar modelos y usarlos para hacer predicciones.
    - `predict_model.py`
    - `train_model.py`
  - `visualization/`: Scripts para crear visualizaciones exploratorias y orientadas a resultados.
    - `visualize.py`

## Cómo Reproducir el Proyecto

1. Clonar el repositorio
2. Instalar las dependencias
3. Ejecutar los scripts en `src/`
