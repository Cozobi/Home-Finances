from app.core.config import USERS
from nicegui import app, ui


@ui.page("/")
def main_page():
    usuario_activo = app.storage.user.get("username", USERS[0])

    with ui.column().classes("w-full max-w-5xl mx-auto p-4 md:p-6"):
        with ui.row().classes("w-full justify-between items-center mb-3 flex-wrap gap-2"):
            with ui.column().classes("gap-0"):
                ui.label("Finanzas del Hogar - Real-Time").classes("text-2xl font-bold")
                ui.label(f"Sesión: {usuario_activo} ").classes("text-xs text-gray-500 dark:text-gray-400")

                # Boton de Cerrar Sesion
                ui.button(
                    icon="logout",
                    on_click=lambda: (app.storage.user.clear(), ui.navigate.to("/login"))
                ).props("flat round color=red").tooltip("Cerrar Sesión")

        with ui.tabs().classes("w-full bg-slate-100 dark:bg-slate-800 rounded-t") as tabs:
            tab_movs = ui.tab("Movimientos del Mes", icon="receipt_long")
            tab_cards = ui.tab("Tarjetas (Corte y Pago)", icon="credit_card")
            tab_rec = ui.tab("Pagos Recurrentes", icon="event_repeat")

        with ui.tab_panels(tabs, value=tab_movs).classes("w-full p-0 bg-transparent"):
            with ui.tab_panel(tab_movs).classes("p-0 pt-3"):
                ui.label("formulario y movimientos")

            with ui.tab_panel(tab_cards).classes("p-0 pt-3"):
                ui.label("tarjetas")

            with ui.tab_panel(tab_rec).classes("p-0 pt-3"):
                ui.label("pagos recurrentes")