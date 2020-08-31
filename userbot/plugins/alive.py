"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/4d6171ac924c6a11dfe83.png"
pm_caption = "**Userbot di** @GucciRxnS **ONLINE ✅**\n\n"
pm_caption += "**🛠 STATO SISTEMA:**\n"
pm_caption += "**❕ Versione Telethon:** 6.0.9\n🐍 **Python:** 3.7.4\n"
pm_caption += "**🗄 Stato database:** nessun errore\n"
pm_caption += "**🔎 Github update:** master\n"
pm_caption += f"**📲 Account principale**: @lordrxns"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
