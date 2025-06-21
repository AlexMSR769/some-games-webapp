from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("7903910159:AAGbuEn31P5GjCsDKhfBJMUprKb0_Cfb4rY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            "🎲 Entrar al menú de juegos",
            web_app=WebAppInfo(url="https://some-games-webapp.vercel.app")
        )
    ]]
    await update.message.reply_text(
        "🎮 *¡Bienvenido a Tus juegos favoritos en Telegram!*\n\nExplora, juega y diviértete sin salir del chat.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
