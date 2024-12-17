
import telebot as tb
import psycopg2
import keyboards
bot = tb.TeleBot('7742537641:AAGFiPBr1osSD8l8f41wgltuDSApuy1AOb8')
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="0000",
                        port=5432)
cursor = conn.cursor()
global IND
IND = ""

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text=f"Стартовое сообщение", reply_markup=tb.types.ReplyKeyboardRemove())

@bot.message_handler(commands=["start1"])
def start_message(message):
    keyboard = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bttn1 = tb.types.KeyboardButton(text="Выложить товар")
    bttn2 = tb.types.KeyboardButton(text="Посмотреть товар")
    keyboard.add(bttn1, bttn2)
    bot.send_message(message.chat.id, text=f"Создана кнопка", reply_markup=keyboard) ###
    bot.register_next_step_handler(message, handle_bttn_lvl_1)

def handle_bttn_lvl_1(message):
    global IND
    if message.text == "Выложить товар":
        IND = "PLACE"
        keyboard = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bttn1 = tb.types.KeyboardButton(text="Одежда")
        bttn2 = tb.types.KeyboardButton(text="Обувь")
        bttn3 = tb.types.KeyboardButton(text="Аксессуары")
        keyboard.add(bttn1, bttn2, bttn3)
        bot.register_next_step_handler(message, handle_bttn_lvl_2)
    if message.text == "Посмотреть товар":
        IND = "LOOK"
        keyboard = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bttn1 = tb.types.KeyboardButton(text="Одежда")
        bttn2 = tb.types.KeyboardButton(text="Обувь")
        bttn3 = tb.types.KeyboardButton(text="Аксессуары")
        keyboard.add(bttn1, bttn2, bttn3)
        bot.register_next_step_handler(message, handle_bttn_lvl_2)

def handle_bttn_lvl_2(message):
    global IND
    if IND == "PLACE":
        if message.text == "Одежда":
        if message.text == "Обувь":
        if message.text == "Аксессуары":
    if IND == "PLACE":
        if message.text == "Одежда":
        if message.text == "Обувь":
        if message.text == "Аксессуары":


bot.polling(none_stop=True)
