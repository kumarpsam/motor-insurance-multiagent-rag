from llm import call_llm

def decision_agent(policy_output, risk_output):
    prompt = f"""
    You are a claims decision officer.

    Policy Result:
    {policy_output}

    Risk Result:
    {risk_output}

    Respond with only one word:
    APPROVE / REJECT / ESCALATE
    """

    return call_llm(prompt, max_tokens=20)
