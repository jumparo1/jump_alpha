# $FLARE Quick Research

## Quick Overview
Last Updated: 2025-04-14 17:46 UTC

Moat 🛡️: Description of Flare's unique features and market position.

Users 👤: Target audience and user base.

Token 💰: $FLARE | Token details and economic model.

Forkability 🌀: Open-source aspects and competitive edge.

Users/Nodes 📈: Key metrics and user statistics.

Social 📣: Community presence and engagement.

Team 🧠: Founders and core team details.

Bullish 🟢: Positive aspects and growth potential.

Bearish 🔴: Challenges and risks.

VC / Whales 🐳: Major investors and token holders.

## Futures Stats
Futures 📊: Key futures statistics and market sentiment.

Top Exchanges:
- Exchange 1: Details
- Exchange 2: Details

Liquidations:
- 24h: Details

Volume:
- 24h Perp: Details
- 24h Spot: Details

Market Sentiment:
- OI Trend: Details
- Funding Trend: Details
- Liquidation Risk: Details

Historical Context:
- 7d OI Change: Details
- 30d Volume Avg: Details
- ATH OI: Details

Platform Metrics:
- TVL: Details
- Daily Active Users: Details
- Markets: Details
- Chains: Details
- Average APY: Details

## On-chain Activity
On-chain Activity 🔗:

Holder Metrics:
- Total Holders: Details
- Top 100 Holders: Details
- Top 10 Holders: Details
- Average Holder Size: Details
- Holder Growth (24h): Details
- Active Holders (24h): Details
- Holder Distribution: Details

Top 20 Holders Activity (24h):
1. Address 1: Activity
2. Address 2: Activity
...

Key Observations:
- Net accumulation: Details
- Exchange flows: Details
- Institutional interest: Details
- DeFi activity: Details
- Staking activity: Details

Data Sources:
- Source 1
- Source 2
- Source 3 

from modules.quick_research import create_quick_research

def generate_research_report(symbol, quick_overview, futures_stats, onchain_activity, bull_bear_thesis):
    data = {
        'symbol': symbol,
        'quick_overview': quick_overview,
        'futures_stats': futures_stats,
        'onchain_activity': onchain_activity,
        'bull_bear_thesis': bull_bear_thesis
    }
    output_path = create_quick_research(data)
    print(f"{symbol} quick research generated and saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    # Placeholder data for demonstration
    symbol = 'FLARE'
    quick_overview = '''Moat 🛡️: Description of Flare's unique features and market position.'''
    futures_stats = '''Futures 📊: Key futures statistics and market sentiment.'''
    onchain_activity = '''On-chain Activity 🔗: Holder Metrics and Key Observations.'''
    bull_bear_thesis = '''## Comprehensive Bullish & Bearish Thesis'''

    generate_research_report(symbol, quick_overview, futures_stats, onchain_activity, bull_bear_thesis) 