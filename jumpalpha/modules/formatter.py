# formatter.py
# This module handles Markdown and Telegram message formatting for the AI Research Bot.

from datetime import datetime

def format_markdown_message(content):
    """Function to format content as a Markdown message."""
    return f"**{content}**"

def format_report(name, tokenomics, sentiment, holders):
    """Function to format the report content."""
    return f"# {name} Report\n\nTokenomics: {tokenomics}\n\nSentiment: {sentiment}\n\nHolders: {holders}\n"

def format_telegram_report(report: dict) -> list[str]:
    """
    Formats a report dictionary into a list of Markdown-formatted message chunks
    ready to send via Telegram (max 4096 chars per message).
    """
    lines = []

    # Header
    lines.append(f"*🧠 JumpAlpha Research Summary*")
    lines.append(f"_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_\n")

    # Token Symbol
    if "symbol" in report:
        lines.append(f"*Token:* `${report['symbol']}`\n")

    # Add sections if available
    section_titles = {
        "quick_overview": "📌 Overview",
        "futures_stats": "📊 Futures",
        "onchain_activity": "🔗 On-Chain Activity",
        "profitable_holders": "💰 Profitable Holders",
        "bull_bear_thesis": "🟢/🔴 Bull vs Bear Thesis"
    }

    for key, title in section_titles.items():
        content = report.get(key)
        if content:
            lines.append(f"*{title}*:\n{content.strip()}\n")

    # Combine everything
    full_message = "\n".join(lines)

    # Telegram max is 4096, we use 4000 buffer
    chunks = [full_message[i:i+4000] for i in range(0, len(full_message), 4000)]

    return chunks

# Add additional formatting functions and logic here. 