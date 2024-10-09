import customtkinter as ctk


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, frame_cambiar):
        super().__init__(master)

        # Guardamos la función para cambiar de frame
        self.frame_cambiar = frame_cambiar

        # Configuración del frame (ventana de inicio de sesión)
        self.label = ctk.CTkLabel(self, text="Iniciar Sesión")
        self.label.pack(pady=20)

        self.usuario_nombre = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.usuario_nombre.pack(pady=10)

        self.usuario_contrasena = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*"
        )
        self.usuario_contrasena.pack(pady=10)

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
        # Aca falta la lógica de validación del inicio de sesión (con MySQL)
        # If validación es exitosa, cambia a la ventana principal
        self.frame_cambiar("principal")

    def registrarse(self):
        self.frame_cambiar("registrar")
