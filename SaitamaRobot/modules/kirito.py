import html
import random
import SaitamaRobot.modules.kiritostrings as kiritostrings
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user
from SaitamaRobot.modules.helper_funcs.alternate import send_message, typing_action


@run_async
def kazuto(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(kiritostrings.KAZUTO))

@run_async
def kirito(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(kiritostrings.KIRI_IMG), caption=f'*Be my opponent {name}*')
    
KIRITO_HANDLER = DisableAbleCommandHandler("kirito", kirito)
    KAZUTO_HANDLER = DisableAbleCommandHandler("kazuto", kazuto)

dispatcher.add_handler(KAZUTO_HANDLER)
dispatcher.add_handler(KIRITO_HANDLER)
