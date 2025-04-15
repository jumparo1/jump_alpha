import requests
from datetime import datetime

def get_current_price(ticker):
    """
    Fetch current price and 24h change from CoinGecko
    """
    try:
        coin_ids = {
            'ETH': 'ethereum',
            'BTC': 'bitcoin',
            'SOL': 'solana'
        }
        
        coin_id = coin_ids.get(ticker.upper(), ticker.lower())
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=false&community_data=false&developer_data=false"
        response = requests.get(url)
        data = response.json()
        
        price = data['market_data']['current_price']['usd']
        change_24h = data['market_data']['price_change_percentage_24h']
        market_cap = data['market_data']['market_cap']['usd']
        total_volume = data['market_data']['total_volume']['usd']
        circulating_supply = data['market_data']['circulating_supply']
        
        change_symbol = "+" if change_24h > 0 else ""
        return {
            'price': f"${price:,.2f} ({change_symbol}{change_24h:.2f}% 24h)",
            'market_cap': f"${market_cap:,.0f}",
            'volume': f"${total_volume:,.0f}",
            'circulating_supply': f"{circulating_supply:,.0f}",
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        }
    except Exception as e:
        return None

def get_tokenomist_data(ticker):
    """
    Format Tokenomist.ai data
    """
    if ticker == 'ETH':
        return """
• No traditional unlocks (not a VC-backed token)
• Current emission rate: ~0.5% annually post-merge
• Staking rewards: ~4-5% APR
• No vesting schedules (fair launch)"""
    return "Data not available"

def get_market_data(price_data):
    """
    Format market data from CoinGecko
    """
    if not price_data:
        return "Error fetching market data"
    
    return f"""
• Market Cap: {price_data['market_cap']}
• 24h Volume: {price_data['volume']}
• Circulating Supply: {price_data['circulating_supply']} tokens
• Price: {price_data['price']}"""

def fetch_tokenomics(project_name, ticker=None):
    """
    Fetch tokenomics data from multiple sources
    """
    if not ticker:
        return "Ticker required for tokenomics data"
        
    price_data = get_current_price(ticker)
    if not price_data:
        return "Error fetching price data"
    
    data = {
        "Last Updated": price_data['timestamp'],
        "Market Data": get_market_data(price_data),
        "Token Metrics (Tokenomist.ai)": get_tokenomist_data(ticker),
        "On-chain Data (Dexu.xyz)": f"""
• Total Holders: {get_holder_count(ticker)}
• Active Addresses (24h): {get_active_addresses(ticker)}
• Top Holder Share: {get_top_holders(ticker)}""",
        "Whale Activity (SpotOnChain)": f"""
• Recent Large Transfers: {get_whale_activity(ticker)}
• Institutional Holdings: {get_institutional_holdings(ticker)}
• Smart Money Flow: {get_smart_money_flow(ticker)}"""
    }
    
    table = "| Category | Details |\n|-----------|----------|\n"
    for category, info in data.items():
        # Replace newlines with <br> for markdown table compatibility
        formatted_info = info.replace('\n', '<br>')
        table += f"| {category} | {formatted_info} |\n"
    return table

# Helper functions for mock data (replace with real API calls later)
def get_holder_count(ticker):
    data = {
        'ETH': '250M+',
        'BTC': '300M+',
        'SOL': '50M+'
    }
    return data.get(ticker.upper(), 'N/A')

def get_active_addresses(ticker):
    data = {
        'ETH': '500K+',
        'BTC': '1M+',
        'SOL': '300K+'
    }
    return data.get(ticker.upper(), 'N/A')

def get_top_holders(ticker):
    data = {
        'ETH': 'Top 100 hold 35%',
        'BTC': 'Top 100 hold 15%',
        'SOL': 'Top 100 hold 45%'
    }
    return data.get(ticker.upper(), 'N/A')

def get_whale_activity(ticker):
    data = {
        'ETH': 'Moderate accumulation',
        'BTC': 'Strong accumulation',
        'SOL': 'Neutral'
    }
    return data.get(ticker.upper(), 'N/A')

def get_institutional_holdings(ticker):
    data = {
        'ETH': 'Growing (Grayscale, 21Shares)',
        'BTC': 'Strong (MicroStrategy, Tesla)',
        'SOL': 'Limited'
    }
    return data.get(ticker.upper(), 'N/A')

def get_smart_money_flow(ticker):
    data = {
        'ETH': 'Net positive',
        'BTC': 'Strong inflow',
        'SOL': 'Neutral'
    }
    return data.get(ticker.upper(), 'N/A')
