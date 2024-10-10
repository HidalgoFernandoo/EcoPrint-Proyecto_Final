# En este archivo van las constantes, ajustes generales.

import customtkinter as ctk


def centrar_ventana(ventana, ancho_ventana, alto_ventana):
    ancho_pantalla = ventana.winfo_screenwidth()  # Obtiene el ancho de la pantalla
    alto_pantalla = ventana.winfo_screenheight()  # Obtiene el alto de la pantalla

    # Ajustamos las coordenadas
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
