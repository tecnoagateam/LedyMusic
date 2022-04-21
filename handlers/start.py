import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
✨ Salam {message.from_user.mention()} !

        mən [{bn}](t.me/{bu}), telegram video chat-da musiqi və video yayınlıya bilən Sahibim Tərəfindən yaradılan bot'am...

Bot Əmrləri bunlarla işlədilə billər : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★Owner: [NRxHacker](t.me/{OWNER_USERNAME})
┣★
┗━━━━━━━━━━━━━━┛

💞 Prablem yaransa Sahiblə [ᴏᴡɴᴇʀ](t.me/{OWNER_USERNAME}) Əlaqəyə keçin...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 Məni Qrupa Əlavə et​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "💔 Sahib 💔", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "🍒 Dəstək 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 İnline 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "📱 Yeniliklər Kanalı", url=f"https://t.me/ledyplaylist"
                    )]
            ]
       ),
    )

