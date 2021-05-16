import requests
url = "https://iamai.p.rapidapi.com/ask"
from SaitamaRobot import telethn, OWNER_ID
from SaitamaRobot.events import register
from telethon import events
from telethon import types
from telethon.tl import functions
import asyncio, os

@register(pattern="Kaizu (.*)")
async def hmm(event):
  test = event.pattern_match.group(1)
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if "no no" in result:
   pro = "I weild the AinCrad Sword made by AinCrad rulers."
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "ann" in result:
   pro = "My name is Kirigaya Kazuto"
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(result)
    except CFError as e:
           print(e)
        
        
        
@register(pattern="Waifu (.*)")
async def waifu(animu):
    xx = await eor(animu, "`Processing...`")
    # """Creates random anime sticker!"""
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await xx.edit("`You haven't written any article, Waifu is going away.`")
            return
    waifus = [32, 33, 37, 40, 41, 42, 58, 20]
    finalcall = "#" + (str(random.choice(waifus)))
    try:
        sticcers = await ultroid_bot.inline_query(
            "stickerizerbot",
            f"{finalcall}{(deEmojify(text))}",
        )
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=True if animu.is_reply else False,
            hide_via=True,
        )
        await xx.delete()
    except ChatSendInlineForbiddenError:
        await xx.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await xx.edit("Sorry boss, I can't send Sticker Here !!")

@register(pattern="convert (.*)")
async def uconverter(event):
    xx = await eor(event, "`Processing...`")
    a = await event.get_reply_message()
    ok = ["image/webp", "application/x-tgsticker"]
    if not (a.media and a.media.document and a.media.document.mime_type in ok):
        return await eor(event, "`Reply to a Sticker...`")
    input = event.pattern_match.group(1)
    b = await event.client.download_media(a, "resources/downloads/")
    if "gif" in input:
        cmd = ["lottie_convert.py", b, "something.gif"]
        file = "something.gif"
    elif "img" in input:
        cmd = ["lottie_convert.py", b, "something.png"]
        file = "something.png"
    elif "sticker" in input:
        cmd = ["lottie_convert.py", b, "something.webp"]
        file = "something.webp"
    else:
        return await xx.edit("**Please select from gif/img/sticker**")
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    stderr.decode().strip()
    stdout.decode().strip()
    os.remove(b)
    await event.client.send_file(event.chat_id, file, force_document=False)
    os.remove(file)
    await xx.delete()

