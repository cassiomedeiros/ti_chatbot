import random


def convert_response_message_to_chat(response: dict) -> str:
    """Convert conteúdo das mensagens do Watson para
    ser interpretado pelo chat.
    """

    result = ""

    for item in response['output']['generic']:
        key = list(item.keys())[0]
        
        if key == 'response_type' and item['response_type'] == 'text':
            result += item['text']
        elif (key == 'response_type' and item['response_type'] == 'title') or (key == 'title'):
            result += item['title']

            content = "</br>"
            for item in item['options']:
                content += f"""<strong><a href='#' onclick='javascript:sendOption(this);'>{item['label']}</a></strong></br>"""
            result += content

    if len(result) == 0:
        result = "Não entendi sua resposta/pergunta"

    return result


def create_ticket(message: str) -> None:
    """Cria ticket com número aleatório para devolver ao usuário.
    """

    ticket_value: int = None

    if message.find('um ticket') > 0:
        return random.randint(10000, 99999)

    return ticket_value


def get_status(message: str) -> None:
    """Cria status aleatório para devolver ao usuário.
    """

    if message.find('ticket é') > 0:

        status = ['Aberto', 'Em Andamento', 'Cancelado', 'Fechado']
        choice = random.randint(0, 3)
        
        return status[choice]
    else:
        return None
