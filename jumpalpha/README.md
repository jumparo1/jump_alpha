# JumpAlpha

🚀 AI-powered on-chain research assistant. Built to find alpha fast.  
Uses a Telegram bot interface, modular AI agents, and real-time data scraped from the chain + social layer.

---

## 🧠 Agents

- **Research Agent** — project name → full breakdown (tokenomics, holders, social, whales)
- **On-Chain Digger** — wallet tracing, inflows/outflows, PnL
- **Portfolio Watcher** *(soon)* — monitor tokens, alerts, and sentiment changes

---

## 🔧 Tech Stack

- **Python 3.11+** (Cursor IDE)
- **Telegram Bot** via `python-telegram-bot`
- **OpenAI / Cursor GPT** (summarization)
- **Local AI** optional via Ollama
- **Data APIs**:
  - `Tokenomist.ai`, `CoinGecko`
  - `Dexu.xyz`, `Holderscan.com`, `SpotOnChain.com`
  - `Arkham Intelligence`, `Crunchbase`
  - `X / Twitter`, `snscrape`, `Velo.xyz`

---

## 📁 Folder Structure

---

## ✅ Naming Standards

- Folder/module names = lowercase + no underscores  
- Python files = `snake_case.py`  
- Telegram bot logic = lives in `telegram_bot/`  
- All config/global constants = in `config/`  
- Output files = in `reports/`

---

Paste this in Cursor, apply the folder renames, and update your README.md.  
You'll have a clean, pro-level repo under your `jumparo1` profile, branded as **JumpAlpha**.

Let me know when you're ready to expand the `research_agent.py` with working tokenomics or social sentiment logic.

## License
This project is licensed under the MIT License. 