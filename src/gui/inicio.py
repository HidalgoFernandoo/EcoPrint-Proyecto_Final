import customtkinter as ctk
from config.config import *
from gui.componentes import *


class InicioFrame(ctk.CTkFrame):
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

        # Centra el contenido del sideFrame
        centrar_frame = ctk.CTkFrame(sideFrame, fg_color=COLOR_PRIMARIO)
        centrar_frame.pack(expand=True)

        ctk.CTkLabel(centrar_frame, text="EcoPrint", font=("Roboto", 32, "bold"),
                     text_color=COLOR_BG, width=210).pack(pady=0)

        ctk.CTkLabel(centrar_frame, text="", image=crear_imagen(
            "src/assets/eco.png", size=(220, 220))).pack(pady=50)

        # Creación de botones en el sideFrame con el estado de selección inicial
        self.botones_sideframe["inicio"] = crear_boton_sideframe(
            centrar_frame, text="Inicio", command=self.inicio, pady=0,
            image=crear_imagen("src/assets/home.png")
        )

        self.botones_sideframe["crear_publicacion"] = crear_boton_sideframe(
            centrar_frame, text="Crear publicación", command=self.crear_publicacion,
            image=crear_imagen("src/assets/pencil-plus.png")
        )

        self.botones_sideframe["perfil"] = crear_boton_sideframe(
            centrar_frame, text="Mi perfil", command=self.perfil,
            image=crear_imagen("src/assets/user-circle.png")
        )

        self.botones_sideframe["configuracion"] = crear_boton_sideframe(
            centrar_frame, text="Configuración", command=self.configuraciones,
            image=crear_imagen("src/assets/settings.png")
        )

        self.botones_sideframe["cerrar_sesion"] = crear_boton_sideframe(
            centrar_frame, text="Cerrar sesión", command=self.cerrar_sesion,
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

        self.cambiar_contenido(frame_inicio, "inicio")

    def crear_publicacion(self):
        frame_publicar = ctk.CTkFrame(master=self, fg_color=COLOR_BG)
        frame_publicar.pack(expand=True, fill="both")

        self.cambiar_contenido(frame_publicar, "crear_publicacion")

        # Crea el frame del formulario y lo centra dentro de frame_publicar
        formulario_frame = ctk.CTkFrame(frame_publicar, fg_color=COLOR_BG)
        formulario_frame.pack(expand=True)

        crear_label(
            formulario_frame, text="Crear Publicación", font=("Roboto", 32, "bold"), pady=(0, 25),
        )

        # Campo de entrada para el título
        crear_label(
            formulario_frame, text=" Título", font=("Roboto", 18, "bold"), pady=(20, 0), image=crear_imagen("src/assets/title.png", size=(22, 22)),
        )
        self.entry_titulo = crear_entry(
            formulario_frame, placeholder_text="Título", width=630, pady=0)

        # Campo de entrada para el texto
        crear_label(
            formulario_frame, text=" Descripción", font=("Roboto", 18, "bold"), pady=(20, 0), image=crear_imagen("src/assets/description.png", size=(22, 22)),
        )
        self.entry_texto = ctk.CTkTextbox(
            formulario_frame,
            font=("Roboto", 14),
            border_width=2,
            border_color=COLOR_PRIMARIO,
            height=120,
            width=630,
            corner_radius=8,
        )
        self.entry_texto.pack(pady=0)

        # Campo de entrada para la ubicación
        crear_label(
            formulario_frame, text=" Ubicación", font=("Roboto", 18, "bold"), pady=(20, 0), image=crear_imagen("src/assets/location.png", size=(22, 22)),
        )
        self.entry_ubicacion = crear_entry(
            formulario_frame, placeholder_text="Ubicación", width=630, pady=0)

        # Campo de entrada para la fecha
        crear_label(
            formulario_frame, text=" Fecha del evento", font=("Roboto", 18, "bold"), pady=(20, 0), image=crear_imagen("src/assets/calendar.png", size=(22, 22)),
        )

        self.entry_fecha = ctk.CTkComboBox(
            formulario_frame,
            width=630,
            height=40,
            corner_radius=8,
            font=("Roboto", 14),
            border_color=COLOR_PRIMARIO,
            button_color=COLOR_PRIMARIO,
            button_hover_color=COLOR_PRIMARIO_HOVER,
        )
        self.entry_fecha.pack(padx=10, pady=(0, 10))
        CTkDatePicker(self.entry_fecha)

        # Botón de enviar
        boton_enviar = crear_boton(
            formulario_frame, text="Publicar", width=630, command=self.enviar_publicacion, image=crear_imagen("src/assets/send.png", size=(22, 22)),
        )

    def enviar_publicacion(self):
        # Obtener los datos de los campos de entrada
        titulo = self.entry_titulo.get()
        descripcion = self.entry_texto.get("1.0", "end").strip()
        ubicacion = self.entry_ubicacion.get()
        fecha = self.entry_fecha.get()

        print(f"Título: {titulo}")
        print(f"Descripción: {descripcion}")
        print(f"Ubicación: {ubicacion}")
        print(f"Fecha del evento: {fecha}")

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
