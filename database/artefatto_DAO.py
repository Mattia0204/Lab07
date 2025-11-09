from database.DB_connect import ConnessioneDB  # importa la classe che gestisce la connessione al database
from model.artefattoDTO import Artefatto  # importa il DTO che rappresenta un artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:  # definizione della classe DAO per gli artefatti
    def __init__(self):  # costruttore
        pass  # nessuna inizializzazione specifica necessaria

    @staticmethod
    def read_all_artefattos():  # metodo statico per leggere tutti gli artefatti dal DB
        print("Executing read from database using SQL query")  # messaggio di debug
        results = []  # lista dove verranno salvati gli oggetti Artefatto recuperati
        cnx = ConnessioneDB.get_connection()  # tenta di ottenere una connessione al database
        if cnx is None:  # se la connessione non va a buon fine
            print("Connection failed")  # messaggio informativo
            return None  # ritorna None per segnalare l'errore
        else:  # se la connessione è avvenuta correttamente
            cursor = cnx.cursor(dictionary=True)  # crea un cursore che restituisce ogni riga come dizionario

            # Query per leggere tutte le righe della tabella Artefatto
            query = """SELECT * 
                       FROM Artefatto"""  # query SQL multilinea

            cursor.execute(query)  # invia la query al database

            for row in cursor:  # scorre tutte le righe restituite dalla query
                # Crea un oggetto Artefatto usando i valori contenuti nella riga
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)  # aggiunge l'oggetto creato alla lista dei risultati

            cursor.close()  # chiude il cursore
            cnx.close()  # chiude la connessione al database
            return results  # restituisce la lista di artefatti
