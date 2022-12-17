## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBUa3P0U8HfcilFtPP84n6M4oTPhSWDqiDR2c-kCa4AMt46xk4TcoTi-Tf8-piRcZfF1JiQPXdoM2Q7zzAA5HdD0oVnnODtWdW_Df8irPCDcd4hbVtEWmiZFQLU4gYuNn-G5Mxk2_q8waPDv6B0FIuMJbugq7XD1Jm3T_t7rmwjbPXlX7QV8EcZb1JIJlncUo4toHovq9DU3egqND9vtWVFgnx_i3eBNpYQ2BfNW3yT0plDV892D3nOW8NGdHKO51yv1ehhtY4PWCEGPKF7WdYct8F6KtdpsHY0WqtR91MHKPSNfa_CXOVc-YaWL8viCNK6Pie4RtkZBE_iqgwuqg9EAAAAAUfAUeYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5489665304:AAG0LMcAZVdhOagSoLpDY9yeeG_A8y-cl4Q")
BOT_NAME = getenv("BOT_NAME", "★彡[AƦTEMꞮDE MUSꞮC]彡★")
API_ID = int(getenv("API_ID", "21849173"))
API_HASH = getenv("API_HASH", "5d4ae6614b45dc890f3cbe3980c493f3")
OWNER_NAME = getenv("OWNER_NAME", "Artemide")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Artemide_assisant")
BOT_USERNAME = getenv("BOT_USERNAME", "Artemide_Musix_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Artemide")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Artemide001")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Artemide001")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5498753510").split()))
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
