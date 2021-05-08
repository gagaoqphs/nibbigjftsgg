import html

from typing import Optional

from telegram import Update, Bot
from telegram.ext import CommandHandler, Filters
from SaitamaRobot.ext.dispatcher import run_async

from SaitamaRobot import dispatcher, DRAGONS, OWNER_USERNAME, OWNER_ID
from SaitamaRobot.modules.helper_funcs.extraction import extract_user
from SaitamaRobot.modules.helper_funcs.chat_status import bot_admin

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "SaitamaRobot/elevated_users.json")


@bot_admin
@run_async
def sudopromote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    banner = update.effective_user
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("You don't seem to be referring to a user.")
        return ""
        
    if int(user_id) == OWNER_ID:
        message.reply_text("Solo AinCrad Raider has always been one of my favorites!")
        return ""
        
    if int(user_id) in DRAGONS:
        message.reply_text("Already a serving Shadow of AinCrad.")
        return ""
    
    with open(ELEVATED_USERS_FILE,"a") as file:
        file.write(str(user_id) + "\n")
    
    DRAGONS.append(user_id)
    message.reply_text("Succefully extracted Shadow under your protection now!")
        
    return ""

@bot_admin
@run_async
def sudodemote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("You don't seem to be referring to a Shadow.")
        return ""

    if int(user_id) == OWNER_ID:
        message.reply_text("Solo AinCrad Raider! He holds all the powers here...U cant touch him")
        return ""
    
    if user_id not in DRAGONS:
        message.reply_text("{} is not a sudo user".format(user_id))
        return ""

    users = [line.rstrip('\n') for line in open(ELEVATED_USERS_FILE)]

    with open(ELEVATED_USERS_FILE,"w") as file:
        for user in users:
            if not int(user) == user_id:
                file.write(str(user) + "\n")

    DRAGONS.remove(user_id)
    message.reply_text("Shadow Released... Disappered into nothingness...!")
    
    return ""


__help__ = """
*Bot owner only:*
 - /addshadow: promotes the user to SUDO USER
 - /rmshadow: demotes the user from SUDO USER
"""

__mod_name__ = "SUDO"

SUDOPROMOTE_HANDLER = CommandHandler("addshadow", sudopromote, pass_args=True, filters=Filters.user(OWNER_ID))
SUDODEMOTE_HANDLER = CommandHandler("rmshadow", sudodemote, pass_args=True, filters=Filters.user(OWNER_ID))

dispatcher.add_handler(SUDOPROMOTE_HANDLER)
dispatcher.add_handler(SUDODEMOTE_HANDLER)
