import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def populate_dropdown_epoche(self):
        epoche = self._model.get_epoche()
        self._view._dd_epoca.options = [ft.dropdown.Option(e) for e in epoche]
        self._view.update()

    def populate_dropdown_musei(self):
        musei = self._model.get_musei()
        self._view._dd_museo.options = [ft.dropdown.Option(m) for m in musei]
        self._view.update()

    # CALLBACKS DROPDOWN
    def handler_dropdown_change(self, e):
        self.museo_selezionato = self._view._dd_museo.value
        self.epoca_selezionata = self._view._dd_epoca.value
        self.mostra_artefatti(None)

    def mostra_artefatti(self, e):
        museo = self._view._dd_museo.value
        epoca = self._view._dd_epoca.value
        artefatti = self._model.get_artefatti_filtrati(museo, epoca)
        self._view.lista_artefatti.controls.clear()
        for a in artefatti:
            self._view.lista_artefatti.controls.append(ft.Text(str(a)))
        self._view.update()


