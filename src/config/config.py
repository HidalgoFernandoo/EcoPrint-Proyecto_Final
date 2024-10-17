# En este archivo van las constantes, ajustes generales.

import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


def centrar_ventana(ventana, ancho_ventana, alto_ventana):
    ancho_pantalla = ventana.winfo_screenwidth()  # Obtiene el ancho de la pantalla
    alto_pantalla = ventana.winfo_screenheight()  # Obtiene el alto de la pantalla

    # Ajustamos las coordenadas
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")


COLOR_PRIMARIO = "#0c955a"
COLOR_PRIMARIO_HOVER = "#0a7e4c"
COLOR_BG = "#faf3e9"




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
        formulario_frame, text="Crear Publicación", font=("Roboto", 24, "bold")
    )
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Campo de entrada para el título de la publicación
    entry_titulo = crear_entry(
        formulario_frame, placeholder_text="Título"
    )
    entry_titulo.grid(row=1, column=0, columnspan=2, pady=10)

    # Campo de entrada para el texto de la publicación
    entry_texto = ctk.CTkEntry(
        formulario_frame, placeholder_text="Texto", height=100, width=350
    )
    entry_texto.grid(row=2, column=0, columnspan=2, pady=10)

    # Campo de entrada para la ubicación de la publicación
    entry_ubicacion = crear_entry(
        formulario_frame, placeholder_text="Ubicación"
    )
    entry_ubicacion.grid(row=3, column=0, columnspan=2, pady=10)

    # Botón de enviar
    boton_enviar = crear_boton(
        formulario_frame, text="Enviar", command=lambda: self.enviar_publicacion(entry_titulo, entry_texto, entry_ubicacion)
    )
    boton_enviar.grid(row=4, column=0, columnspan=2, pady=(10, 20))