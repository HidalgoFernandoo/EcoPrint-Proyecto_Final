import customtkinter as ctk
from config.config import *
from gui.componentes import *


class PrincipalFrame(ctk.CTkFrame):  # Otra vista (frame) para la ventana principal
    def __init__(self, master):
        super().__init__(master)

        frame_main = ctk.CTkScrollableFrame(master=self, fg_color=COLOR_BG)
        frame_main.pack(fill="both", expand=True)
        
        self.label_bienvenida = crear_label(
            frame_main, text="Texto de prueba", font=("Roboto", 32, "bold"), text_color=COLOR_PRIMARIO,
        )

        self.side_frame()

    def side_frame(self):
        sideFrame = ctk.CTkFrame(
            master=self, width=240, fg_color=COLOR_PRIMARIO)
        sideFrame.place(relx=0, rely=0, relheight=1)

        self.mis_publicaciones_btn = crear_boton_sideframe(
            sideFrame, text="Inicio", selected=True, pady=(250, 0), image=crear_imagen("src/assets/home.png"),
        )

        self.publicar_btn = crear_boton_sideframe(
            sideFrame, text="Crear publicación", image=crear_imagen("src/assets/pencil-plus.png"),
        )

        self.mis_publicaciones_btn = crear_boton_sideframe(
            sideFrame, text="Mi perfil", image=crear_imagen("src/assets/user-circle.png"),
        )

        self.mis_publicaciones_btn = crear_boton_sideframe(
            sideFrame, text="Configuración", image=crear_imagen("src/assets/settings.png"),
        )

        self.logout_btn = crear_boton_sideframe(
            sideFrame, text="Cerrar sesión", command=self.quit, image=crear_imagen("src/assets/logout.png"),
        )
