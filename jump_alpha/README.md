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
│   └── sources.py               # All URLs + tooling for scraping
├── modules/
│   ├── pipeline.py              # Master orchestration logic
│   ├── tokenomics.py
│   ├── onchain.py
│   ├── sentiment.py
│   ├── whales_vcs.py
│   └── formatter.py             # Markdown / Telegram message builder
├── prompts/
│   └── one_liner.txt
│   └── bull_bear.txt
├── .env                         # API tokens (Telegram, Helius, etc.)
├── requirements.txt
└── README.md
```

## License
This project is licensed under the MIT License. 