from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
import random

class ChernyshevFrendsBot:

    frends_names = ['Начальник', 'Вика-мерседес', 'Гончаров', 'Илья', 'Дмитрий', 'Мадина', 'Юля', 'Владимир Зотов']
    answers = {
        'чо нового?': ['Эти клоуны на работе опять не работают. Надо тебе выйти раздать пинков',
                       'Что может быть нового в этом цирке?',
                       'Маразм крепчает', 'Пацаны тебе привет передавали, с поклоном', 'Тухло'],
        'попиздеть': ['Рыба гниет с головы, а помидор с жопки',
                      'Ученые из Тайланда открыли новый рецепт рыбного соуса',
                      'Минпромторг сформровал программу для реабилитации трудных подростков из Гатчины',
                      'Рамсы надо загибать по понятиям', 'Свежий воздух-лучшее средство от бессоницы'],
        'жрать пойдете?': ['Ага, щас',
                           'Нафиг, холодно',
                           'Так уже пожрали',
                           'Через 15 минут', 'Иди один, смотри не подавись',
                           'Лучше бы выпить предложил']
    }

    default_mes = 'Что-то дружок ты странные вопросы задаешь. Ты точно Чернышев?!. Я понимаю вопросы:' \
                  '"чо нового?","жрать пойдете?", "попиздеть". \n' \
                  'Еще я могу добавить эмоций в наш разговор командой /scream или быть поспокойней /quiet'

    def __init__(self):
        updater = Updater(self.getToken())
        # Get the dispatcher to register handlers
        # Then, we register each handler and the conditions the update must meet to trigger it
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("scream", self.scream))
        dispatcher.add_handler(CommandHandler("quite", self.quiet))
        #dispatcher.add_handler(CommandHandler("whisper", whisper))
        #dispatcher.add_handler(CommandHandler("menu", menu))
        # Register handler for inline buttons
        #dispatcher.add_handler(CallbackQueryHandler(button_tap))
        # Echo any message that is not a command
        dispatcher.add_handler(MessageHandler(~Filters.command, self.echo))
        self.updater = updater
        self.dispatcher = dispatcher
        self.screem = False

    def getName(self):
        return 'ChernyshevFrendsBot'

    def getToken(self):
        with open('.token') as f:
            token = f.read()
        return token

    def echo(self, update: Update, context: CallbackContext):
        # Print to console
        print(f'{update.message.from_user.first_name} wrote {update.message.text}')
        if update.message.text and update.message.text.lower() in self.answers.keys():
            answ = f'{random.choices(self.frends_names)[0]} пишет:' \
                   f' {random.choices(self.answers[update.message.text.lower()])[0]}'
        else:
            answ = self.default_mes
        if self.screem:
            answ = answ.upper()
        context.bot.send_message(
                update.message.chat_id,
                answ,
                # To preserve the markdown, we attach entities (bold, italic...)
                 entities=update.message.entities
        )
        #update.message.copy(update.message.chat_id)

    def scream(self, update: Update, context: CallbackContext):
        self.screem = True

    def quiet(self, update: Update, context: CallbackContext):
        self.screem = False

    def run(self):
        # Start the Bot
        self.updater.start_polling()
        # Run the bot until you press Ctrl-C
        self.updater.idle()
