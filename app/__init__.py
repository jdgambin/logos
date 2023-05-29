"""Para decirle a Flask que lea y aplique el archivo de configuración."""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
