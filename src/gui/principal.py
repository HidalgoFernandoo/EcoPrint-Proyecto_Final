import customtkinter as ctk
from config.config import *
from gui.componentes import *


class PrincipalFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.frame_contenido = None
        self.botones_sideframe = {}  # Diccionario para almacenar botones del sideFrame
        self.side_frame()
        self.inicio()  # Carga el frame de inicio por defecto

    def side_frame(self):
        sideFrame = ctk.CTkFrame(
            master=self, width=240, fg_color=COLOR_PRIMARIO)
        sideFrame.pack(side="left", fill="y")

        # Creación de botones en el sideFrame con el estado de selección inicial
        self.botones_sideframe["inicio"] = crear_boton_sideframe(
            sideFrame, text="Inicio", command=self.inicio, pady=(250, 0),
            image=crear_imagen("src/assets/home.png")
        )

        self.botones_sideframe["crear_publicacion"] = crear_boton_sideframe(
            sideFrame, text="Crear publicación", command=self.crear_publicacion,
            image=crear_imagen("src/assets/pencil-plus.png")
        )

        self.botones_sideframe["perfil"] = crear_boton_sideframe(
            sideFrame, text="Mi perfil", command=self.perfil,
            image=crear_imagen("src/assets/user-circle.png")
        )

        self.botones_sideframe["configuracion"] = crear_boton_sideframe(
            sideFrame, text="Configuración", command=self.configuraciones,
            image=crear_imagen("src/assets/settings.png")
        )

        self.botones_sideframe["cerrar_sesion"] = crear_boton_sideframe(
            sideFrame, text="Cerrar sesión", command=self.cerrar_sesion,
            image=crear_imagen("src/assets/logout.png")
        )

    def actualizar_estado_botones(self, boton_activo):
        # Actualiza el color del botón activo y resetea los demás
        for nombre, boton in self.botones_sideframe.items():
            if nombre == boton_activo:
                # Fondo verde oscuro para el botón activo
                boton.configure(fg_color=COLOR_PRIMARIO_HOVER)
            else:
                # Fondo predeterminado para los demás botones
                boton.configure(fg_color=COLOR_PRIMARIO)

    def cambiar_contenido(self, nuevo_frame, boton_activo):
        # Cambia el contenido principal y actualiza el estado del botón activo
        if self.frame_contenido:
            self.frame_contenido.pack_forget()  # Oculta el frame anterior

        self.actualizar_estado_botones(boton_activo)
        self.frame_contenido = nuevo_frame
        self.frame_contenido.pack(side="left", fill="both", expand=True)

    # ------------------------------------- FRAMES DE CONTENIDO -------------------------------------
    def inicio(self):
        frame_inicio = ctk.CTkScrollableFrame(master=self, fg_color=COLOR_BG)
        crear_label(
            frame_inicio, text="Inicio", font=("Roboto", 32, "bold"), pady=(30, 10),
        )

        self.btn = crear_boton(
            frame_inicio, text="Registrarse",
        )

        self.cambiar_contenido(frame_inicio, "inicio")

    def crear_publicacion(self):
        frame_publicar = ctk.CTkFrame(master=self, fg_color=COLOR_BG)
        crear_label(
            frame_publicar, text="Crear publicación", font=("Roboto", 32, "bold"), pady=(30, 10),
        )
        self.cambiar_contenido(frame_publicar, "crear_publicacion")

                
        # Configurar grid del frame principal para centrar el formulario
        frame_publicar.grid_columnconfigure(0, weight=1)  # Centrado en horizontal
        frame_publicar.grid_rowconfigure(0, weight=1)     # Centrado en vertical
        frame_publicar.grid_rowconfigure(6, weight=1)     # Espacio debajo del formulario

        # Frame del formulario
        formulario_frame = ctk.CTkFrame(frame_publicar)
        formulario_frame.grid(row=1, column=0, padx=20, pady=20)
        
        # Título del formulario
        label_titulo = crear_label(
            formulario_frame, text="Crear Publicación", font=("Roboto", 24, "bold"), grid=True,
        )
        label_titulo.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Campo de entrada para el título de la publicación
        entry_titulo = crear_entry(
            formulario_frame, placeholder_text="Título", grid=True,
        )
        entry_titulo.grid(row=1, column=0, columnspan=2, pady=10)

        # Campo de entrada para el texto de la publicación
        entry_texto = ctk.CTkEntry(
            formulario_frame, placeholder_text="Texto", height=100, width=350, grid=True
        )
        entry_texto.grid(row=2, column=0, columnspan=2, pady=10)

        # Campo de entrada para la ubicación de la publicación
        entry_ubicacion = crear_entry(
            formulario_frame, placeholder_text="Ubicación", grid=True
        )
        entry_ubicacion.grid(row=3, column=0, columnspan=2, pady=10)

        # Botón de enviar
        boton_enviar = crear_boton(
            formulario_frame, text="Enviar", command=lambda: self.enviar_publicacion(entry_titulo, entry_texto, entry_ubicacion), grid=True
        )
        boton_enviar.grid(row=4, column=0, columnspan=2, pady=(10, 20))


        # # Campo de entrada para el título de la publicación
        # crear_label(
        #     frame_publicar, text=" Título", font=("Roboto", 18, "bold"), image=crear_imagen("src/assets/title.png", size=(22, 22)),
        # )
        # self.entry_titulo = crear_entry(
        #     frame_publicar, placeholder_text="Título"
        # )

        # # Campo de entrada para el texto de la publicación
        # crear_label(
        #     frame_publicar, text=" Descripción", font=("Roboto", 18, "bold"), image=crear_imagen("src/assets/description.png", size=(22, 22)),
        # )
        # self.entry_texto = crear_entry(
        #     frame_publicar, placeholder_text="Texto",
        # )

        # # Campo de entrada para la ubicación de la publicación
        # crear_label(
        #     frame_publicar, text=" Ubicación", font=("Roboto", 18, "bold"), image=crear_imagen("src/assets/location.png", size=(22, 22)),
        # )
        # self.entry_ubicacion = crear_entry(
        #     frame_publicar, placeholder_text="Ubicación"
        # )

        # # Botón de enviar
        # crear_boton(
        #     frame_publicar, text="Enviar"
        # )
        
        
        

    def perfil(self):
        frame_perfil = ctk.CTkFrame(master=self, fg_color=COLOR_BG)
        crear_label(
            frame_perfil, text="Mi perfil", font=("Roboto", 32, "bold"), pady=(30, 10),
        )
        self.cambiar_contenido(frame_perfil, "perfil")

    def configuraciones(self):
        frame_configuracion = ctk.CTkFrame(
            master=self, fg_color=COLOR_BG)
        crear_label(
            frame_configuracion, text="Configuración", font=("Roboto", 32, "bold"), pady=(30, 10),
        )
        self.cambiar_contenido(frame_configuracion, "configuracion")

    def cerrar_sesion(self):
        self.quit()
