from llm import call_llm
import json
import re

def planner_agent(user_input):
    prompt = f"""
    You are a motor insurance claim planner.

    Analyse the claim and decide which checks are required.

    Claim Details:
    {user_input}

    Respond ONLY with valid JSON.
    Do NOT include explanation.
    Do NOT include markdown.
    Output format:

    {{
        "validate_policy": true or false,
        "assess_risk": true or false
    }}
    """

    response = call_llm(prompt, max_tokens=60)

    # Extract JSON safely
    try:
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("No JSON found")

    except Exception as e:
        print("Planner returned invalid JSON. Defaulting to all checks.")
        return {
            "validate_policy": True,
            "assess_risk": True
        }
