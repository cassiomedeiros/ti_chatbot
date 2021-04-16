from flask import Flask, render_template
import os
from watson.assistant import AssistantService
import watson.utils as utils
import random
from random import randint
from watson.save_data import WatsonDB

app = Flask(__name__)
assistente_service = AssistantService()

watsonDB = WatsonDB()


@app.route('/')
@app.route('/index')
def chat():
    return render_template('chat.html')

@app.route('/send_message/<message>')
def send_mesage(message):

    # envia mensagem para o Watson
    response = assistente_service.send_message(message)

    # formata mensagem recebida do Watson para o chat
    result = utils.convert_response_message_to_chat(response)
    
    # armazena mensagem do usuário e resposta do Watson.
    watsonDB.save_message(message, 'user')
    watsonDB.save_message(response['output'], 'watson')

    # cria um número de ticket aleatório para responder aos usuário nos casos
    # quem o assitente não conseguiu ajudar.
    ticket_number = utils.create_ticket(result)
    if ticket_number is not None:
        watsonDB.save_message(str(ticket_number), 'ticket')
        result = result.replace('um ticket', f'um ticket com número {ticket_number}')

    # devolve para o usuário um status aleatório do ticket quando ele solicita
    status = utils.get_status(result)
    if status is not None:
        result = result.replace('ticket é', f'ticket é {status}. ')

    return result

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8666))
    app.run(host='127.0.0.1', port=port, debug=True)
