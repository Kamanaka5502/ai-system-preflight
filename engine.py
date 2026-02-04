from preflight.prompts import PREFLIGHT_PROMPT

def generate_preflight_spec(idea: str) -> str:
    prompt = PREFLIGHT_PROMPT.format(idea=idea)
    # This is where you would call the LLM
    # For now we just return the structured prompt
    return prompt

