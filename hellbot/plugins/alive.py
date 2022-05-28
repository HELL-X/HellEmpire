import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from hellbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>★ 𝐻𝑒𝑙𝑙 𝐸𝑚𝑝𝑖𝑟𝑒 𝐼𝑠 𝐴𝑙𝑖𝑣𝑒 ★</b></i>
<i><b>♕︎𝑂𝑤𝑛𝑒𝑟 </i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣❥︎ <b>» 𝑇𝑒𝑙𝑒𝑡ℎ𝑜𝑛 ~</b> <i>{}</i>
┣❥︎ <b>» 𝐻𝑒𝑙𝑙𝐸𝑚𝑝𝑖𝑟𝑒 ~</b> <i>{}</i>
┣❥︎ <b>» 𝑆𝑢𝑑𝑜 ~</b> <i>{}</i>
┣❥︎ <b>» 𝑈𝑝𝑇𝑖𝑚𝑒 ~</b> <i>{}</i>
┣❥︎ <b>» 𝑃𝑖𝑛𝑔 ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/HELL_X_EMPIRE'>[ 𝐻𝑒𝑙𝑙𝐸𝑚𝑝𝑖𝑟𝑒 ]</a> «««</i></b>
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>𝐻𝑒𝑙𝑙𝐸𝑚𝑝𝑖𝑟𝑒 ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@hell_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await hell.delete()



@hell_cmd(pattern="Hell$")
async def hell_a(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» нєℓℓвσт ιѕ σиℓιиє ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
