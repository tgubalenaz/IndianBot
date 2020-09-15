"""

Available Commands:

.sux

.fuk

.kiss"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd("simptester"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 101)

    #input_str = event.pattern_match.group(1)

   # if input_str == "simptester":

    await event.edit("🔍 **ESEGUO CONTROLLO SULL'UTENTE SELEZIONATO**")

    animation_chars = [

            "Simp tester avviato. ✅",

            "🔎 **Verifico.**",

            "🔎 **Verifico..**",

            "🔎 **Verifico...**",

            "🔎 **Verifico....**",

            "🔦 L'utente selezionato sembra essere un simp!",

            "**Sei un simp al 98% 🤫**"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 20])


