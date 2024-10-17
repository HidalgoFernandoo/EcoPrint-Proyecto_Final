import customtkinter as ctk
from config.config import *
from PIL import Image


def crear_boton(parent, text, command=None, grid=False, pady=20, **kwargs):
    boton = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=350,
        height=40,
        corner_radius=8,
        font=("Roboto", 14, "bold"),
        fg_color=COLOR_PRIMARIO,
        hover_color=COLOR_PRIMARIO_HOVER,
        **kwargs
    )
    
    if grid:
        pass
    else:
        boton.pack(pady=pady, padx=50)

    return boton


def crear_boton_sideframe(parent, text, command=None, pady=5, selected=False, **kwargs):
    boton = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=210,
        height=40,
        corner_radius=8,
        font=("Roboto", 15, "bold"),
        hover=False,
        compound="left",
        fg_color=COLOR_PRIMARIO_HOVER if selected else COLOR_PRIMARIO,
        text_color=COLOR_BG,
        anchor="w",
        **kwargs
    )
    boton.pack(pady=pady, padx=30, fill="x")

    return boton


def crear_imagen(route, size=(20, 20)):
    return ctk.CTkImage(Image.open(route), size=size)


def crear_entry(parent, placeholder_text="", grid=False, pady=10, **kwargs):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder_text,
        width=350,
        height=40,
        corner_radius=8,
        font=("Roboto", 14),
        border_color=COLOR_PRIMARIO,
        **kwargs
    )
    
    if grid:
        pass
    else:
        entry.pack(pady=pady)

    return entry


def crear_label(parent, text="", pady=10, grid=False, font=("Roboto", 14), **kwargs):
    label = ctk.CTkLabel(
        parent,
        text=text,
        width=850,
        height=40,
        wraplength=500,
        anchor="w",
        corner_radius=8,
        font=font,
        text_color=COLOR_PRIMARIO,
        compound="left",
        **kwargs
    )
    
    if grid:
        pass
    else:
        label.pack(pady=pady)

    return label
