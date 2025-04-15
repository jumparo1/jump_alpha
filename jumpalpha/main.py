from modules.scraper import (
    get_homepage_text, 
    get_dexu_data,
    get_artemis_data,
    get_spotonchain_data,
    get_crunchbase_data,
    search_twitter
)
from modules.tokenomics import fetch_tokenomics
from modules.summarizer import generate_one_liner, generate_bull_bear
from pathlib import Path
from telegram import InputFile
from modules.research_agent import run_full_pipeline

def get_project_info():
    print("\nEnter project information:")
    name = input("Project name: ").strip()
    ticker = input("Ticker symbol (if any): ").strip()
    website = input("Website URL: ").strip()
    return {
        "name": name,
        "ticker": ticker,
        "url": website
    }

def run_research(project_info):
    project_name = project_info["name"]
    ticker = project_info["ticker"]
    website_url = project_info["url"]
    
    print(f"\nGathering information for {project_name}...")
    
    # 1. Website Analysis
    homepage_text = get_homepage_text(website_url)
    one_liner = generate_one_liner(homepage_text)
    
    # 2. Tokenomics Analysis
    tokenomics = fetch_tokenomics(project_name, ticker)
    
    # 3. On-chain Metrics
    onchain_metrics = f"""
## Dexu.xyz Analysis
{get_dexu_data(ticker)}

## Artemis.xyz Analysis
{get_artemis_data(project_name)}
"""
    
    # 4. Whale & VC Analysis
    whale_vc_analysis = f"""
## SpotOnChain Analysis
{get_spotonchain_data(ticker)}

## Crunchbase Analysis
{get_crunchbase_data(project_name)}
"""
    
    # 5. Social Media Analysis
    social_analysis = f"""
## Twitter Analysis
{search_twitter(ticker)}
"""
    
    # 6. Bull/Bear Analysis
    bull_bear = generate_bull_bear(one_liner, tokenomics)

    output = f"""# {project_name} Research Summary

## 1. One-liner
{one_liner}

## 2. Website Analysis
{homepage_text}

## 3. Tokenomics
{tokenomics}

## 4. On-chain Metrics
{onchain_metrics}

## 5. Whale & VC Analysis
{whale_vc_analysis}

## 6. Social Media Analysis
{social_analysis}

## 7. Bullish / Bearish Thesis
{bull_bear}
"""
    Path("outputs").mkdir(exist_ok=True)
    output_file = f"outputs/{project_name.lower().replace(' ', '_')}.md"
    with open(output_file, "w") as f:
        f.write(output)
    print(f"\nAnalysis complete! Results saved to {output_file}")

def handle_research(update, context):
    args = context.args
    if not args:
        update.message.reply_text("Usage: /research <project name>")
        return

    name = args[0]
    website = args[1] if len(args) > 1 else None
    twitter = args[2] if len(args) > 2 else None

    file_path = run_full_pipeline(name)

    with open(file_path, "rb") as f:
        update.message.reply_document(document=InputFile(f), filename=file_path.split("/")[-1])

if __name__ == "__main__":
    project_info = get_project_info()
    run_research(project_info)
