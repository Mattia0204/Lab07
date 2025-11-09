import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia grafica dell'app
    - Mostra dati forniti dal MODEL
    - Intercetta azioni dell'utente e le passa al CONTROLLER
'''

class View:
    def __init__(self, page: ft.Page):
        # Riferimento alla pagina principale di Flet
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"   # Centra contenuti orizzontalmente
        self.page.theme_mode = ft.ThemeMode.DARK    # Tema scuro iniziale

        # Gestore degli alert (popup di messaggi)
        self.alert = AlertManager(page)

        # Controller: verrà impostato dall'esterno
        self._controller = None

    def show_alert(self, messaggio):
        # Wrapper per mostrare un popup tramite AlertManager
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        # Collegamento View ↔ Controller
        self._controller = controller

    def update(self):
        # Aggiorna l'interfaccia grafica
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge tutti gli elementi della UI. """

        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(
            value="Musei di Torino",
            size=38,
            weight=ft.FontWeight.BOLD
        )

        # --- Sezione 2: Filtraggio ---

        # Dropdown dei Musei
        self._dd_museo = ft.Dropdown(
            label="Museo",
            options=[],                    # Le option saranno caricate dal controller
            width=200,
            hint_text="Seleziona museo",
            on_change=self._controller.handler_dropdown_change  # callback ogni volta che cambia
        )
        # Popolazione tramite controller
        self._controller.populate_dropdown_musei()

        # Dropdown delle Epoche
        self._dd_epoca = ft.Dropdown(
            label="Epoca",
            options=[],
            width=200,
            hint_text="Seleziona epoca",
            on_change=self._controller.handler_dropdown_change
        )
        # Popolazione tramite controller
        self._controller.populate_dropdown_epoche()

        # --- Sezione 3: Lista artefatti ---

        # Bottone che forza il refresh lista artefatti
        pulsante_mostra_artefatti = ft.ElevatedButton(
            "Mostra Artefatti",
            on_click=self._controller.mostra_artefatti
        )

        # Lista visuale dove verranno mostrati gli artefatti filtrati
        self.lista_artefatti = ft.ListView(
            expand=True,     # si espande nello spazio disponibile
            spacing=5,
            padding=10,
            auto_scroll=True  # scroll automatico
        )

        # --- Toggle per tema chiaro/scuro ---
        self.toggle_cambia_tema = ft.Switch(
            label="Tema scuro",
            value=True,
            on_change=self.cambia_tema
        )

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,   # Switch Tema

            # Titolo
            self.txt_titolo,
            ft.Divider(),

            # Dropdown musei + epoche affiancati
            ft.Row(
                spacing=200,
                controls=[self._dd_museo, self._dd_epoca],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),

            # Bottone Mostra Artefatti
            ft.Row(
                spacing=200,
                controls=[pulsante_mostra_artefatti],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            # Lista risultante
            ft.Row(
                spacing=200,
                controls=[self.lista_artefatti],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),
        )

        # Abilita scroll verticale adattivo
        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Gestisce cambio tema scuro/chiaro """
        # Cambia theme_mode in base allo switch
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        )

        # Aggiorna etichetta dello switch
        self.toggle_cambia_tema.label = (
            "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        )

        self.page.update()

