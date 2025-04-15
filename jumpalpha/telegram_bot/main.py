import sys
import os

# Add root directory to sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from jumpalpha.modules.research_agent import run_full_pipeline
from jumpalpha.modules.formatter import format_telegram_report
from modules.quick_research import create_quick_research
from modules.scraper import scrape_website_data
from jumpalpha.generate_peaq_research import get_peaq_data

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
async def handle_research(update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /research <project name> [website] [twitter]")
        return

    name = args[0]
    website = args[1] if len(args) > 1 else None
    twitter = args[2] if len(args) > 2 else None

    await update.message.reply_text(f"⏳ Running research on *{name}*...", parse_mode="Markdown")

    try:
        # Run the full research pipeline
        report_data = run_full_pipeline(name, website, twitter)
        
        # Generate and save the research output
        output_path = create_quick_research(report_data)
        await update.message.reply_text(f"Research generated and saved to: {output_path}", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error running research: {str(e)}")

def get_peaq_data():
    return scrape_website_data()

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("research", handle_research))
    print("🤖 JumpAlpha bot is running...")
    app.run_polling()

if __name__ == "__main__":
    peaq_data = get_peaq_data()
    output_path = create_quick_research(peaq_data)
    print(f"PEAQ quick research generated and saved to: {output_path}")
