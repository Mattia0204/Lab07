import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Fa da intermediario tra MODELLO e VIEW
    - Contiene la logica dell’applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        # Salvo i riferimenti a modello e vista
        self._model = model
        self._view = view

        # Variabili che terranno le selezioni fatte nei dropdown
        self.museo_selezionato = None
        self.epoca_selezionata = None

    #       POPOLAMENTO DROPDOWN
    def populate_dropdown_epoche(self):
        epoche = []
        epoche.append(" ")
        # Aggiungo l’opzione vuota in cima: significa “nessun filtro”

        lista_epoche = self._model.get_epoche()
        # Chiedo al modello la lista delle epoche

        for epoca in lista_epoche:
            epoche.append(epoca)
            # Le aggiungo al dropdown

        # Aggiorno realmente il dropdown nella view
        self._view._dd_epoca.options = [ft.dropdown.Option(e) for e in epoche]
        self._view.update()

    def populate_dropdown_musei(self):
        musei = []
        musei.append(" ")
        # Anche qui prima opzione vuota = nessun filtro

        lista_musei = self._model.get_musei()
        # Ottengo dal modello i nomi dei musei

        for museo in lista_musei:
            musei.append(museo)

        # Aggiorno dropdown nella view
        self._view._dd_museo.options = [ft.dropdown.Option(m) for m in musei]
        self._view.update()

    #      CALLBACK DEI DROPDOWN
    def handler_dropdown_change(self, e):
        # Ogni volta che cambia uno dei due dropdown,
        # salvo i valori correnti
        self.museo_selezionato = self._view._dd_museo.value
        self.epoca_selezionata = self._view._dd_epoca.value

        # E aggiorno la lista artefatti filtrata
        self.mostra_artefatti(None)

    #     MOSTRA GLI ARTEFATTI
    def mostra_artefatti(self, e):
        # Leggo le scelte contenute nei dropdown
        museo = self._view._dd_museo.value
        epoca = self._view._dd_epoca.value

        # Chiedo al modello la lista filtrata
        artefatti = self._model.get_artefatti_filtrati(museo, epoca)
        if not artefatti:
            # Svuoto la lista visibile nella view
            self._view.lista_artefatti.controls.clear()

            #messaggio di aller quando filtri non producono risultato tra gli artefatti
            self._view.alert.show_alert("I filtri applicati non trovano artefatti presenti nel database")

        else:
            # Svuoto la lista visibile nella view
            self._view.lista_artefatti.controls.clear()

            # Inserisco un elemento testuale per ogni artefatto filtrato
            for a in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(str(a)))

            # Aggiorno la view
            self._view.update()
