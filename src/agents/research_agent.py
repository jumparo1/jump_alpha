# pipeline.py
# This module handles the master orchestration logic for the AI Research Bot.

from src.utils.formatter import format_report
from src.data.website_scraper import scrape_project_website

def orchestrate_research(token_symbol):
    """Main function to orchestrate the research process."""
    # Get the research template
    template = get_research_template(token_symbol)
    
    # Here you would gather actual data and replace placeholders in the template
    filled_report = template.replace("[Insert Date]", "2025-04-14")  # Example of filling in a date
    
    # Save the report
    filename = save_report(f"{token_symbol} Research Report", filled_report)
    print(f"Report saved as {filename}")

def save_report(name: str, content: str):
    filename = f"reports/{name.lower().replace(' ', '_')}.md"
    with open(filename, "w") as f:
        f.write(content)
    return filename


def run_full_pipeline(name, website=None, twitter=None):
    # Scrape the project website if a URL is provided
    website_info = scrape_project_website(website) if website else {}

    # Your real data gathering here
    report = {
        "symbol": name,
        "quick_overview": "Quick overview content...",
        "futures_stats": "Futures stats content...",
        "onchain_activity": "On-chain activity content...",
        "profitable_holders": "Profitable holders content...",
        "bull_bear_thesis": "Bull/Bear thesis content...",
        "moat_summary": f"{website_info.get('headline', 'N/A')} — {website_info.get('description', 'N/A')}",
        "user_profile": website_info.get("paragraph", "N/A")
    }

    return report


# Example usage
# filename = run_full_pipeline("Example Report")
# print(f"Report saved as {filename}")

# Add additional orchestration functions and logic here.

def get_research_template(token_symbol):
    """
    Returns a structured research template for the specified token.
    
    Args:
        token_symbol (str): The symbol of the token for which the research is being generated.
    
    Returns:
        str: A formatted research template with placeholders for data.
    """
    template = f"""# {token_symbol} Quick Research

## Quick Overview
Last Updated: [Insert Date]

Moat 🛡️: [Describe unique features and market position].

Users 👤: [Describe target audience and user base].

Token 💰: {token_symbol} | [Token details and economic model].

Forkability 🌀: [Open-source aspects and competitive edge].

Users/Nodes 📈: [Key metrics and user statistics].

Social 📣: [Community presence and engagement].

Team 🧠: [Founders and core team details].

Bullish 🟢: [Positive aspects and growth potential].

Bearish 🔴: [Challenges and risks].

VC / Whales 🐳: [Major investors and token holders].

## Futures Stats
Futures 📊: [Key futures statistics and market sentiment].

Top Exchanges:
- [Exchange 1]: [Details]
- [Exchange 2]: [Details]

Liquidations:
- 24h: [Details]

Volume:
- 24h Perp: [Details]
- 24h Spot: [Details]

Market Sentiment:
- OI Trend: [Details]
- Funding Trend: [Details]
- Liquidation Risk: [Details]

Historical Context:
- 7d OI Change: [Details]
- 30d Volume Avg: [Details]
- ATH OI: [Details]

Platform Metrics:
- TVL: [Details]
- Daily Active Users: [Details]
- Markets: [Details]
- Chains: [Details]
- Average APY: [Details]

## On-chain Activity
On-chain Activity 🔗:

Holder Metrics:
- Total Holders: [Details]
- Top 100 Holders: [Details]
- Top 10 Holders: [Details]
- Average Holder Size: [Details]
- Holder Growth (24h): [Details]
- Active Holders (24h): [Details]
- Holder Distribution: [Details]

Top 20 Holders Activity (24h):
1. [Address 1]: [Activity]
2. [Address 2]: [Activity]
...

Key Observations:
- Net accumulation: [Details]
- Exchange flows: [Details]
- Institutional interest: [Details]
- DeFi activity: [Details]
- Staking activity: [Details]

Data Sources:
- [Source 1]
- [Source 2]
- [Source 3]
"""
    return template 