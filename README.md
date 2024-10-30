# H4CK1NG_T00L v2.0

## Descripción

**H4CK1NG_T00L** es una suite de herramientas de **penetración y análisis de seguridad** diseñada para ofrecer una solución completa y escalable. Esta herramienta está orientada tanto a usuarios principiantes como avanzados en el campo de la ciberseguridad, con un enfoque en una **interfaz gráfica intuitiva** que facilita la ejecución de tareas comunes de pruebas de penetración.

En esta versión 2.0, se ha implementado una estructura modular que permite una mayor **escalabilidad y facilidad de mantenimiento**. Cada módulo se encuentra separado en scripts individuales, lo cual facilita la adición de nuevas funcionalidades en el futuro.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

- **main.py**: Archivo principal que inicia la interfaz gráfica y coordina las funcionalidades.
- **/GUI**: Módulos que manejan los aspectos visuales de la herramienta.
  - `dark_theme.py`: Implementa un tema oscuro para la GUI.
  - `frames.py`: Define los frames y ventanas de la interfaz.
- **/TOOLS**: Módulos que contienen las herramientas principales de análisis.
  - `dir_scanner.py`: Realiza un análisis basado en diccionario para encontrar directorios web.
  - `metadata_analyzer.py`: Extrae metadatos de documentos PDF y Word.
- **/UTILS**: Módulos utilitarios para gestionar diversas funciones auxiliares.
  - `file_handler.py`: Maneja operaciones de archivos necesarias.
  - `http_requests.py`: Realiza peticiones HTTP/HTTPS para las funcionalidades de análisis.

## Funcionalidades

### 1. Análisis de Directorios Web
- Realiza un análisis basado en diccionario para identificar directorios en una URL específica, verificando su disponibilidad a través de peticiones HTTP/HTTPS.

### 2. Análisis de Metadatos
- Extrae metadatos de documentos PDF y Word, revelando información potencialmente sensible como nombres de autores, fechas de modificación y detalles del software utilizado.

## Uso

Para ejecutar la herramienta, simplemente ejecuta `main.py`. La interfaz gráfica te permitirá navegar por las diferentes funcionalidades, proporcionando una experiencia de usuario fluida y sencilla.

```bash
python main.py
