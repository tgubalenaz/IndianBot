from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = [
    "PayPal.me/AlessandroPrestii",
]

@borg.on(admin_cmd(pattern="pp"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
