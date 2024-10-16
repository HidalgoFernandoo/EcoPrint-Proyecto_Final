import customtkinter as ctk
from config.config import *


def crear_boton(parent, text, command=None, pady=20, **kwargs):
    boton = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=350,
        height=40,
        corner_radius=8,
        font=("", 16, "bold"),
        fg_color=COLOR_PRIMARIO,
        hover_color=COLOR_PRIMARIO_HOVER,
        **kwargs
    )
    boton.pack(pady=pady)

    return boton


def crear_entry(parent, placeholder_text="", pady=10, **kwargs):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder_text,
        width=350,
        height=40,
        corner_radius=8,
        border_color=COLOR_PRIMARIO,
        **kwargs
    )
    entry.pack(pady=pady)

    return entry


def crear_label(parent, text="", pady=10, **kwargs):
    label = ctk.CTkLabel(
        parent,
        text=text,
        width=350,
        height=40,
        wraplength=500,
        corner_radius=8,
        **kwargs
    )
    label.pack(pady=pady)

    return label
