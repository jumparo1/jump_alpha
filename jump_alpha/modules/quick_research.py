from pathlib import Path
import json
from datetime import datetime

def generate_quick_research(data):
    """
    Generate a quick research summary in markdown format
    """
    template = """# ${symbol} Quick Research

## Quick Overview
{quick_overview}

## Futures Stats
{futures_stats}

## On-chain Activity
{onchain_activity}
"""
    
    return template.format(
        symbol=data['symbol'],
        quick_overview=data['quick_overview'],
        futures_stats=data['futures_stats'],
        onchain_activity=data['onchain_activity']
    )

def create_quick_research(data):
    """
    Create and save quick research to file
    """
    research = generate_quick_research(data)
    Path("outputs").mkdir(exist_ok=True)
    output_path = f"outputs/{data['symbol'].lower()}.md"
    with open(output_path, "w") as f:
        f.write(research)
    return output_path 