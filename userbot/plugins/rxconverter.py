"""QuotLy: Avaible commands: .rxconverter
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(admin_cmd(pattern=r"rxconverter(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Rispondi ad un messaggio stupida scimmia.")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("Allora sei proprio stupido, rispondi ad un messaggio con media.")
       return
    chat = "@FileConvertBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("Inoltro comando a @FileConvertBot come Admin")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=649841519))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @QuotLyBot and try again```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)
