import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
import os

TOKEN = '8190339416:AAEgd0UDRG9J2a4F8ugNas-7AL1SIX1l0_o'
bot = telebot.TeleBot(TOKEN)

# Комплименты
compliments = [
    "Ты – как солнечный лучик 🌞",
    "С тобой каждый день особенный ✨",
    "Ты – чудо в этом мире 🌍",
    "Твоя улыбка освещает всё вокруг 😍",
    "Ты невероятно красива 💖",
    "Ты – мое вдохновение 🎨",
    "С тобой – счастье рядом ❤️",
    "Ты – моя вселенная 🌌",
    "Ты – как песня для моей души 🎶",
    "Ты – самая лучшая девушка на свете 💎"
]

# Подарки: стикер + эмодзи
stickers = [
    'CAACAgQAAxkBAWgNO2feZq3FeaVN_5a2sPz4l7JxtjasAAKDDQACop8IUPwPrm1ppVYENgQ',  # Стикер 1
    'CAACAgQAAxkBAWgNLmfeZjZ0_9-bA1Fy8mmlvRCjhGYZAALxFwACjP4JUlquLrmUJIR9NgQ',  # Стикер 2
    'CAACAgQAAxkBAWgOsmfecU5MggNxDCBufWJ789gHbzhkAAInFAACqK9QUqEJOSpct5giNgQ',
    'CAACAgQAAx0CbDYgDQABAgl4Z9c1fXb04JW-H2FlpmuJf6oez7wAAicXAALaM7hQmWEiCxvP1mw2BA',
    'CAACAgQAAxkBAWgO0WfeciiGcjnfoyQ-eLqRHtTkbX_OAAKBCwACc31gUaKeas6XdLM0NgQ'
    'CAACAgQAAxkBAWgO32feclY0wq6idQ67NkqvtcNh7DRpAAJrCQACoMXoU2ZGGCZhT3Y9NgQ'
    'CAACAgQAAxkBAWgO5mfecmhOngQkhOttT-I2RV5ltW5UAAL7FAAC_nRZUI9sCtptm3dJNgQ'# Стикер 3
]

gifts_text = [
    "🎁 Вот тебе волшебный подарок! 💫",
    "🌟 Это для самой прекрасной девушки 💝",
    "✨ Пусть этот подарок поднимет тебе настроение! 🎀",
    "💐 Для тебя — букет самой искренней любви 🌸",
    "🎈 Сюрприз! Ты заслуживаешь только лучшее 💖",
    "🍫 Шоколадное настроение только для тебя 😋",
    "🧸 Объятия в коробке! Лови 🤗",
    "🌹 Роза для той, кто прекраснее цветов 🌷",
    "🕊️ Пусть этот подарок принесёт тебе гармонию и радость 💞",
    "🎊 Ты особенная, и этот подарок — знак моей любви 💌",
    "🦄 Волшебство рядом, когда ты улыбаешься ✨",
    "🥰 Подарок от души для самой милой девушки на свете 💘",
    "💎 Блестящий подарок для моей звезды ⭐",
    "📦 Маленький ящик счастья только для тебя 🫶",
    "🍓 Сладкий комплимент в форме подарка 😍",
    "🐻 Мишка передаёт тебе свои плюшевые обнимашки 🐾",
    "💫 Пусть этот день будет сказочным — как ты 🌈"
]

# Музыка
music_files = [
    "love1.mp3",
    "love2.mp3",
    "love3.mp3",
    "love4.mp3",
    "love5.mp3",
    "love6.mp3",
    "love7.mp3",
]

# Кнопки
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("💌 Комплимент"),
        KeyboardButton("🎁 Получить подарок"),
        KeyboardButton("🎶 Музыка о любви"),
        KeyboardButton("🌟 Получить TG-подарок")
    )
    return markup


# Старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, Азиза! 💖 Выбери, что хочешь получить сегодня:", reply_markup=main_menu())

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "💌 Комплимент":
        compliment = random.choice(compliments)
        bot.send_message(message.chat.id, compliment)

    elif message.text == "🎁 Получить подарок":
        gift_text = random.choice(gifts_text)
        sticker_id = random.choice(stickers)
        bot.send_message(message.chat.id, gift_text)
        bot.send_sticker(message.chat.id, sticker_id)

    elif message.text == "🎶 Музыка о любви":
        music = random.choice(music_files)
        if os.path.exists(music):
            with open(music, 'rb') as audio:
                bot.send_audio(message.chat.id, audio, caption="Вот песня специально для тебя ❤️")
        else:
            bot.send_message(message.chat.id, "Песня не найдена 😢 Убедись, что файл есть в папке с ботом.")

    elif message.text == "🌟 Получить TG-подарок":
        bot.send_message(message.chat.id,
                         "Чтобы отправить настоящий Telegram-подарок 🌟 — открой чат с @ishowdopamine и оправь ему стикер и он подарить тебе подарок от своего имени 💝")

    else:
        bot.send_message(message.chat.id, "Выбери один из вариантов в меню ✨", reply_markup=main_menu())

# Запуск
bot.polling(none_stop=True)
