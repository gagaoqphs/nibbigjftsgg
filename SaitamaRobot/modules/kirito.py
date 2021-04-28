import html
import random
import SaitamaRobot.modules.kiritostrings as kiritostrings
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def kazuto(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(kiritostrings.KAZUTO))
   


KAZUTO_HANDLER = DisableAbleCommandHandler("KAZUTO", animequotes)

dispatcher.add_handler(KAZUTO_HANDLER)
