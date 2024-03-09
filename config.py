import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

STRING_SESSION = getenv("STRING_SESSION", "BQAYv8oAe7ZmfT9jPkWTpgneEitXqLQOoXalJ5hA7bBocYaHOgZ7vGqMb13eAY6dKUGVnUg-BGqM1qsBYl2NWOT8mUvWnukjawuQp2FIGMO7rKvTLdv5xwfPN-QN28sOR3-3fc3xhqtZLJuoqSRamErU6NIl_MVcLrmt4u3AY26AQqCxB3rY216p0TF81TfJxXblwsQmxItS6XPRmbmcWN2K0BZFzwKmpdsz9X5Rk89ZnbVF8jTpq3ILIJHAyFm2gDQfRyuv1yoDu6alOjS5Evxv0S_7xQJH7VqWKVv56ueS2psd6wT5Xh063JgFPyC6iWdVx5Q0tZTRgKIDDoywRnkuBZYTxwAAAAGmimwcAA")
BOT_TOKEN = getenv("BOT_TOKEN", "7146033656:AAG-Y5kHvNvbu0bAYpo0z1qmcpcURu4MGz8")
API_ID = int(getenv("API_ID", "1621962"))
API_HASH = getenv("API_HASH", "6f019552c1cf83dec1851516b1bb099c")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
