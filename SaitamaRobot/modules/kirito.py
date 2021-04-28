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
   
@run_async
def kirito(update: Update, context: CallbackContext):
update.effective_message.reply_photo(random.choice(kiritostrings.KIRI_IMG), caption=f'*Command me*')



KAZUTO_HANDLER = DisableAbleCommandHandler("kazuto", kazuto)
KIRITO_HANDLER = DisableAbleCommandHandler("kirito", kirito)

dispatcher.add_handler(KAZUTO_HANDLER)
dispatcher.add_handler(KIRITO_HANDLER)
