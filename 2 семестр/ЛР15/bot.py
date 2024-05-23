import io
import json
import random
import telebot
import calendar
import psycopg2 
from telebot import types
from datetime import date


API_TOKEN = ''
days = ["понедельник", "вторник", "среда", "четверг", "пятница" ]
week_keyboard = (
    types.ReplyKeyboardMarkup(resize_keyboard=True)
    .add(types.KeyboardButton("Понедельник"))
    .add(types.KeyboardButton("Вторник"))
    .add(types.KeyboardButton("Среда"))
    .add(types.KeyboardButton("Четверг"))
    .add(types.KeyboardButton("Пятница"))
    .add(types.KeyboardButton("Расписание на текущую неделю"))
    .add(types.KeyboardButton("Расписание на следующую неделю"))
)

bot = telebot.TeleBot(API_TOKEN)

def connect_db():
    return psycopg2.connect(
        dbname="",
        user="",
        password="",
        host=""
    )

def create_db():
    db_cursor = connect_db.cursor()

    with open('sq_db.sql', 'r') as file:
        query = file.read()

    db_cursor.execute(query)
    db_cursor.commit()

def is_day_name(day_name):
    return day_name.lower() in days

def is_even_week():
    today = date.today()
    week_number = today.isocalendar()[1]
    return week_number % 2 == 0

def get_schedule(day_name, is_even):
    schedule = []

    with io.open("calendar.json", encoding='utf-8') as f:
        file_content = f.read()
        calendar = json.loads(file_content)

        schedule = calendar["even" if is_even else "odd"][day_name.lower()]

    return schedule

def get_format_schedule(day_name, is_even):
    schedule = get_schedule(day_name, is_even)

    formattedString = "{day_name}:\n".format(day_name=day_name.capitalize())

    for item in schedule:
        formattedString += "{item}\n".format(item=item)

    return formattedString

def get_curweek_schedule():
    even = is_even_week()

    s = "Расписание на текущую неделю:\n\n"
    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

def get_nextweek_schedule():
    even = not is_even_week()

    s = "Расписание на следующую неделю:\n\n"
    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Чем могу вам помочь? Используйте /help если у вас возникли вопросы", reply_markup=week_keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_message = """
Привет! Я бот для удобного просмотра учебного расписания.

Я создан в рамках дисциплины "Разработка пользовательского интерфейса" студентом группы 4311-22 Акберовым А. Р.

Вот что я могу:
/start - начать взаимодействие с ботом
/help - получить справку о боте и доступных командах
/week - узнать, верхняя или нижняя текущая неделя
/kstu - получить ссылку на официальный сайт КНИТУ
/vk - получить ссылку на официальную группу КНИТУ в VK
/tg - получить ссылку на официальный Telegram-канал КНИТУ
/location - получить адреса всех учебных корпусов"""

    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['location'])
def handle_location(message):
    locations = """
Местонахождение учебных корпусов:
Корпус «А» - г. Казань, ул. К. Маркса, 68
Корпус «Б», «В», «О» - г. Казань, ул. К. Маркса, 72
Корпус «Д», «Е», «Л», «М» - г. Казань, ул. Сибирский тракт, 12
Корпус «К» - г. Казань, ул. Толстого, 8/31
Корпус «Г» - г. Казань, ул. Попова, 10
Корпус «И» - г. Казань, ул. Сибирский тракт, 41
Корпус «Т» - г. Казань, ул. Толстого, 6 корпус 1
"""

    bot.send_message(message.chat.id, locations)

@bot.message_handler(commands=['vk'])
def handle_vk_group(message):
    bot.send_message(message.chat.id, "Группа Казанского национального технического университета (КНИТУ) в VK: https://vk.com/knitu")

@bot.message_handler(commands=['tg'])
def handle_vk_group(message):
    bot.send_message(message.chat.id, "Telegram-канал Казанского национального технического университета (КНИТУ): https://t.me/knitu_official")

@bot.message_handler(commands=['kstu'])
def kstu_handler(message):
    bot.send_message(message.chat.id, 'Официальный сайт КНИТУ: https://www.kstu.ru/')

@bot.message_handler(commands=['week'])
def handle_week(message):
    bot.send_message(message.chat.id, "Текущая неделя: {week_type}".format(week_type="верхняя" if is_even_week() else "нижняя"))

@bot.message_handler(func=lambda message: message.text.lower() == "куда идти")
def handle_wheretogo(message):
    bot.send_message(message.chat.id, "Для получения адресов корпусов воспользуйтесь командной /location")

@bot.message_handler(func=lambda message: True)
def handle_day(message):
    text = message.text.lower()

    if is_day_name(text):
        schedule = get_format_schedule(text, is_even_week())
        bot.send_message(message.chat.id, schedule)

    #week_num = get_week_num(date.today().day, date.today().month, date.today().year)

    elif text == "расписание на текущую неделю":
        schedule = get_curweek_schedule()
        bot.send_message(message.chat.id, schedule)

    elif text == "расписание на следующую неделю":
        schedule = get_nextweek_schedule()
        bot.send_message(message.chat.id, schedule)

    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял.")


bot.infinity_polling()
create_db()
