"""rxlinkconverter: Comandi disponibili: .rxlinkconverter
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(admin_cmd(pattern=r"rxlinkconverter(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Rispondi ad un messaggio stupida scimmia.")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("Inoltro comando a @GucciRxnSConverterBOT")
       return
    chat = "@GucciRxnSConverterBOT"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.")
       return
    await event.edit("Inoltro comando a @GucciRxnSConverterBOT")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1338175784))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Sblocca @GucciRxnSConverterBOT")
              return
          if response.text.startswith("Hi!"):
             await event.edit("Disattiva impostazione privacy per inoltro dei messaggi.")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)
