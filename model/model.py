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
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        artefatti = self._artefatto_dao.read_all_artefattos
        if museo == None:
            if epoca == None:
                return artefatti
            else:
                artefatti_filtrati = []
                if artefatti["epoca"]   == epoca:
                    artefatti_filtrati = artefatti_filtrati.append(artefatti)
                return artefatti_filtrati
        else:
            artefatti_filtrati = []
            if artefatti["museo"] == museo:
                artefatti_filtrati = artefatti_filtrati.append(artefatti)
            return artefatti_filtrati

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        artefatti = self._artefatto_dao.read_all_artefattos
        for artefatto in artefatti:
            epoche = [artefatto["epoca"]]
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        musei = self._museo_dao.read_all_museums
        return musei

