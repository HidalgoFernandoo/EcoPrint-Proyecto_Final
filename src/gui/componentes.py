import customtkinter as ctk
from config.config import *
from PIL import Image
import ctkdlib


class CTkDatePicker(ctk.CTkToplevel):
    def __init__(self,
                 master,
                 height=200,
                 width=200,
                 **kwargs):

        super().__init__(takefocus=1)

        self.attach = master
        self.height = height
        self.width = width

        self.overrideredirect(True)

        self.attach._canvas.tag_bind(
            "right_parts", "<Button-1>", lambda e: self._iconify())
        self.attach._canvas.tag_bind(
            "dropdown_arrow", "<Button-1>", lambda e: self._iconify())
        self.attach.bind('<Configure>', lambda e: self._withdraw(), add="+")
        self.attach.winfo_toplevel().bind(
            '<Configure>', lambda e: self._withdraw(), add="+")

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

        self.geometry('{}x{}+{}+{}'.format(self.width,
                      self.height, x_pos, y_pos))


class MostrarPublicacion:
    def __init__(self, contenedor, titulo, descripcion, creador, fecha_creacion, fecha_evento, ubicacion):
        self.contenedor = contenedor
        self.titulo = titulo
        self.descripcion = descripcion
        self.creador = creador
        self.fecha_creacion = fecha_creacion
        self.fecha_evento = fecha_evento
        self.ubicacion = ubicacion
        self.contador_votos = 0

        self.tarjeta_frame = self.tarjeta_publicacion()

    def tarjeta_publicacion(self):
        # Crear un frame para la tarjeta de publicación
        tarjeta_frame = ctk.CTkFrame(
            master=self.contenedor,
            fg_color=COLOR_BG,
            corner_radius=15,
            border_color=COLOR_PRIMARIO_HOVER,
            border_width=2)
        tarjeta_frame.pack(padx=190, pady=20, expand=False, fill="x")

        # Titulo de la tarjeta
        titulo_frame = ctk.CTkFrame(
            tarjeta_frame, fg_color=COLOR_PRIMARIO_HOVER, corner_radius=8)
        titulo_frame.pack(pady=(0, 15), padx=0, fill="x")

        titulo_label = ctk.CTkLabel(titulo_frame, text=self.titulo, text_color=COLOR_BG,
                                    font=("Roboto", 16, "bold"), height=40)
        titulo_label.pack(expand=True)

        # Descripción de la tarjeta
        self.descripcion_label = ctk.CTkLabel(tarjeta_frame, text=self.descripcion,
                                              font=("Roboto", 14), text_color="#333333",
                                              anchor="w", justify="left")
        self.descripcion_label.pack(pady=(0, 10), padx=20, anchor="w")

        # Ajustar el wraplength dinámicamente después de renderizar el frame
        tarjeta_frame.bind("<Configure>", self.ajustar_wraplength)

        # Frame de información
        info_frame = ctk.CTkFrame(tarjeta_frame, fg_color="transparent")
        info_frame.pack(fill="x", padx=15, pady=10)

        # Creador
        creador_label = ctk.CTkLabel(info_frame, text=f" Creador: {self.creador}",
                                     font=("Roboto", 12, "bold"), compound="left", image=crear_imagen("src/assets/user-circle.png"), text_color=COLOR_PRIMARIO_HOVER)
        creador_label.grid(row=0, column=0, padx=5, pady=0, sticky="w")

        # Fecha de creación
        fecha_creacion_label = ctk.CTkLabel(info_frame, text=f" Fecha de creación: {self.fecha_creacion}",
                                            font=("Roboto", 12, "bold"), compound="left", image=crear_imagen("src/assets/calendar-user.png"), text_color=COLOR_PRIMARIO_HOVER)
        fecha_creacion_label.grid(row=1, column=0, padx=5, pady=0, sticky="w")

        # Fecha del evento
        fecha_evento_label = ctk.CTkLabel(info_frame, text=f" Fecha del evento: {self.fecha_evento}",
                                          font=("Roboto", 12, "bold"), compound="left", image=crear_imagen("src/assets/calendar-stats.png"), text_color=COLOR_PRIMARIO_HOVER)
        fecha_evento_label.grid(row=1, column=1, padx=5, pady=0, sticky="e")

        # Ubicación
        ubicacion_label = ctk.CTkLabel(info_frame, text=f" Ubicación: {self.ubicacion}",
                                       font=("Roboto", 12, "bold"), compound="left", image=crear_imagen("src/assets/map.png"), text_color=COLOR_PRIMARIO_HOVER)
        ubicacion_label.grid(row=0, column=1, padx=5, pady=0, sticky="e")

        # Ajuste de las columnas para que ocupen el ancho total
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=1)

        # Sección de votos
        votos_frame = ctk.CTkFrame(tarjeta_frame, fg_color="transparent")
        votos_frame.pack(padx=15, pady=(10, 0), fill="x")

        # Botón de voto positivo
        boton_voto_positivo = ctk.CTkButton(
            votos_frame,
            text="Votar Positivo",
            fg_color=COLOR_PRIMARIO_HOVER,
            height=34,
            text_color=COLOR_BG,
            corner_radius=8,
            font=("Roboto", 14, "bold"),
            command=lambda: self.votar(),
            compound="left",
            image=crear_imagen("src/assets/thumb-up.png"),
        )
        boton_voto_positivo.pack(side="left", fill="x", padx=5, expand=True)

        # Contador de votos
        self.contador_label = ctk.CTkLabel(
            votos_frame,
            text=f"{self.contador_votos}",
            font=("Roboto", 14, "bold"),
            height=34,
            text_color=COLOR_BG,
            corner_radius=80,
            fg_color=COLOR_PRIMARIO_HOVER,
        )
        self.contador_label.pack(side="left", padx=10)

        # Botón "Voy a participar"
        boton_participar = ctk.CTkButton(
            votos_frame,
            text="Voy a Participar",
            fg_color=COLOR_PRIMARIO_HOVER,
            text_color=COLOR_BG,
            height=34,
            corner_radius=10,
            font=("Roboto", 14, "bold"),
            command=lambda: self.participar(),
            compound="right",
            image=crear_imagen("src/assets/mood-plus.png"),
        )
        boton_participar.pack(side="left", fill="x", padx=5, expand=True)

        return tarjeta_frame

    def ajustar_wraplength(self, event):
        # Calcular el ancho de la tarjeta y ajustar el wraplength dinámicamente
        ancho_tarjeta = self.tarjeta_frame.winfo_width() - 30  # Resta márgenes
        self.descripcion_label.configure(wraplength=ancho_tarjeta)

    def votar(self):
        self.contador_votos += 1
        self.actualizar_contador()

    def participar(self):
        print("Participo en el evento.")

    def actualizar_contador(self):
        self.contador_label.configure(text=f"{self.contador_votos}")


def crear_boton(parent, text, command=None, fill="none", padx=50, width=350, pady=20, **kwargs):
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
        **kwargs
    )
    boton.pack(pady=pady, padx=padx, fill=fill,)

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


def crear_entry(parent, placeholder_text="", padx=0, fill="none", width=350, pady=10, **kwargs):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder_text,
        width=width,
        height=40,
        corner_radius=8,
        font=("Roboto", 14),
        border_color=COLOR_PRIMARIO,
        **kwargs
    )
    entry.pack(pady=pady, padx=padx, fill=fill)

    return entry


def crear_label(parent, text="", pady=10, font=("Roboto", 14), **kwargs):
    label = ctk.CTkLabel(
        parent,
        text=text,
        width=700,
        height=40,
        wraplength=500,
        anchor="w",
        corner_radius=8,
        font=font,
        text_color=COLOR_PRIMARIO,
        compound="left",
        **kwargs
    )
    label.pack(pady=pady, padx=170, fill="x")

    return label
