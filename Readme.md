Telegram Bot: DevProgramadorbot - Version 0.1.0
Explanation in English:

This Telegram bot, named DevProgramadorbot, is designed to assist users in finding programming-related courses and to help administer a Telegram group by moderating messages.

Features
Course Management
Search Courses: Users can search for courses by typing a relevant term in a private chat with the bot. The bot will return a list of matching courses with their names, languages, and direct links to access them, presented as inline keyboard buttons.
Add Courses (Admin Only): Authorized users can add new courses to the bot's database using the /addcourse command. The command requires the course's language, name, and a link, formatted as /addcourse language | course name | link. This command is restricted to private chats.
Group Moderation
Profanity Filter: In groups, the bot checks messages for predefined "forbidden words". If a forbidden word is detected, the original message is deleted, and a modified version of the message (with the forbidden word replaced) is sent back to the chat.
Admin Exemption: Administrators in a group are exempt from the profanity filter.
How to Use
For All Users
Start a chat with the bot: Find the bot on Telegram and start a private conversation.
Search for courses: Simply type the programming language or topic you're interested in (e.g., "web", "UI", "UX"). The bot will respond with available courses.
For Authorized Users (Admins)
Add a new course: In a private chat with the bot, use the command:
/addcourse <language> | <course name> | <link>

Replace <language> with the programming language or category (e.g., python, javascript, UI).
Replace <course name> with the full name of the course.
Replace <link> with the URL to the course.
Example: /addcourse Python | Python para Iniciantes | https://example.com/python

Setup and Configuration
Prerequisites
Python 3.x
pyTelegramBotAPI library
Installation
Clone the repository:

Bash

git clone <repository_url>
cd <repository_directory>
Install dependencies:

Bash

pip install pyTelegramBotAPI
Set up your Bot Token:
Obtain your bot token from BotFather on Telegram. Set it as an environment variable named TELEGRAM_BOT_TOKEN.
Alternatively, you can directly replace 'seu_token' in config.py with your bot token (though using environment variables is recommended for security).

Linux/macOS:

Bash

export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
Windows (Command Prompt):

Bash

set TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
Windows (PowerShell):

PowerShell

$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
Configure Authorized Users:
Edit the USUARIOS_AUTORIZADOS set in handlers.py to include the user IDs or usernames (prefixed with @) of users authorized to add courses.

Python

USUARIOS_AUTORIZADOS = {
    123456789,         # Your user ID
    '@your_username'   # Your username (lowercase and with @)
}
Customize Forbidden Words:
The palavras_proibidas.json file contains a list of words to be moderated and their replacements. You can edit this file to add, remove, or change entries.

JSON

[
    {"palavra": "badword", "troca": "goodword"},
    {"palavra": "anotherbad", "troca": "anothergood"}
]
Running the Bot
To start the bot, run the bot.py script:

Bash

python bot.py
You will see the message "Bot rodando..." in your console, indicating the bot is active.

Project Structure
bot.py: The main entry point of the bot. Initializes the bot and starts polling for messages.
config.py: Handles the loading of the bot's API token from environment variables.
courses.py: Contains functions for loading, saving, adding, and searching for courses from cursos_devprogramador.json.
cursos_devprogramador.json: A JSON file storing the course data (language, name, link).
handlers.py: Defines how the bot responds to various commands and messages, including course search, adding courses, and integration with moderation.
load_palavras.py: Utility to load the list of forbidden words from a JSON file.
moderation.py: Implements the message moderation logic, including checking for forbidden words and admin status.
palavras_proibidas.json: A JSON file containing the list of words to be moderated and their respective replacements.

Explicação em Portugues-BR:

Bot Telegram: DevProgramadorbot - Versão 0.1.0
Este bot para Telegram, chamado DevProgramador, foi desenvolvido por mim, para ajudar usuários a encontrar cursos relacionados à programação(obs. Cursos estes disponíveis no Telegram e somente encaminha o usuário a canais externos) e auxiliar na administração de grupos do Telegram através da moderação de mensagens.

