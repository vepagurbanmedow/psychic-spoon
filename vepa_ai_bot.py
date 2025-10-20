import telebot
import openai
import os
from dotenv import load_dotenv

# .env fayldan tokenlarni yuklaymiz
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_KEY

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Salom! Men Vepa yaratgan sun’iy intellektman. Nima yordam kerak?")

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    user_text = message.text

    if "kim yaratgan" in user_text.lower():
        bot.reply_to(message, "Meni Vepa dasturchi yaratgan 🤖")
        return

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        answer = completion.choices[0].message["content"]
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

print("🤖 Bot ishga tushdi...")
bot.polling()

