import customtkinter as ctk
from gui.terminos_condiciones import Terminos_CondicionesFrame
from core.usuarios import *


class RegistroFrame(ctk.CTkFrame):
    def __init__(self, master, frame_cambiar):
        super().__init__(master)
        self.frame_cambiar = frame_cambiar

        self.label = ctk.CTkLabel(self, text="Registrarse")
        self.label.pack(pady=20)

        self.usuario_correo = ctk.CTkEntry(self, placeholder_text="Correo electrónico")
        self.usuario_correo.pack(pady=(0, 10), padx=0)

        self.usuario_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.usuario_nombre.pack(pady=(0, 10), padx=0)

        self.usuario_apellido = ctk.CTkEntry(self, placeholder_text="Apellido")
        self.usuario_apellido.pack(pady=(0, 10), padx=0)

        self.__usuario_contrasena = ctk.CTkEntry(
            self, show="*", placeholder_text="Contraseña"
        )
        self.__usuario_contrasena.pack(pady=(0, 10), padx=0)

        self.registrar_button = ctk.CTkButton(
            self, text="Registrarse", command=self.verificar_campos
        )
        self.registrar_button.pack(pady=(0, 10), padx=0)

        self.frameTerminos = ctk.CTkFrame(self, fg_color="transparent")
        self.frameTerminos.pack(pady=(0, 10), padx=105, fill="x")

        self.terminosCheckbox = ctk.CTkCheckBox(
            self, width=0, text="", onvalue="on", offvalue="off"
        )
        self.terminosCheckbox.pack(pady=0, padx=0, side="left")

        self.terminos_button = ctk.CTkButton(
            self,
            width=310,
            fg_color="transparent",
            text="Acepto los términos y condiciones",
            anchor="w",
            command=self.ver_terminos,
        )
        self.terminos_button.pack(pady=0, padx=0, fill="x", side="left")

        self.volver_login = ctk.CTkButton(
            self, text="volver", command=self.volver_login
        )
        self.volver_login.pack(pady=(0, 10), padx=0)

    def ver_terminos(self):
        Terminos_CondicionesFrame(self)

    def volver_login(self):
        self.frame_cambiar("login")

    def verificar_campos(self):
        # Validar campos vacíos
        if not self.usuario_correo.get() or "@" not in self.usuario_correo.get():
            # FALTA label debes ingresar un correo válido
            # FALTA agregar para verificar que el CORREO ELECTRÓNICO es válido
            return
        if (
            not self.__usuario_contrasena.get()
            or len(self.__usuario_contrasena.get()) < 10
        ):
            # FALTA label debes ingresar una contrasena válida, recuerda que debe tener al menos 10 caracteres
            return
        if not self.usuario_nombre.get():
            # FALTA label debes ingresar un nombre
            return
        if not self.usuario_apellido.get():
            # FALTA label debes ingresar un apellido
            return
        if not self.terminosCheckbox.get() == "on":
            # Falta label debes aceptar los terminos y condiciones
            return

        # Si los campos son correctos, registrar usuario
        usuario = Usuario(
            self.usuario_correo.get(), self.__usuario_contrasena.get()
        )
        usuario.registrar_usuario(
            self.usuario_nombre.get(),
            self.usuario_apellido.get(),
        )
