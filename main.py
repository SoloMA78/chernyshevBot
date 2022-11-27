import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from ChernyshevFrendsBot import ChernyshevFrendsBot

def main() -> None:
    cfBot = ChernyshevFrendsBot()
    cfBot.run()

if __name__ == '__main__':
    main()