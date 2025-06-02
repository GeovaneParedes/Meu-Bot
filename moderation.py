import re
from load_palavras import carregar_palavras_proibidas

palavras_proibidas = carregar_palavras_proibidas()

def is_admin(bot, message):
    try:
        admins = bot.get_chat_administrators(message.chat.id)
        return any(admin.user.id == message.from_user.id for admin in admins)
    except Exception:
        return False

def verificar_palavras_proibidas(bot, message):
    if not message.text:
        return
    texto_original = message.text
    mensagem_alterada = texto_original

    for proibida in palavras_proibidas:
        palavra = proibida["palavra"]
        troca = proibida["troca"]
        pattern = re.compile(rf'\b{re.escape(palavra)}\b', re.IGNORECASE)
        mensagem_alterada = pattern.sub(troca, mensagem_alterada)

    if mensagem_alterada != texto_original:
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(chat_id=message.chat.id, text=mensagem_alterada)
        except Exception as e:
            print(f"Erro ao moderar mensagem: {e}")
