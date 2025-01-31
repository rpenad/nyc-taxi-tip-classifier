# NYC Taxi Tip Classifier - Clasificador de Propinas para Viajes en Taxi en NYC (2020) - Inspirado en la charla "Keeping up with Machine Learning in Production" de Shreya Shankar

Este proyecto construye un modelo de clasificación para predecir si una propina en un viaje en taxi en Nueva York será alta o baja, en relacion al notebook llamado 00_nyc-taxi-model.ipynb , en el cual se adiciona una nueva metodologia , al cambiar la herramienta para el entrenamiento  con  TensorFlow para entrenar tu modelo en lugar de scikit-learn. En este nuevo notebook vamos a integrar este nuevo enfoque , asegurándonos de incluir la evaluación del modelo en diferentes meses utilizando métricas como F1-score y curvas ROC.
## Nueva Estrategia de Clasificación

Se añadió una nueva estrategia de clasificación en el notebook 'ConEstrategia.ipynb'. Esta estrategia incluye:

1. **Diferencias en la selección de características**:
   - Se implementaron nuevas características derivadas de los datos temporales como `pickup_weekday`, `pickup_hour`, `pickup_minute`, y `work_hours`.
   - Adicionalmente, se calcularon características relacionadas con la duración y velocidad del viaje (`trip_time` y `trip_speed`).

2. **Modelo de Machine Learning diferente**:
   - En lugar del modelo original, se utilizó un modelo secuencial de Keras con varias capas densas (`Dense`), que es una red neuronal artificial.
   - El modelo se entrenó utilizando el optimizador Adam y la función de pérdida de entropía cruzada binaria.

3. **Evaluación del modelo**:
   - Los resultados muestran que el nuevo modelo obtuvo mejores puntuaciones de F1 y AUC-ROC en comparación con el modelo anterior.
   - Se generaron y compararon curvas ROC para diferentes meses, lo que permitió una evaluación más detallada del desempeño del modelo a lo largo del tiempo.

Para ejecutar el nuevo notebook, siga las mismas instrucciones descritas anteriormente para la configuración del entorno.


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
Clasificador de Propinas para Viajes en Taxi en NYC (2020)
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
