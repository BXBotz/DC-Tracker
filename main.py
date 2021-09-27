import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
 
Telegram = Client(
    "DC Tracker Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Telegram.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

START_TEXT = """🎸 Your Telegram DC Is : `{}`"""
START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('♻️ Updates Channel ♻️', url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")
             ]]
        )

Telegram.run()
