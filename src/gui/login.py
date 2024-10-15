import customtkinter as ctk
from core.usuarios import *


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, frame_cambiar):
        super().__init__(master)

        # Guardamos la función para cambiar de frame
        self.frame_cambiar = frame_cambiar

        # Configuración del frame (ventana de inicio de sesión)
        self.label = ctk.CTkLabel(self, text="Iniciar Sesión")
        self.label.pack(pady=20)

        self.usuario_correo = ctk.CTkEntry(self, placeholder_text="Correo")
        self.usuario_correo.pack(pady=10)

        self.__usuario_contrasena = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*"
        )
        self.__usuario_contrasena.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self, text="Iniciar Sesión", command=self.login
        )
        self.login_button.pack(pady=20)

        self.label_registrar = ctk.CTkLabel(
            self,
            text="¿No tienes una cuenta? ¡Registrate!",
            wraplength=210,
            font=("", 16, "bold"),
        )
        self.label_registrar.pack(pady=(90, 10), padx=20, fill="x")
        self.registrar_button = ctk.CTkButton(
            self, text="Registrarse", command=self.registrarse
        )
        self.registrar_button.pack(pady=(0, 10), padx=0)

    def login(self):
        if not self.usuario_correo.get():
            # FALTA label "Debes ingresar un correo"
            return
        if not self.__usuario_contrasena.get():
            # FALTA label "Debes ingresar una contrasena"
            return

        usuario_logeado = Usuario(
            self.usuario_correo.get(), self.__usuario_contrasena.get()
        )

        # Verificar usuario
        if not usuario_logeado.verificar_usuario(
            self.usuario_correo.get(), self.__usuario_contrasena.get()
        ):
            # FALTA label "Usuario o contrasena incorrecto"
            return
        self.frame_cambiar("principal")

    def registrarse(self):
        self.frame_cambiar("registrar")
