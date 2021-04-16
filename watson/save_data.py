import json
from datetime import datetime

class WatsonDB:

    """Classe responsável por recuperar e armazenar dados 
        em um estrutura de dados em Json.
    """

    def __init__(self):
        """Inicializa a estrutura de dados.
        """
        self._initialize_data()
        self._file_name = "temp\\data.json"

    def _initialize_data(self):
        """Inicializa a estrutura de dados.
        """
        self._data = {}
        self._data['watson'] = list()
        self._data['user'] = list()
        self._data['ticket'] = list()
 
    def _load_data(self):
        """Carrega os dados da base local.
        """

        try:
            f = open(self._file_name)
            self._data = json.load(f)
            f.close()
        except:
            pass

    def save_message(self, message, key):
        """Salva os dados da estrutura de dados local

        Args:
            message: O conteúdo da menssagem a ser armazenada.
            key: O nome da chave onde a mensagem deverá ser armazenada.
            As keys podem ser:
                - "watson" para conteúdo de resposta do Watson;
                - "user" para armazenar os dados de entrada dos usuários;
                - "ticket" para armazenar os tickets aleatórios gerados.
        """

        msg = {
            "date": str(datetime.now()),
            "message": message
        }

        self._load_data()
        self._data[key].append(msg)

        with open(self._file_name, 'w+') as f:
            json.dump(self._data, f)

        return self._data

    def get_messages(self):
        """Recupera mensagens armazenadas na estrutura local.
        """
        self._load_data()

        return self._data



