from database.museo_DAO import MuseoDAO  # importa il DAO per accedere ai dati dei musei
from database.artefatto_DAO import ArtefattoDAO  # importa il DAO per accedere ai dati degli artefatti

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:  # definizione della classe Model
    def __init__(self):  # costruttore del model
        self._museo_dao = MuseoDAO()  # istanzia il DAO dei musei
        self._artefatto_dao = ArtefattoDAO()  # istanzia il DAO degli artefatti

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str, epoca: str):  # metodo per filtrare gli artefatti
        artefatti = self._artefatto_dao.read_all_artefattos()  # legge tutti gli artefatti dal DB
        if museo == " ":  # se il dropdown ha l'opzione vuota (stringa con spazio)
            museo=None  # la considera come assenza di filtro
        if epoca == " ":  # stessa cosa per l'epoca
            epoca=None  # reset del filtro epoca
        if museo is None and epoca is None:  # se nessun filtro è attivo
            return artefatti  # restituisce tutti gli artefatti
        artefatti_filtrati = []  # lista che conterrà i risultati filtrati
        musei = self._museo_dao.read_all_museums()  # legge tutti i musei dal DB
        id_museo = None  # inizializza la variabile che conterrà l'id del museo selezionato

        for m in musei:  # cicla su tutti i musei
            if m.nome == museo:  # confronta il nome selezionato con il nome nel DB
                id_museo = m.id  # salva l'id corrispondente

        for artefatto in artefatti:  # cicla sugli artefatti letti dal DB
            if museo is None or epoca is None:  # se è attivo solo uno dei due filtri
                if artefatto.epoca == epoca or artefatto.id_museo == id_museo:  # filtro OR
                    artefatti_filtrati.append(artefatto)  # aggiunge l'artefatto filtrato
            else:  # se entrambi i filtri sono attivi
                if artefatto.epoca == epoca and artefatto.id_museo == id_museo:  # filtro AND
                    artefatti_filtrati.append(artefatto)  # aggiunge l'artefatto filtrato
        return artefatti_filtrati  # restituisce la lista filtrata

    def get_epoche(self):  # metodo per ottenere tutte le epoche disponibili
        artefatti = self._artefatto_dao.read_all_artefattos()  # legge tutti gli artefatti dal DB
        if artefatti is None:  # se errore di connessione
            return []  # restituisce lista vuota
        epoche = []  # lista che conterrà epoche uniche
        for artefatto in artefatti:  # cicla su tutti gli artefatti
            if artefatto.epoca not in epoche:  # evita duplicati
                epoche.append(artefatto.epoca)  # aggiunge l'epoca
        return epoche  # restituisce epoche uniche

    # --- MUSEI ---
    def get_musei(self):  # metodo per ottenere tutti i musei
        musei = self._museo_dao.read_all_museums()  # legge i musei dal DB
        if musei is None:  # se errore di connessione
            return []  # restituisce lista vuota
        nomi_musei = []  # lista che conterrà i nomi dei musei
        for museo in musei:  # cicla sui musei
            if museo.nome not in nomi_musei:  # evita duplicati
                nomi_musei.append(museo.nome)  # aggiunge il nome
        return nomi_musei  # restituisce tutti i nomi dei musei





