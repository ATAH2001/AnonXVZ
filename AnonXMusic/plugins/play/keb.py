import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.command(["/VR"], ""))
async def cpanel(_, message: Message):             
        text = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس المرتجل**"
        kep = ReplyKeyboardMarkup([
["مطور البوت", "مبرمج السورس"],
["السورس","اصدار"],
["اقتباس","استوري"],
["انمي","متحركه"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["قران","نقشبندي"],
["اذكار","كتابات"],
["حروف","بوت"],
["غنيلي","سوال"],
["تلاوات","عبدالباسط"],
["افاتار بنات","افاتار شباب"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command("⛔ ¦ المحظورين") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89840a4c57675832debf9.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🍁 ¦ حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc0bab3462bd868b3081.jpg",
        caption=f"""• اليك طريقه حظر اي شخص .\n\n• قم بـ استخدام الامر هكذا : /block حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🖇 ¦ الغاء حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4268ef332d710c5547357.jpg",
        caption=f"""• اليك طريقه الغاء حظر شخص .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔥 ¦ المحظورين عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc2b0b6c4eea77c43b8b4.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين عام .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🗞 ¦ حظر عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d0db8351713f77bb8450b.jpg",
        caption=f"""• اليك طريقه الحظر العام .\n\n• قم بـ استخدام الامر هكذا :/ح ع\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔖 ¦ الغاء العام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/611ee77edc1763ea2b07b.jpg",
        caption=f"""• اليك طريقه الغاء الحظر العام .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🪂 ¦ الاحصائيات") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/571e1fb1857c8ae6e6be1.jpg",
        caption=f"""• اليك طريقه معرفه الاحصائيات .\n\n• قم بـ استخدام الامر هكذا : الاحصائيات\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command(["ذكاء الاصطناعي"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c544b771eeed7dbdc51a9.jpg",
        caption=f"""• اليك طريقه معرفه سرعه البوت .\n\n• قم بـ استخدام الامر هكذا : /gpt\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )
@app.on_message(filters.command(["تفعيل"], "") & ~filters.private)
async def pipong(client: Client, message: Message):
   if len(message.command) == 1:
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    gr = await get_groupsr(client.me.username)
    A_q_lp = InlineKeyboardMarkup([[InlineKeyboardButton("♪ قناة البوت  💎 .", url="t.me/AlmortagelTech")]])
    await message.reply_text("**♪ تم تفعيل البوت بنجاح  💎 .**",reply_markup=A_q_lp)
    return 
    
@app.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        gr = await get_groupsr(client.me.username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        A_q_lp = InlineKeyboardMarkup([[InlineKeyboardButton("♪ قناة البوت  💎 .", url="t.me/AlmortagelTech")]])
        await client.send_message(chat_id,f"**♪ تم تفعيل البوت تلقائيا  💎 .**",reply_markup=A_q_lp)
        return 
       except:
          pass
    message.continue_propagation()