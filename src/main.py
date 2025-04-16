import sys
import os

# Add src directory to sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from agents.research_agent import run_full_pipeline
from utils.formatter import format_telegram_report
from data.scraper import scrape_all_sources

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
        report = run_full_pipeline(name, website, twitter)
        
        # Scrape data from all sources
        scraped_data = scrape_all_sources(name)
        
        # Print the final report
        print(report)

    except Exception as e:
        await update.message.reply_text(f"❌ Error running research: {str(e)}")

def get_peaq_data():
    return scrape_website_data()

def research_ai_wayfinder():
    """Perform research on AIWayfinder using the research_agent template and save the report in the reports folder."""
    token_symbol = "AIW"
    
    # Get the research template
    template = get_research_template(token_symbol)
    
    # Gather data using the run_full_pipeline function
    report_data = run_full_pipeline(token_symbol, website="https://x.com/AIWayfinder")
    
    # Fill in the template with actual data
    filled_report = template.replace("[Insert Date]", "2025-04-14")  # Example of filling in a date
    filled_report = filled_report.replace("[Describe unique features and market position]", report_data['quick_overview'])
    filled_report = filled_report.replace("[Token details and economic model]", report_data['token_details'])
    # Continue replacing placeholders with actual data...

    # Save the report
    filename = save_report(f"{token_symbol} Research Report", filled_report)
    print(f"Report saved as {filename}")

def main():
    token = input("Enter token symbol (e.g., BABY): ").strip().upper()
    report = run_full_pipeline(token)
    print(report)

if __name__ == "__main__":
    main()
