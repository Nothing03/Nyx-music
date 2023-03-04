## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCmlWUTtuk9O9JqKzrwVjbiZA5fJv7bNgL4CqMeJ4y57nYxFTK6yN1kPE3F1TaAOfto-ph3QByA8oTGALS-dqJ_OWs1aC3lL1UOI4QgK95sxCz2tWFYo1IhWzMN-ov3Gq8M4LGJ5L7rRdQ7M8pf9kWuuRW9WITXAEDzvmKMuN37bIBwwOnG3HAsARiU6Fkk1fFDLWzR0uQ8wFceGQYFYwdaGaXXQb-udTQ9kUeq_afFUYnH9i5q4wlQbMZBNTgpy33LgPS_c9HRxNva3C3h8y6JNKrD_HYFiT8kS6Oi0XSFUGEv3oArtvFzatE_PSVxw8P-5ldeTcu4TmpSBzis3bUHAAAAAWiCwroA")
BOT_TOKEN = getenv("BOT_TOKEN", "6257547712:AAHgzrWZDZWOBdxKSYtNaWAG8VpFDr9TVMI")
BOT_NAME = getenv("BOT_NAME", "Ultra_pro")
API_ID = int(getenv("API_ID", "23489281"))
API_HASH = getenv("API_HASH", "5fd3d83fa943f0f3d05bf1964a6d77f3")
OWNER_NAME = getenv("OWNER_NAME", "Ultra Max Music")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "ultrapromusic")
BOT_USERNAME = getenv("BOT_USERNAME", "ultra_music_pro_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ultra Max Music")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ultramisic")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ultramisic")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6048367290").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
