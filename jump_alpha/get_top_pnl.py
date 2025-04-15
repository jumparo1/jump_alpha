import requests
from datetime import datetime

def get_top_pnl(token_address, chain='ethereum'):
    """
    Get top 10 PnL holders for a specific token using DexScreener API
    """
    # DexScreener API endpoint
    DEXSCREENER_API = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    
    try:
        # Get token data from DexScreener
        response = requests.get(DEXSCREENER_API)
        data = response.json()
        
        # Process pairs data
        top_pnl = []
        
        if 'pairs' in data:
            for pair in data['pairs'][:10]:  # Get top 10 pairs
                pnl_data = {
                    'pair_address': pair.get('pairAddress', ''),
                    'base_token': pair.get('baseToken', {}).get('symbol', ''),
                    'quote_token': pair.get('quoteToken', {}).get('symbol', ''),
                    'price_usd': float(pair.get('priceUsd', 0)),
                    'price_native': float(pair.get('priceNative', 0)),
                    'volume_24h': float(pair.get('volume', {}).get('h24', 0)),
                    'liquidity_usd': float(pair.get('liquidity', {}).get('usd', 0)),
                    'price_change_24h': float(pair.get('priceChange', {}).get('h24', 0)),
                    'dex': pair.get('dexId', '')
                }
                top_pnl.append(pnl_data)
        
        # Sort by volume
        top_pnl.sort(key=lambda x: x['volume_24h'], reverse=True)
        
        return top_pnl
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def display_top_pnl(token_address, chain='ethereum'):
    """
    Display top 10 pairs in a formatted way
    """
    top_pnl = get_top_pnl(token_address, chain)
    
    print(f"\nTop 10 Pairs for {token_address}")
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("\nRank | Pair | Price (USD) | 24h Volume | Liquidity (USD) | 24h Change | DEX")
    print("-" * 100)
    
    for i, pair in enumerate(top_pnl, 1):
        print(f"{i:4} | {pair['base_token']}/{pair['quote_token']} | "
              f"${pair['price_usd']:,.4f} | ${pair['volume_24h']:,.2f} | "
              f"${pair['liquidity_usd']:,.2f} | {pair['price_change_24h']:,.2f}% | "
              f"{pair['dex']}")

if __name__ == "__main__":
    # Example usage
    token_address = input("Enter token address: ")
    chain = input("Enter chain (default: ethereum): ") or 'ethereum'
    display_top_pnl(token_address, chain) 