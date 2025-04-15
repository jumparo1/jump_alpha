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
- **Telegram Bot** via 
- **OpenAI / Cursor GPT** (summarization)
- **Local AI** optional via Ollama
- **Data APIs**:
  - , 
  - , , 
  - , 
  - , , 

---

## 📁 Folder Structure

```
jumpalpha/
├── research_agent.py      # Main logic for scraping and orchestrating data
├── tokenomics.py
├── sentiment.py
├── whale_tracker.py
├── formatter.py
config/
├── settings.py            # All keys, constants
├── sources.py             # Centralized data source list
reports/
├── [project].md           # Final output files
telegram_bot/
├── main.py                # Handles /research command
prompts/
├── one_liner.txt
├── bull_bear.txt
.env
README.md
```

---

## ✅ Naming Standards

- Folder/module names = lowercase + no underscores  
- Python files = `snake_case.py`  
- Telegram logic = lives in `telegram_bot/`  
- Config = lives in `config/`  
- Output = goes into `reports/`
