from pathlib import Path

def prompt_from_file(file, variables={}):
    text = Path(file).read_text()
    for k, v in variables.items():
        text = text.replace(f"<<{k}>>", v)
    return text

def generate_one_liner(homepage_text):
    """
    Generate a one-line summary using Cursor's GPT-4
    """
    prompt = prompt_from_file("prompts/one_liner.txt", {"TEXT": homepage_text})
    # The user will need to manually copy this prompt to Cursor's GPT-4
    print("\nPlease copy this prompt to Cursor's GPT-4 to generate a one-liner:\n")
    print(prompt)
    return input("\nPaste the generated one-liner here: ")

def generate_bull_bear(content, tokenomics):
    """
    Generate bullish/bearish thesis using Cursor's GPT-4
    """
    prompt = prompt_from_file("prompts/bull_bear.txt", {
        "ONE_LINER": content,
        "TOKENOMICS": tokenomics
    })
    # The user will need to manually copy this prompt to Cursor's GPT-4
    print("\nPlease copy this prompt to Cursor's GPT-4 to generate bull/bear thesis:\n")
    print(prompt)
    return input("\nPaste the generated bull/bear thesis here: ")
