from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str, epoca: str):
        artefatti = self._artefatto_dao.read_all_artefattos()
        if museo is None and epoca is None:
            return artefatti
        artefatti_filtrati = []
        musei = self._museo_dao.read_all_museums()
        id_museo = None

        for m in musei:
            if m.nome == museo:
                id_museo = m.id

        for artefatto in artefatti:
            if museo is None or epoca is None:
                if artefatto.epoca == epoca or artefatto.id_museo == id_museo:
                    artefatti_filtrati.append(artefatto)
            else:
                if artefatto.epoca == epoca and artefatto.id_museo == id_museo:
                    artefatti_filtrati.append(artefatto)
        return artefatti_filtrati

    def get_epoche(self):
        artefatti = self._artefatto_dao.read_all_artefattos()
        if artefatti is None:
            return []
        epoche = []
        for artefatto in artefatti:
            if artefatto.epoca not in epoche:
                epoche.append(artefatto.epoca)
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        musei = self._museo_dao.read_all_museums()
        if musei is None:
            return []
        nomi_musei = []
        for museo in musei:
            if museo.nome not in nomi_musei:
                nomi_musei.append(museo.nome)
        return nomi_musei




