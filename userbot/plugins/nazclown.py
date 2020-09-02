"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/4161fabad95cc63d78a64.png"
pm_caption = "**🎊 Congratulazioni! 🎉**\n"
pm_caption += "Non avevo mai letto così tante pagliacciate in una volta sola e ho deciso di conferirti un riconoscimento..\n\n"
pm_caption += "**SEI UFFICIALMENTE UN NUOVO PAGLIACCIO DI NAZLAND! 🤡**"

@borg.on(admin_cmd(pattern=r"clown"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"clown", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
