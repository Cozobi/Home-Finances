from nicegui import ui
from app.view.pages import landing
import os

STORAGE_SECRET = os.getenv("APP_SECRET_KEY", "clave-secreta-hogar-cambiar-en-prod-2026")


ui.run(
    title="Finanzas del Hogar",
    host="0.0.0.0",
    port=8080,
    storage_secret=STORAGE_SECRET,
    reload=False
)