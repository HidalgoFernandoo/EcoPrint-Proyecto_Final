import customtkinter as ctk
from config.config import *
from PIL import Image
import ctkdlib


class CTkDatePicker(ctk.CTkToplevel):
    def __init__(self, master, height=200, width=200, **kwargs):

        super().__init__(takefocus=1)

        self.attach = master
        self.height = height
        self.width = width

        self.overrideredirect(True)

        self.attach._canvas.tag_bind(
            "right_parts", "<Button-1>", lambda e: self._iconify()
        )
        self.attach._canvas.tag_bind(
            "dropdown_arrow", "<Button-1>", lambda e: self._iconify()
        )
        self.attach.bind("<Configure>", lambda e: self._withdraw(), add="+")
        self.attach.winfo_toplevel().bind(
            "<Configure>", lambda e: self._withdraw(), add="+"
        )

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        self.calendar = ctkdlib.CTkCalendar(
            self.frame, command=self._pass, **kwargs)
        self.calendar.pack(expand=True, fill="both")

        self.update_idletasks()
        self.deiconify()
        self.withdraw()

        date = self.calendar.current_date()
        self.attach.set(f"{date[0]}/{date[1]}/{date[2]}")

        self.hide = True

    def _iconify(self):
        if self.attach.cget("state") == "disabled":
            return

        if self.winfo_ismapped():
            self.hide = False

        if self.hide:
            self.deiconify()
            self.hide = False
            self.place_dropdown()
        else:
            self.withdraw()
            self.hide = True

    def _withdraw(self):
        if self.winfo_ismapped():
            self.withdraw()
            self.hide = True

    def _pass(self, date):
        self.attach.set(f"{date[0]}/{date[1]}/{date[2]}")
        self._withdraw()

    def place_dropdown(self):
        x_pos = self.attach.winfo_rootx()
        y_pos = self.attach.winfo_rooty() + self.attach.winfo_reqheight()

        self.geometry("{}x{}+{}+{}".format(self.width,
                      self.height, x_pos, y_pos))


def crear_boton(
    parent, text, command=None, fill="none", padx=50, width=350, pady=20, **kwargs
):
    boton = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        height=40,
        corner_radius=8,
        font=("Roboto", 15, "bold"),
        compound="right",
        fg_color=COLOR_PRIMARIO,
        hover_color=COLOR_PRIMARIO_HOVER,
        **kwargs,
    )
    boton.pack(
        pady=pady,
        padx=padx,
        fill=fill,
    )

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
        **kwargs,
    )
    boton.pack(pady=pady, padx=30, fill="x")

    return boton


def crear_imagen(route, size=(20, 20)):
    return ctk.CTkImage(Image.open(route), size=size)


def crear_entry(
    parent, placeholder_text="", padx=0, fill="none", width=350, pady=10, **kwargs
):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder_text,
        width=width,
        height=40,
        corner_radius=8,
        font=("Roboto", 14),
        border_color=COLOR_PRIMARIO,
        **kwargs,
    )
    entry.pack(pady=pady, padx=padx, fill=fill)

    return entry


def crear_label(parent, text="", pady=10, anchor="w", padx=170, text_color=COLOR_PRIMARIO, font=("Roboto", 14), **kwargs):
    label = ctk.CTkLabel(
        parent,
        text=text,
        width=700,
        height=40,
        wraplength=500,
        anchor=anchor,
        corner_radius=8,
        font=font,
        text_color=text_color,
        compound="left",
        **kwargs,
    )
    label.pack(pady=pady, padx=padx, fill="x")

    return label


def crear_stat(parent, titulo, contador, padx=0):
    label_stat = ctk.CTkLabel(
        parent,
        text=f"{titulo}\n {contador}",
        height=40,
        width=150,
        anchor="center",
        corner_radius=8,
        font=("Roboto", 18, "bold"),
        text_color=COLOR_BG,
        fg_color=COLOR_PRIMARIO,
    )

    # Asegurar que el label se expanda adecuadamente
    label_stat.pack(side="left", expand=True, fill="x", padx=padx, pady=0, ipady=20, ipadx=20)

    return label_stat
