"""Para especificar las opciones de configuración de la aplicación."""
import os

class Config:
    """
    Clase para almacenar las variables de configuración.

    Atributos:
        SECRET_KEY -- se usa para proteger los formularios web ante ataques CSRF.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Christ-is-King-of-kings'
