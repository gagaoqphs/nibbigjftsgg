import html
import random

from telegram.error import BadRequest
from tswift import Song

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
    
    
@run_async
@typing_action
def lyrics(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message
    query = " ".join(args)
    song = ""
    if not query:
        msg.reply_text("You haven't specified which song to look for!")
        return
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song!"
    else:
        reply = "Song not found!"
    if len(reply) > 4090:
        with open("lyrics.txt", 'w') as f:
            f.write(f"{reply}\n\n\nOwO UwU OmO")
        with open("lyrics.txt", 'rb') as f:
            msg.reply_document(document=f,
            caption="Message length exceeded max limit! Sending as a text file.")
    else:
        msg.reply_text(reply)


    
KIRITO_HANDLER = DisableAbleCommandHandler("kirito", kirito)
KAZUTO_HANDLER = DisableAbleCommandHandler("kazuto", kazuto)
LYRICS_HANDLER = DisableAbleCommandHandler("lyrics", lyrics)

dispatcher.add_handler(KAZUTO_HANDLER)
dispatcher.add_handler(KIRITO_HANDLER)
dispatcher.add_handler(LYRICS_HANDLER)
