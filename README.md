# Atendimento de TI utilizando Watson Assistant

## Primeiros passos

1. Clonar projeto em sem ambiente local;

2. Criar o enviroment dentro da pasta raíz do projeto.

> python -m venv venv

3. Ativar o enviroment.

> .\venv\Scripts\activate

4. Instalar as dependências

> pip install -r requitements.txt

5. Acessar o arquivo "watson_config.py" dentro da pasta "watson" e alimentar as respectivas variáveis de autenticação.
```
apikey: str = "colar a sua api key aqui"

service_url: str = "colar a url do seu serviço do Watson Assistant aqui"

version: str = "versão do seu assistente no formato yyyy-MM-dd"

assistant_id: str = "sua assistant id"
```

6. Executar o serviço.

> python app.py

## Métricas

Na pasta notebooks é possível acompanhar alguns indicadores do experimento no arquivo "kpis".

## Skills Chatbot

Na pasta "skill" contém conteúdo o "json" gerado pela plataforma IBM Assistant com as intenções geradas para treino.

## Referências

https://github.com/arjuntherajeev/watson_chatbot_template