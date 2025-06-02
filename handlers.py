from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from moderation import verificar_palavras_proibidas, is_admin
from courses import buscar_cursos, adicionar_curso

USUARIOS_AUTORIZADOS = {
    1910472568,        # Seu user ID
    '@devgege'         # Username em minúsculo e sem @ para facilitar comparação
}

def is_authorized_user(message):
    user_id = message.from_user.id
    username = message.from_user.username
    if user_id in USUARIOS_AUTORIZADOS:
        return True
    if username and ('@' + username.lower()) in {'@' + u for u in USUARIOS_AUTORIZADOS if isinstance(u, str)}:
        return True
    return False

def register_handlers(bot):

    @bot.message_handler(commands=['addcourse'])
    def handle_add_course(message):
        if message.chat.type != 'private':
            bot.reply_to(message, "Esse comando só pode ser usado no chat privado.")
            return

        if not is_authorized_user(message):
            bot.reply_to(message, "Você não tem permissão para adicionar cursos.")
            return

        try:
            _, data = message.text.split(' ', 1)
            linguagem, nome, link = [item.strip() for item in data.split('|')]
        except Exception:
            bot.reply_to(message, "Formato inválido. Use:\n/addcourse linguagem | nome do curso | link")
            return

        adicionar_curso(linguagem, nome, link)
        bot.reply_to(message, f"Curso '{nome}' na linguagem '{linguagem}' adicionado com sucesso!")

    @bot.message_handler(func=lambda m: True)
    def handle_message(message):
        if not message.text:
            return

        if message.chat.type in ['group', 'supergroup']:
            if is_admin(bot, message):
                return
            verificar_palavras_proibidas(bot, message)

        elif message.chat.type == 'private':
            send_courses(bot, message)

def send_courses(bot, message):
    termo = message.text.strip()
    cursos_encontrados = buscar_cursos(termo)

    if cursos_encontrados:
        resposta = "Cursos encontrados:\n\n"
        keyboard = InlineKeyboardMarkup()
        for curso in cursos_encontrados:
            texto_botao = f"{curso['nome']} ({curso['linguagem']})"
            link = curso['link']
            keyboard.add(InlineKeyboardButton(text=texto_botao, url=link))
        bot.send_message(message.chat.id, resposta, reply_markup=keyboard)
    else:
        bot.reply_to(message, "Nenhum curso encontrado para esse termo.")
