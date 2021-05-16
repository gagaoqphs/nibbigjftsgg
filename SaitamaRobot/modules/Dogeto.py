import requests as r
from pyrogram.types import Message
from pyrogram import filters
from SaitamaRobot import app
from SaitamaRobot.utils import cust_filter
import urllib.request
import json
import asyncio
from random import randint
from pyrogram import filters
from pyrogram.types import Message
from SaitamaRobot import telethn as tbot
from SaitamaRobot.events import register

@register(pattern=r"^/cat ?(.*)")
async def cat(_, message: Message):
    with urllib.request.urlopen(
        "https://api.thecatapi.com/v1/images/search"
    ) as url:
        data = json.loads(url.read().decode())
    cat_url = (data[0]['url'])
    await message.reply_photo(cat_url)


@register(pattern=r"^/reddit ?(.*)")
async def reddit(_, message: Message):
    app.set_parse_mode("html")
    if len(message.command) != 2:
        await message.reply_text("/reddit needs an argument")
    subreddit = message.command[1]
    res = r.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}")
    res = res.json()

    rpage = res.get(str("subreddit"))  # Subreddit
    title = res.get(str("title"))  # Post title
    memeu = res.get(str("url"))  # meme pic url
    plink = res.get(str("postLink"))

    caps = f"<b>Title</b>: {title}\n"
    caps += f"<b>Subreddit: </b>r/{rpage}\n"
    caps += f"<b>PostLink:</b> {plink}"
    await message.reply_photo(photo=memeu, caption=(caps))
