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

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/rpenad/nyc-taxi-tip-classifier.git
    cd nyc-taxi-tip-classifier
    ```

2. Crear y activar un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Descargar los datos crudos:
    ```bash
    python src/data/make_dataset.py
    ```

5. Preprocesar los datos:
    ```bash
    python src/features/build_features.py
    ```

6. Entrenar y evaluar el modelo:
    ```bash
    python src/models/train_model.py
    ```

7. Visualizar las importancias de las características:
    ```bash
    python src/visualization/visualizePara finalizar tu proyecto en GitHub y asegurarnos de que todo funcione correctamente, sigue estos pasos finales:

### Verificación y Ejecución del Proyecto
1. **Clonar el Repositorio**: En una nueva ubicación o en otra máquina, clona el repositorio para verificar la reproducibilidad.
    ```bash
    git clone https://github.com/rpenad/nyc-taxi-tip-classifier.git
    cd nyc-taxi-tip-classifier
    ```

2. **Crear y Activar un Entorno Virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instalar las Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Descargar los Datos Crudos**:
    ```bash
    python src/data/make_dataset.py
    ```

5. **Preprocesar los Datos**:
    ```bash
    python src/features/build_features.py
    ```

6. **Entrenar y Evaluar el Modelo**:
    ```bash
    python src/models/train_model.py
    ```

7. **Visualizar las Importancias de las Características**:
    ```bash
    python src/visualization/visualize.py
    ```

### Notebooks
Crea dos notebooks en el directorio `notebooks/` para la exploración de datos y el entrenamiento del modelo:

#### `notebooks/01-tuusuario-exploratory-data-analysis.ipynb`
Incluye celdas para cargar los datos, explorar las características, y visualizar estadísticas descriptivas.

#### `notebooks/02-tuusuario-train-model.ipynb`
Incluye celdas para cargar los datos, preprocesarlos, entrenar el modelo, evaluar el modelo y visualizar las importancias de las características. Asegúrate de incluir las siguientes celdas al inicio para la recarga automática de los módulos:
```python
%load_ext autoreload
%autoreload 2

from src.data import make_dataset
from src.features import build_features
from src.models import train_model
from src.visualization import visualize
