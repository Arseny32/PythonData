import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Определяем команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш Telegram-бот.')

# Определяем команду /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Список доступных команд:\n/start - начать общение\n/help - помощь')

# Основная функция для запуска бота
def main() -> None:
    # Вставьте свой токен, полученный от BotFather
    updater = Updater("7742537641:AAGFiPBr1osSD8l8f41wgltuDSApuy1AOb8")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()