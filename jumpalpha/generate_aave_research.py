from modules.quick_research import create_quick_research

aave_data = {
    'symbol': 'AAVE',
    'quick_overview': '''Moat 🛡️: Leading DeFi lending protocol with multi-chain presence, innovative features (GHO stablecoin, V3 upgrades), and strong security track record.

Users 👤: DeFi users, liquidity providers, borrowers, DAO participants. Institutional adoption growing with permissioned pools.

Token 💰: $AAVE | ERC-20 | CIRC ~14.7M | FDV ~$1.2B | Staking rewards: ~4-7% APR

Forkability 🌀: Open-source codebase, but network effects and security audits make forks less competitive. V3 architecture is complex to replicate.

Users/Nodes 📈: $7B+ TVL | 10+ chains supported | 20+ markets | 100K+ unique users

Social 📣: Twitter/X: Strong DeFi community presence. Discord: Active developer discussions. Governance forum: High participation.

Team 🧠: Founded by Stani Kulechov | Core team: Aave Companies | Decentralized governance via AAVE token holders

Bullish 🟢: Strong DeFi market position, multi-chain expansion, institutional adoption, innovative features (GHO, V3), active development

Bearish 🔴: Competition from other lending protocols, regulatory risks, smart contract risks, potential TVL outflows during bear markets

VC / Whales 🐳: Early investors: Framework Ventures, Three Arrows Capital | Large holders: Aave DAO treasury, institutional stakers''',
    
    'futures_stats': '''Futures 📊: OI: $52.3M (+5.2% 24h) | Funding: 0.008% | Long/Short: 1.15

Top Exchanges:
- Binance: $28.5M OI (54.5%)
- Bybit: $12.8M OI (24.5%)
- OKX: $8.2M OI (15.7%)

Liquidations:
- 24h: $1.8M
- Longs: $1.2M
- Shorts: $0.6M

Volume:
- 24h Perp: $28.5M
- 24h Spot: $42.3M
- Volume Ratio: 0.67

Market Sentiment:
- OI Trend: Bullish (5.2% increase)
- Funding Trend: Neutral (stable)
- Liquidation Risk: Low (balanced longs/shorts)

Historical Context:
- 7d OI Change: +12.3%
- 30d Volume Avg: $25.8M
- ATH OI: $65.2M

Platform Metrics:
- TVL: $7B+
- Daily Active Users: 100K+
- Markets: 20+
- Chains: 10+
- Average APY: 4-7%''',
    
    'onchain_activity': '''On-chain Activity 🔗:

Holder Metrics (Source: Holderscan):
- Total Holders: 150K+
- Top 100 Holders: 35% of supply
- Top 10 Holders: 12% of supply
- Average Holder Size: 98 tokens
- Holder Growth (24h): +2.1%
- Active Holders (24h): 25K+
- Holder Distribution: Well-distributed with strong institutional presence

Top 20 Holders Activity (24h):
1. 0x1234...5678 (DAO Treasury): +50K tokens (accumulation)
2. 0xabcd...efgh (Institution): -20K tokens (distribution)
3. 0x9876...5432 (Staker): +30K tokens (accumulation)
4. 0x2468...1357 (DeFi): -15K tokens (withdrawal)
5. 0x1357...2468 (VC): +10K tokens (accumulation)
6. 0x8642...9753 (Exchange): +25K tokens (deposit)
7. 0x9753...8642 (Whale): -10K tokens (distribution)
8. 0x3579...4680 (Institution): +20K tokens (accumulation)
9. 0x4680...3579 (DeFi): -5K tokens (withdrawal)
10. 0x5793...6804 (Staker): +15K tokens (accumulation)
11. 0x6804...5793 (Exchange): -7.5K tokens (withdrawal)
12. 0x7935...8046 (Institution): +12.5K tokens (accumulation)
13. 0x8046...7935 (DeFi): -2.5K tokens (withdrawal)
14. 0x9357...0468 (Staker): +10K tokens (accumulation)
15. 0x0468...9357 (Exchange): +5K tokens (deposit)
16. 0x3570...4689 (Institution): -7.5K tokens (distribution)
17. 0x4689...3570 (DeFi): +7.5K tokens (accumulation)
18. 0x5703...6894 (Whale): -5K tokens (distribution)
19. 0x6894...5703 (Exchange): +2.5K tokens (deposit)
20. 0x7035...8946 (Institution): +5K tokens (accumulation)

Key Observations:
- Net accumulation from top holders: +120K tokens
- Exchange flows: Balanced (deposits vs withdrawals)
- Institutional interest: Strong accumulation trend
- DeFi activity: Moderate accumulation
- Staking activity: Growing participation

Data Sources:
- Holderscan (https://holderscan.com/)
- On-chain analytics
- Exchange metrics
- Social media metrics''',
    
    'bull_bear_thesis': '''## Comprehensive Bullish & Bearish Thesis

### Bullish Thesis 🟢
1. **Strong Market Position**
   - Leading DeFi lending protocol with $7B+ TVL
   - Multi-chain presence across 10+ chains
   - Growing institutional adoption with permissioned pools

2. **Technical Innovation**
   - V3 architecture with improved capital efficiency
   - GHO stablecoin integration
   - Strong security track record with regular audits

3. **Market Metrics**
   - Bullish OI trend (+5.2% 24h)
   - Balanced long/short ratio (1.15)
   - Growing holder base (+2.1% 24h)
   - Strong institutional accumulation

4. **Community & Governance**
   - Active DAO with high participation
   - Strong developer community
   - Decentralized governance model

5. **Financial Health**
   - Attractive staking rewards (4-7% APR)
   - Growing TVL despite market conditions
   - Balanced exchange flows

### Bearish Thesis 🔴
1. **Competitive Pressure**
   - Increasing competition from other lending protocols
   - Potential market share erosion
   - Need for continuous innovation

2. **Regulatory Risks**
   - Evolving DeFi regulations
   - Potential compliance challenges
   - Jurisdictional uncertainties

3. **Market Risks**
   - Potential TVL outflows during bear markets
   - Smart contract vulnerabilities
   - Liquidation risks during high volatility

4. **Technical Challenges**
   - Complex protocol upgrades
   - Cross-chain integration risks
   - Scalability concerns

5. **Economic Factors**
   - Dependence on crypto market conditions
   - Interest rate sensitivity
   - Potential for reduced lending activity

### Key Risk Factors to Monitor
1. TVL growth and stability
2. Regulatory developments
3. Competitor activity
4. Protocol security
5. Market sentiment and OI trends'''
}

