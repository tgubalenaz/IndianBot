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

   # if input_str == "fuk":

    await event.edit("fuk")

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

        await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd("sux"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

    #if input_str == "sux":

    await event.edit("sux")

    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵👼👰"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


""


from telethon import events

import asyncio





@borg.on(admin_cmd("kiss"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

    #if input_str == "kiss":

    await event.edit("kiss")

    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵💋👰"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])
