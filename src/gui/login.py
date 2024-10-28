import customtkinter as ctk
from core.usuarios import *
from config.config import *
from gui.componentes import *


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, frame_cambiar):
        super().__init__(master)

        # Guardamos la función para cambiar de frame
        self.frame_cambiar = frame_cambiar

        self.label_bienvenida = crear_label(
            self,
            text="¡Bienvenido a EcoPrint!",
            font=("Roboto", 32, "bold"),
            pady=(100, 50),
        )

        self.label_login = crear_label(
            self, text="Inicia Sesión", font=("Roboto", 18, "bold")
        )

        self.usuario_correo = crear_entry(self, placeholder_text="Correo electrónico")

        self.__usuario_contrasena = crear_entry(
            self, placeholder_text="Contraseña", show="*"
        )

        self.login_button = crear_boton(self, text="Iniciar Sesión", command=self.login)

        self.label_registrar = crear_label(
            self,
            text="¿No tienes una cuenta? ¡Registrate!",
            font=("Roboto", 18, "bold"),
            pady=(90, 0),
        )

        self.registrar_button = crear_boton(
            self, text="Registrarse", command=self.registrarse
        )

    def login(self):
        if not self.usuario_correo.get():
            # FALTA label "Debes ingresar un correo"
            return
        if not self.__usuario_contrasena.get():
            # FALTA label "Debes ingresar una contrasena"
            return

        logear_usuario = Usuario(
            self.usuario_correo.get(), self.__usuario_contrasena.get()
        )

        # Verificar usuario
        if not logear_usuario.verificar_usuario(
            self.usuario_correo.get(), self.__usuario_contrasena.get()
        ):
            # FALTA label "Usuario o contrasena incorrecto"
            return
        self.frame_cambiar("inicio")

    def registrarse(self):
        self.frame_cambiar("registrar")
