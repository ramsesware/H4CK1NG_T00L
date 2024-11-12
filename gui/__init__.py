# Importar funciones específicas para simplificar la importación desde gui
from .dark_theme import apply_dark_theme
from .frames import create_main_window, create_directory_analysis_frame, create_metadata_analysis_frame

# Puedes exponer los componentes que desees
__all__ = ["apply_dark_theme", "create_main_window", "create_directory_analysis_frame", "create_metadata_analysis_frame"]
