"""

Available Commands:

.sux

.fuk

.kiss"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd("lovelang"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

   # if input_str == "lovelang":

    await event.edit("lovelang")

    animation_chars = [

            "TI AMO",

            "TE AMO",

            "I LOVE YOU",

            "JE T'AIME",

            "TE QUIERO",

            "EU TE AMO",

            "TE IUBESC",

            "Я тебя люблю",

            "AISHITERU",

            "我愛你。"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 20])


