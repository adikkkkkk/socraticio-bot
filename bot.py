import telebot

TOKEN = "8439390561:AAHvu9dkFPncPLzO7gMpjd6iALmH1BpUO54"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Socraticio. Напиши тему.")

@bot.message_handler(func=lambda message: True)
def main(message):
    bot.send_message(message.chat.id,
        "📚 Объясни простыми словами\n"
        "🤔 Почему это работает?\n"
        "💡 Пример из жизни"
    )

bot.polling()
