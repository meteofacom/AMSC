# AMSC

Herramientas en **Python** para el procesamiento de datos crudos del proyecto **AMSC**: descarga/organización, limpieza, análisis y generación de resultados reproducibles.

> Guía detallada de uso: revisa el PDF **“Instrucciones de uso_ Código de procesamiento de datos crudos AMSC.pdf”** incluido en el repositorio.

---

## Características

- Procesamiento reproducible de datos crudos (lectura, limpieza y formateo).
- Flujo de trabajo modular por pasos.
- Scripts listos para ejecutar desde terminal o cuaderno (Jupyter).
- Salidas estructuradas para análisis y visualización posteriores.

---

## Requisitos

- Python 3.9+  
- Recomendado: entorno virtual (venv o conda)

Paquetes típicos (ajústalos según tus scripts):
- `pandas`, `numpy`, `matplotlib`
- (`pyyaml`, `tqdm`, `pyarrow`, etc., si aplica)

---

## Instalación rápida

```bash
# 1) Clonar
git clone https://github.com/meteofacom/AMSC.git
cd AMSC

# 2) (Opcional) Crear entorno
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3) Instalar dependencias (cuando se publique requirements.txt)
pip install -r requirements.txt
