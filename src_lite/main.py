import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def handle_research(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /research command."""
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /research <token symbol>")
        return

    token = args[0].upper()
    await update.message.reply_text(f"⏳ Researching {token}...")

    try:
        # TODO: Implement research logic using ChatGPT
        report = f"Research report for {token}\n\nThis is a placeholder for ChatGPT integration."
        await update.message.reply_text(report)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    """Start the bot."""
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("research", handle_research))
    app.run_polling() 