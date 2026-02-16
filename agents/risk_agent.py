from llm import call_llm

def risk_agent(user_input):
    prompt = f"""
    You are a motor insurance fraud analyst.

    Assess if claim looks suspicious.

    Claim:
    {user_input}

    Respond in ONE short sentence only.
    """

    return call_llm(prompt, max_tokens=40)
