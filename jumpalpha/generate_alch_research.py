import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Static data for ALCH research
alch_data = {
    "name": "ALCH (Alchemist)",
    "description": "Alchemist is a decentralized protocol on Solana focused on DeFi innovations and community-driven development.",
    
    "moat": """
    - First-mover advantage in several DeFi primitives on Solana
    - Strong community engagement and governance model
    - Innovative tokenomics design with sustainable yield mechanisms
    """,
    
    "users": """
    - Active daily traders: ~2,500+
    - Total unique holders: 15,000+
    - Monthly active users: 8,000+
    """,
    
    "token": {
        "symbol": "ALCH",
        "chain": "Solana",
        "total_supply": "100,000,000",
        "circulating_supply": "~45,000,000",
        "current_price": "$0.1568",
        "market_cap": "$7.04M",
        "fdv": "$15.68M"
    },
    
    "forkability": """
    - Medium difficulty to fork due to:
      - Complex smart contract architecture
      - Strong community network effects
      - Established partnerships and integrations
    """,
    
    "team": """
    - Anonymous but proven track record
    - Active development team with regular updates
    - Strong technical background in Solana ecosystem
    """,
    
    "social": {
        "twitter_followers": {
            "count": "25,000+",
            "change_24h": "+3.2%"
        },
        "discord_members": {
            "count": "15,000+",
            "change_24h": "+1.8%"
        },
        "telegram_members": {
            "count": "8,000+",
            "change_24h": "+2.5%"
        },
        "github_activity": {
            "status": "High",
            "change_24h": "+15 commits"
        }
    },
    
    "bullish": """
    1. Strong growth metrics with increasing TVL and user adoption
    2. High trading volume indicating market interest
    3. Consistent development and feature releases
    4. Multiple DEX integrations showing ecosystem adoption
    5. Positive price performance (+28% 24h change)
    """,
    
    "bearish": """
    1. Anonymous team carries inherent risks
    2. Competition in Solana DeFi space
    3. Market volatility and dependency on SOL ecosystem
    4. Regulatory uncertainties in DeFi space
    """,
    
    "vc_whales": """
    - Notable VCs: Not publicly disclosed
    - Whale concentration: Moderate
    - Top 10 holders control ~35% of supply
    """,
    
    "onchain_analytics": {
        "dex_metrics": {
            "total_24h_volume": "$10.7M",
            "total_liquidity": "$5.8M",
            "top_pairs": [
                {
                    "dex": "Raydium",
                    "pair": "ALCH/SOL",
                    "volume_24h": "$9.7M",
                    "liquidity": "$5.5M",
                    "price": "$0.1568",
                    "change_24h": "+28.06%"
                },
                {
                    "dex": "Meteora",
                    "pair": "ALCH/SOL",
                    "volume_24h": "$774.9K",
                    "liquidity": "$59.5K",
                    "price": "$0.1560",
                    "change_24h": "+27.07%"
                },
                {
                    "dex": "Orca",
                    "pair": "ALCH/SOL",
                    "volume_24h": "$84.6K",
                    "liquidity": "$44.5K",
                    "price": "$0.1583",
                    "change_24h": "+28.73%"
                }
            ],
            "key_observations": [
                "High concentration on Raydium (90% of volume)",
                "Consistent pricing across DEXes ($0.155-0.158)",
                "Strong positive momentum across all pairs",
                "Healthy liquidity distribution",
                "Active trading on multiple DEXes"
            ]
        }
    }
}


def generate_token_metrics(data):
    """Generate token metrics section."""
    return f"""
## Token Metrics
- Symbol: {data['symbol']}
- Chain: {data['chain']}
- Total Supply: {data['total_supply']}
- Circulating Supply: {data['circulating_supply']}
- Current Price: {data['current_price']}
- Market Cap: {data['market_cap']}
- FDV: {data['fdv']}
"""


def generate_social_metrics(data):
    """Generate social metrics section."""
    return f"""
## Social Metrics
- Twitter: {data['twitter_followers']['count']} ({data['twitter_followers']['change_24h']})
- Discord: {data['discord_members']['count']} ({data['discord_members']['change_24h']})
- Telegram: {data['telegram_members']['count']} ({data['telegram_members']['change_24h']})
- Github Activity: {data['github_activity']['status']} ({data['github_activity']['change_24h']})
"""


def generate_research():
    """Generate ALCH research document with on-chain analytics"""
    
    logging.info("Starting research generation for ALCH")
    output = f"""# ALCH Research Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

## Overview
{alch_data['description']}

## Moat{alch_data['moat']}

## Users{alch_data['users']}

"""
    
    output += generate_token_metrics(alch_data['token'])
    output += f"""
## Forkability{alch_data['forkability']}

## Team{alch_data['team']}

"""
    output += generate_social_metrics(alch_data['social'])
    output += f"""
## Bullish Thesis{alch_data['bullish']}

## Bearish Thesis{alch_data['bearish']}

## VC & Whales{alch_data['vc_whales']}

## On-chain Analytics

### DEX Metrics
- Total 24h Volume: {alch_data['onchain_analytics']['dex_metrics']['total_24h_volume']}
- Total Liquidity: {alch_data['onchain_analytics']['dex_metrics']['total_liquidity']}

### Top Trading Pairs
"""
    
    # Add top pairs data
    for pair in alch_data['onchain_analytics']['dex_metrics']['top_pairs']:
        output += f"""
#### {pair['dex']} - {pair['pair']}
- 24h Volume: {pair['volume_24h']}
- Liquidity: {pair['liquidity']}
- Price: {pair['price']}
- 24h Change: {pair['change_24h']}
"""
    
    # Add key observations
    output += "\n### Key Observations\n"
    for observation in alch_data['onchain_analytics']['dex_metrics']['key_observations']:
        output += f"- {observation}\n"
    
    # Write to file
    try:
        with open('outputs/alch.md', 'w') as f:
            f.write(output)
        logging.info("ALCH quick research generated and saved to outputs/alch.md")
    except IOError as e:
        logging.error(f"Error writing to file: {e}")

if __name__ == "__main__":
    generate_research() 