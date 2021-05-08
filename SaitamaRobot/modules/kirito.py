import html
import random

from telegram.error import BadRequest
from tswift import Song

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

import SaitamaRobot.modules.kiritostrings as kiritostrings
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user
from SaitamaRobot.modules.helper_funcs.alternate import send_message, typing_action

from SaitamaRobot import dispatcher, DRAGONS, DEMONS, LOGGER

@run_async
def wiki(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_to_message if update.effective_message.reply_to_message else update.effective_message
    res = ""
    if msg == update.effective_message:
        search = msg.text.split(" ", maxsplit=1)[1]
    else:
        search = msg.text
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        update.message.reply_text(
            "Disambiguated pages found! Adjust your query accordingly.\n<i>{}</i>"
            .format(e),
            parse_mode=ParseMode.HTML)
    except PageError as e:
        update.message.reply_text(
            "<code>{}</code>".format(e), parse_mode=ParseMode.HTML)
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">Read more...</a>"""
        if len(result) > 4000:
            with open("result.txt", 'w') as f:
                f.write(f"{result}\n\nUwU OwO OmO UmU")
            with open("result.txt", 'rb') as f:
                context.bot.send_document(
                    document=f,
                    filename=f.name,
                    reply_to_message_id=update.message.message_id,
                    chat_id=update.effective_chat.id,
                    parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text(
                result,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True)


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

def check_message(context: CallbackContext, message):
    reply_msg = message.reply_to_message

    if message.text.lower() == "kazuya":
        return True
    if reply_msg:
        if reply_msg.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False
    
    
@run_async
def gfban(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name


    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = kiritostrings.GBAM
        reason = random.choice(kiritostrings.GFBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)


    
    

    
GFBAM_HANDLER = CommandHandler("gfban", gfban)    
KIRITO_HANDLER = DisableAbleCommandHandler("kirito", kirito)
KAZUTO_HANDLER = DisableAbleCommandHandler("kazuto", kazuto)
LYRICS_HANDLER = DisableAbleCommandHandler("lyrics", lyrics)
WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki)

dispatcher.add_handler(GFBAM_HANDLER)
dispatcher.add_handler(WIKI_HANDLER)
dispatcher.add_handler(KAZUTO_HANDLER)
dispatcher.add_handler(KIRITO_HANDLER)
dispatcher.add_handler(LYRICS_HANDLER)
