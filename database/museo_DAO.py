from database.DB_connect import ConnessioneDB  # importa la classe/utility per ottenere la connessione al DB
from model.museoDTO import Museo  # importa il DTO/struct per rappresentare un Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:  # definizione della classe DAO per i musei
    def __init__(self):  # costruttore della classe
        pass  # nessuna inizializzazione necessaria

    @staticmethod
    def read_all_museums():  # metodo statico che legge tutti i musei dal DB
        print("Executing read from database using SQL query")  # log su console per debug
        results = []  # lista che conterrà gli oggetti Museo risultanti dalla query
        cnx = ConnessioneDB.get_connection()  # apre/ottiene la connessione al DB
        if cnx is None:  # se la connessione non è stata ottenuta
            print("Connection failed")  # stampa messaggio di errore
            return None  # restituisce None per indicare fallimento
        else:  # se la connessione è ok
            cursor = cnx.cursor(dictionary=True)  # crea un cursore che restituisce righe come dizionari
            # Una sola query, con cui si leggono tutte le righe (si selezioneranno poi quelle che interessano es. con un if)
            query = """SELECT * 
                       FROM Museo"""  # query SQL multi-linea per selezionare tutte le righe dalla tabella Museo
            cursor.execute(query)  # esegue la query sul DB
            for row in cursor:  # itera sulle righe ritornate dal cursore
                # Posso creare oggetti di tipo museo
                museo = Museo(row["id"], row["nome"], row["tipologia"])  # crea un'istanza Museo usando i campi della riga
                results.append(museo)  # aggiunge l'oggetto Museo alla lista dei risultati

            cursor.close()  # chiude il cursore
            cnx.close()  # chiude la connessione al DB
            return results  # restituisce la lista di oggetti Museo