from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""𝗛𝗲𝗹𝗹𝗼 {message.from_user.mention()}, 𝗠𝘆 𝗻𝗮𝗺𝗲 𝗶𝘀 {BOT_NAME}. 𝗧𝗵𝗶𝘀 𝗜𝘀 𝗔 𝗣𝗿𝗼𝗳𝗲𝘀𝘀𝗶𝗼𝗻𝗮𝗹 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 !! 𝗨𝗶 𝗗𝗲𝘀𝗶𝗴𝗻 𝗕𝘆 [𝗡𝘆𝗰](https//t.me/Fake_Friendship_Fake_smile)\𝗻\𝗻𝗗𝗲𝗽𝗹𝗼𝘆 𝗢𝗻 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗩𝗽𝘀 𝗦𝗲𝗿𝘃𝗲𝗿 𝗘𝗻𝗷𝗼𝘆 𝗟𝗮𝗴 𝗙𝗿𝗲𝗲 𝗦𝗼𝗻𝗴 𝗪𝗶𝘁𝗵 𝗦𝘂𝗽𝗲𝗿 𝗦𝗽𝗲𝗲𝗱'𝗫 :) 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "Commands & Help ❔", callback_data="cbbasic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "How to Use Me ❓", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       "Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                       "Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f01f58c3d9b187ae1d8a1.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/AMANTYA1/RaiChu-MusicV2")
                ]
            ]
        ),
    )
