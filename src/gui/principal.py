import customtkinter as ctk
from config.config import *


class PrincipalFrame(ctk.CTkFrame):  # Otra vista (frame) para la ventana principal
    def __init__(self, master):
        super().__init__(master)

        # Configuración del frame (ventana principal)
        self.label = ctk.CTkLabel(self, text="Texto de prueba")
        self.label.pack(
            pady=20
        )  # Se añade a 20 pixeles por abajo de la ventana principal

        self.logout_button = ctk.CTkButton(
            self, text="Cerrar Sesión", command=self.quit
        )
        self.logout_button.pack(pady=20)  # Abajo del texto de prueba