Funcionalidades
Gestão de Cursos
Buscar Cursos: Os usuários podem procurar cursos digitando um termo relevante em um chat privado com o bot. O bot retornará uma lista de cursos correspondentes com seus nomes, linguagens e links diretos para acessá-los, apresentados como botões de teclado inline.
Adicionar Cursos (Somente Admin): Usuários autorizados podem adicionar novos cursos ao banco de dados do bot usando o comando /addcourse. O comando requer a linguagem do curso, o nome e um link, formatado como /addcourse linguagem | nome do curso | link. Este comando é restrito a chats privados.
Moderação de Grupos
Filtro de Palavrões: Em grupos, o bot verifica as mensagens em busca de "palavras proibidas" predefinidas. Se uma palavra proibida for detectada, a mensagem original é apagada e uma versão modificada da mensagem (com a palavra proibida substituída) é enviada de volta ao chat.
Exceção para Administradores: Administradores de um grupo estão isentos do filtro de palavrões.
Como Usar
Para Todos os Usuários
Iniciar um chat com o bot: Encontre o bot no Telegram e inicie uma conversa privada.
Buscar cursos: Basta digitar a linguagem de programação ou tópico de seu interesse (ex: "web", "UI", "UX"). O bot responderá com os cursos disponíveis.
Para Usuários Autorizados (Admins)
Adicionar um novo curso: Em um chat privado com o bot, use o comando:
/addcourse <linguagem> | <nome do curso> | <link>

Substitua <linguagem> pela linguagem de programação ou categoria (ex: python, javascript, UI).
Substitua <nome do curso> pelo nome completo do curso.
Substitua <link> pela URL do curso.
Exemplo: /addcourse Python | Python para Iniciantes | https://example.com/python

Configuração e Instalação
Pré-requisitos
Python 3.x
Biblioteca pyTelegramBotAPI
Instalação
Clonar o repositório:

Bash

git clone <url_do_repositorio>
cd <diretorio_do_repositorio>
Instalar dependências:

Bash

pip install pyTelegramBotAPI
Configurar o Token do seu Bot:
Obtenha o token do seu bot no BotFather do Telegram. Defina-o como uma variável de ambiente chamada TELEGRAM_BOT_TOKEN.
Alternativamente, você pode substituir diretamente 'seu_token' em config.py pelo seu token do bot (embora o uso de variáveis de ambiente seja recomendado por segurança).

Linux/macOS:

Bash

export TELEGRAM_BOT_TOKEN="SEU_TOKEN_DO_BOT"
Windows (Prompt de Comando):

Bash

set TELEGRAM_BOT_TOKEN="SEU_TOKEN_DO_BOT"
Windows (PowerShell):

PowerShell

$env:TELEGRAM_BOT_TOKEN="SEU_TOKEN_DO_BOT"
Configurar Usuários Autorizados:
Edite o conjunto USUARIOS_AUTORIZADOS em handlers.py para incluir os IDs de usuário ou nomes de usuário (prefixados com @) dos usuários autorizados a adicionar cursos.

Python

USUARIOS_AUTORIZADOS = {
    123456789,         # Seu ID de usuário
    '@seu_nome_de_usuario'   # Seu nome de usuário (em minúsculas e com @)
}
Personalizar Palavras Proibidas:
O arquivo palavras_proibidas.json contém uma lista de palavras a serem moderadas e suas substituições. Você pode editar este arquivo para adicionar, remover ou alterar entradas.

JSON

[
    {"palavra": "palavrafeia", "troca": "palavraboa"},
    {"palavra": "outrafeia", "troca": "outraboa"}
]
Rodando o Bot
Para iniciar o bot, execute o script bot.py:

Bash

python bot.py
Você verá a mensagem "Bot rodando..." no seu console, indicando que o bot está ativo.

Estrutura do Projeto
bot.py: O ponto de entrada principal do bot. Inicializa o bot e começa a sondar por mensagens.
config.py: Lida com o carregamento do token da API do bot a partir de variáveis de ambiente.
courses.py: Contém funções para carregar, salvar, adicionar e buscar cursos de cursos_devprogramador.json.
cursos_devprogramador.json: Um arquivo JSON que armazena os dados dos cursos (linguagem, nome, link).
handlers.py: Define como o bot responde a vários comandos e mensagens, incluindo busca de cursos, adição de cursos e integração com a moderação.
load_palavras.py: Utilitário para carregar a lista de palavras proibidas de um arquivo JSON.
moderation.py: Implementa a lógica de moderação de mensagens, incluindo a verificação de palavras proibidas e o status de administrador.
palavras_proibidas.json: Um arquivo JSON contendo a lista de palavras a serem moderadas e suas respectivas substituições.
