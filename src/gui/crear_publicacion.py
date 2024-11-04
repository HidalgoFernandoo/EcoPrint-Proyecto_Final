import customtkinter as ctk
from config.config import *
from gui.componentes import *
from core.publicaciones import *
from core.usuarios import *

from datetime import datetime  # Para saber la hora actual


class FormularioPublicacion:
    def __init__(self, contenedor):
        self.contenedor = contenedor

        self.frame_publicar = ctk.CTkFrame(master=self.contenedor, fg_color=COLOR_BG)
        self.frame_publicar.pack(expand=True, fill="both")

        # Crea el frame del formulario y lo centra dentro de frame_publicar
        formulario_frame = ctk.CTkFrame(self.frame_publicar, fg_color=COLOR_BG)
        formulario_frame.pack(expand=True, fill="x")

        crear_label(
            formulario_frame,
            text="Crear Publicación",
            font=("Roboto", 32, "bold"),
            pady=(0, 25),
        )

        # Campo de entrada para el título
        crear_label(
            formulario_frame,
            text=" Título",
            font=("Roboto", 18, "bold"),
            pady=(20, 0),
            image=crear_imagen("src/assets/icons/title.png", size=(22, 22)),
        )
        self.entry_titulo = crear_entry(
            formulario_frame, placeholder_text="Título", width=630, pady=0, padx=190, fill="x")

        # Campo de entrada para el texto
        crear_label(
            formulario_frame,
            text=" Descripción",
            font=("Roboto", 18, "bold"),
            pady=(20, 0),
            image=crear_imagen("src/assets/icons/description.png", size=(22, 22)),
        )
        self.entry_texto = ctk.CTkTextbox(
            formulario_frame,
            font=("Roboto", 14),
            border_width=2,
            border_color=COLOR_PRIMARIO,
            height=120,
            corner_radius=8,
        )
        self.entry_texto.pack(pady=0, padx=190, fill="x")

        # Campo de entrada para la ubicación
        crear_label(
            formulario_frame,
            text=" Ubicación",
            font=("Roboto", 18, "bold"),
            pady=(20, 0),
            image=crear_imagen("src/assets/icons/location.png", size=(22, 22)),
        )
        self.entry_ubicacion = crear_entry(
            formulario_frame, placeholder_text="Ubicación", width=630, pady=0, padx=190, fill="x")

        # Campo de entrada para la fecha
        crear_label(
            formulario_frame,
            text=" Fecha del evento",
            font=("Roboto", 18, "bold"),
            pady=(20, 0),
            image=crear_imagen("src/assets/icons/calendar.png", size=(22, 22)),
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
        self.entry_fecha.pack(padx=190, pady=(0, 10), fill="x")
        CTkDatePicker(self.entry_fecha)

        # Botón de enviar
        boton_enviar = crear_boton(
            formulario_frame, text="Publicar", command=self.enviar_publicacion,
            image=crear_imagen("src/assets/icons/send.png", size=(22, 22)), fill="x", padx=190
        )

    def enviar_publicacion(self):
        # Obtener los datos de los campos de entrada
        titulo = self.entry_titulo.get()
        descripcion = self.entry_texto.get("1.0", "end").strip()
        ubicacion = self.entry_ubicacion.get()
        fecha_evento = self.entry_fecha.get()

        # Convertimos la fecha en un formato que la bd puede soportar
        fecha_evento = datetime.strptime(self.entry_fecha.get(),  "%d/%m/%Y").strftime("%Y-%m-%d")
        fecha_creacion = datetime.now().date()
        creador = f"{Usuario.usuario_actual[0]} {Usuario.usuario_actual[1]}"

        # Devolver los datos ingresados para almacenarlos.
        publicar = Publicaciones()
        publicar.subir_publicacion_a_bd(
            titulo, descripcion, ubicacion, fecha_creacion, fecha_evento, creador
        )
