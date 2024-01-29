from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai  # Убедитесь, что у вас установлены библиотеки python-telegram-bot и openai


# Замените 'your_openai_api_key' на ваш ключ API от OpenAI
openai.api_key = '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'


# Замените 'your_chatgpt_model_id' на идентификатор вашей модели ChatGPT
model_id = 'ru-davinci-003'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, взаимодействующий с ChatGPT. Отправь мне свой вопрос.')


def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = generate_chatgpt_response(user_input)
    update.message.reply_text(response)


def generate_chatgpt_response(prompt: str) -> str:
    # Запрос к ChatGPT для генерации ответа на основе введенного текста
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def main() -> None:
    # Замените 'your_bot_token' на токен вашего телеграм-бота
    updater = Updater(token='6711276815:AAFxv69mDFYdAZOg0q-taA38bpuL2ZYzbhc 6711276815:AAFxv69mDFYdAZOg0q-taA38bpuL2ZYzbhc', use_context=True)


    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()