import customtkinter as ctk
from gui.terminos_condiciones import Terminos_CondicionesFrame


class RegistroFrame(ctk.CTkFrame):
    def __init__(self, master, frame_cambiar):
        super().__init__(master)
        self.frame_cambiar = frame_cambiar

        self.label = ctk.CTkLabel(self, text="Registrarse")
        self.label.pack(pady=20)

        self.correo = ctk.CTkEntry(self, placeholder_text="Correo electrónico")
        self.correo.pack(pady=(0, 10), padx=0)

        self.usuario_nombre = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.usuario_nombre.pack(pady=(0, 10), padx=0)

        self.usuario_contrasena = ctk.CTkEntry(
            self, show="*", placeholder_text="Contraseña"
        )
        self.usuario_contrasena.pack(pady=(0, 10), padx=0)

        self.registrar_button = ctk.CTkButton(self, text="Registrarse")
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
