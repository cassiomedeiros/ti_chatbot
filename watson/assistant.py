from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2
import watson.watson_config as config

class AssistantService:

    """ Classe responsável por criar a comunicação com o Watson Assistant.
    """

    def __init__(self):
        """Inicializa variáveis e cria a sessão com o Watson.
        """
        self._service = None
        self._session_id = None
        self._create_session()
    
    def _create_session(self):
        """Realiza autenticação e cria sessão com o Watson.
        """

        authenticator = IAMAuthenticator(apikey=config.apikey)

        self._service = AssistantV2(
            version=config.version,
            authenticator=authenticator
        )

        session = self._service.create_session(
            assistant_id = config.assistant_id 
        )
        self._session_id = session.get_result()['session_id']

    def send_message(self, message: str):
        """Envia mensagem para o Watson Assistant.

        Args:
            message: O conteúdo da mensagem a ser enviada.
        """

        response = self._service.message(
            config.assistant_id, 
            self._session_id, 
            input={
                'message_type:': 'text',
                'text': str(message)
            })

        result = response.get_result()

        return result

    