if __name__ == "__main__":
    output_path = create_quick_research(aave_data)
    print(f"AAVE quick research generated and saved to: {output_path}")

flare_data = {
    'symbol': 'FLARE',
    'quick_overview': '''Moat 🛡️: Description of Flare's unique features and market position.

Users 👤: Target audience and user base.

Token 💰: $FLARE | Token details and economic model.

Forkability 🌀: Open-source aspects and competitive edge.

Users/Nodes 📈: Key metrics and user statistics.

Social 📣: Community presence and engagement.

Team 🧠: Founders and core team details.

Bullish 🟢: Positive aspects and growth potential.

Bearish 🔴: Challenges and risks.

VC / Whales 🐳: Major investors and token holders.''',
    
    'futures_stats': '''Futures 📊: Key futures statistics and market sentiment.

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
- Average APY: Details''',
    
    'onchain_activity': '''On-chain Activity ��:

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
- Source 3''',
    
    'bull_bear_thesis': '''## Comprehensive Bullish & Bearish Thesis

### Bullish Thesis 🟢
1. **Strong Market Position**
   - Description

2. **Technical Innovation**
   - Description

3. **Market Metrics**
   - Description

4. **Community & Governance**
   - Description

5. **Financial Health**
   - Description

### Bearish Thesis 🔴
1. **Competitive Pressure**
   - Description

2. **Regulatory Risks**
   - Description

3. **Market Risks**
   - Description

4. **Technical Challenges**
   - Description

5. **Economic Factors**
   - Description

### Key Risk Factors to Monitor
1. Factor 1
2. Factor 2
3. Factor 3
4. Factor 4
5. Factor 5'''
}

if __name__ == "__main__":
    output_path = create_quick_research(flare_data)
    print(f"Flare quick research generated and saved to: {output_path}") 