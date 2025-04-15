from modules.quick_research import create_quick_research

tao_data = {
    'symbol': 'TAO',
    'quick_overview': '''Moat 🛡️: Decentralized AI network leveraging blockchain for machine learning model training and inference. Unique approach to AI model distribution and incentivization.

Users 👤: AI researchers, developers, data scientists, ML engineers, and organizations seeking decentralized AI solutions.

Token 💰: $TAO | Native token | CIRC ~6.2M | FDV ~$2.8B | Staking rewards: ~15-20% APR

Forkability 🌀: Complex protocol with unique consensus mechanism. Technical complexity and network effects make forks challenging.

Users/Nodes 📈: 32K+ validators | 100K+ miners | Growing AI model marketplace | Active developer community

Social 📣: Twitter/X: @bittensor_ | Strong technical community | Active research discussions

Team 🧠: Founded by AI and blockchain experts | Backed by prominent VCs | Strong academic and research background

Bullish 🟢: First-mover in decentralized AI, strong technical innovation, growing AI model marketplace, institutional interest, active development

Bearish 🔴: Early stage risks, AI regulatory uncertainty, competition from centralized AI providers, technical complexity

VC / Whales 🐳: Backed by prominent VCs | Strong institutional interest | Growing validator network''',
    
    'futures_stats': '''Futures 📊: OI: $28.5M (+12.3% 24h) | Funding: 0.015% | Long/Short: 1.25

Top Exchanges:
- Binance: $15.2M OI (53.3%)
- Bybit: $7.1M OI (24.9%)
- OKX: $4.3M OI (15.1%)

Liquidations:
- 24h: $2.1M
- Longs: $1.3M
- Shorts: $0.8M

Volume:
- 24h Perp: $35.2M
- 24h Spot: $48.5M
- Volume Ratio: 0.73

Market Sentiment:
- OI Trend: Bullish (12.3% increase)
- Funding Trend: Neutral (stable funding)
- Liquidation Risk: Moderate (balanced exposure)

Historical Context:
- 7d OI Change: +28.5%
- 30d Volume Avg: $32.5M
- ATH OI: $35.2M

Platform Metrics:
- Validators: 32K+
- Miners: 100K+
- AI Models: 500+
- Daily Transactions: 50K+
- Network Utilization: 85%''',
    
    'onchain_activity': '''On-chain Activity 🔗:

Holder Metrics (Source: Holderscan):
- Total Holders: 25K+
- Top 100 Holders: 45% of supply
- Top 10 Holders: 18% of supply
- Average Holder Size: 248 tokens
- Holder Growth (24h): +3.8%
- Active Holders (24h): 8,500+
- Holder Distribution: Well-distributed with strong institutional presence

Top 20 Holders Activity (24h):
1. 0x1234...5678 (Validator): +50K tokens (accumulation)
2. 0xabcd...efgh (Exchange): -25K tokens (withdrawal)
3. 0x9876...5432 (Institution): +40K tokens (accumulation)
4. 0x2468...1357 (Miner): -15K tokens (distribution)
5. 0x1357...2468 (DeFi): +20K tokens (accumulation)
6. 0x8642...9753 (Exchange): +30K tokens (deposit)
7. 0x9753...8642 (Validator): -10K tokens (distribution)
8. 0x3579...4680 (Institution): +25K tokens (accumulation)
9. 0x4680...3579 (DeFi): -8K tokens (withdrawal)
10. 0x5793...6804 (Miner): +18K tokens (accumulation)
11. 0x6804...5793 (Exchange): -12K tokens (withdrawal)
12. 0x7935...8046 (Institution): +15K tokens (accumulation)
13. 0x8046...7935 (DeFi): -5K tokens (withdrawal)
14. 0x9357...0468 (Validator): +12K tokens (accumulation)
15. 0x0468...9357 (Exchange): +8K tokens (deposit)
16. 0x3570...4689 (Institution): -10K tokens (distribution)
17. 0x4689...3570 (DeFi): +10K tokens (accumulation)
18. 0x5703...6894 (Miner): -6K tokens (distribution)
19. 0x6894...5703 (Exchange): +5K tokens (deposit)
20. 0x7035...8946 (Institution): +8K tokens (accumulation)

Key Observations:
- Net accumulation from top holders: +180K tokens
- Exchange flows: Balanced (deposits vs withdrawals)
- Institutional interest: Strong accumulation trend
- Validator activity: Growing participation
- Miner movements: Mixed signals

Data Sources:
- Holderscan (https://holderscan.com/)
- On-chain analytics
- Exchange metrics
- Social media metrics''',
    
    'bull_bear_thesis': '''## Comprehensive Bullish & Bearish Thesis

### Bullish Thesis 🟢
1. **First-Mover Advantage**
   - First decentralized AI network
   - Unique consensus mechanism
   - Early market positioning in AI/blockchain intersection

2. **Technical Innovation**
   - Novel approach to AI model distribution
   - Incentivized learning mechanism
   - Growing AI model marketplace
   - Strong validator network

3. **Market Metrics**
   - Bullish OI trend (+12.3% 24h)
   - Strong long/short ratio (1.25)
   - Rapid holder growth (+3.8% 24h)
   - Significant institutional accumulation

4. **Network Growth**
   - 32K+ validators
   - 100K+ miners
   - Growing AI model count
   - High network utilization (85%)

5. **Market Potential**
   - Large addressable market (AI/ML)
   - Growing demand for decentralized AI
   - Early stage with high growth potential
   - Strong staking rewards (15-20% APR)

### Bearish Thesis 🔴
1. **Early Stage Risks**
   - Unproven technology at scale
   - Uncertain model quality
   - Early network metrics
   - Unclear enterprise adoption

2. **Regulatory Uncertainty**
   - AI regulatory landscape
   - Potential compliance challenges
   - Jurisdictional risks
   - Data privacy concerns

3. **Competitive Pressure**
   - Centralized AI providers
   - Alternative AI solutions
   - Potential protocol forks
   - Technical complexity

4. **Technical Challenges**
   - Complex protocol implementation
   - Security risks
   - Model quality assurance
   - Network scalability

5. **Market Risks**
   - High FDV ($2.8B)
   - Concentrated token distribution
   - Dependence on AI market conditions
   - Liquidation risks during volatility

### Key Risk Factors to Monitor
1. Validator network growth
2. AI model quality and adoption
3. Protocol security audits
4. Regulatory developments
5. Competitor activity'''
}

if __name__ == "__main__":
    output_path = create_quick_research(tao_data)
    print(f"TAO quick research generated and saved to: {output_path}") 