from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/DUROV"), InlineKeyboardButton("Creator", url="https://telegram.me/DUROV") ],
        [InlineKeyboardButton(
            "🍿 mode 🍿", url="https://AMAZON.com/DEAD/YoutubeD")]
    ])
    welcomed = f"""Hey <b>{message.from_user.first_name}</b>\nA Simple YouTot that can:
  ➠ Doe videos
  ➠ Download videos \n\n Made with  by @DUROV"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
