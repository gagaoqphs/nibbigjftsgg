import json
import requests
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import (
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    replymarkup,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    run_async,
    CallbackQueryHandler,
)


def anime_quote():
    url = "https://animechan.vercel.app/api/random"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    quote = dic["quote"]
    character = dic["character"]
    anime = dic["anime"]
    return quote, character, anime


def quotes(update: Update, context: CallbackContext):
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Change🔁", callback_data="change_quote")]]
    )
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


def change_quote(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Change🔁", callback_data="quote_change")]]
    )
    message.edit_text(msg, reply_markup=keyboard, parse_mode=ParseMode.HTML)


QUOTE = DisableAbleCommandHandler("quote", quotes, run_async=True)
CHANGE_QUOTE = CallbackQueryHandler(change_quote, pattern=r"change_.*", run_async=True)
QUOTE_CHANGE = CallbackQueryHandler(change_quote, pattern=r"quote_.*", run_async=True)

dispatcher.add_handler(QUOTE)
dispatcher.add_handler(CHANGE_QUOTE)
dispatcher.add_handler(QUOTE_CHANGE)
