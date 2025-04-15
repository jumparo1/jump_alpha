# AI Research Bot

## Quick Overview
Jump Alpha is an advanced AI-driven Telegram bot that specializes in on-chain cryptocurrency analysis. It provides real-time insights and analytics, helping users make informed decisions in the crypto market.

## Overview
The AI Research Bot is a Telegram bot designed to perform on-chain analysis and provide insights into various cryptocurrency projects. It leverages multiple modules to gather data, analyze sentiment, and format results for easy consumption.

## Features
- On-chain data analysis
- Sentiment analysis
- Whale and VC tracking
- Markdown and Telegram message formatting

## Setup
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure your API tokens in the `.env` file.
4. Run the bot using `python main.py`.

## Directory Structure
```
ai_research_bot/
├── main.py                      # Telegram bot entrypoint
├── config/
│   └── settings.py              # API keys, constants
│   └── sources.py               # URLs and scraping tools
├── modules/
│   ├── pipeline.py              # Orchestration logic
│   ├── tokenomics.py            # Tokenomics analysis
│   ├── onchain.py               # On-chain analysis
│   ├── sentiment.py             # Sentiment analysis
│   ├── whales_vcs.py            # Whales and VCs analysis
│   └── formatter.py             # Message formatting
├── prompts/
│   └── one_liner.txt            # One-liner prompts
│   └── bull_bear.txt            # Bullish/bearish prompts
├── outputs/                     # Stores research reports and analysis results
├── jump_alpha/                  # Core application logic and modules
├── .env                         # API tokens
├── requirements.txt             # Project dependencies
└── README.md                    # Project overview
```

## License
This project is licensed under the MIT License. 