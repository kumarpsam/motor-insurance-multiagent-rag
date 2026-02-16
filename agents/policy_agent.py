from llm import call_llm
from rag import retrieve_context

def policy_agent(user_input):
    context = retrieve_context(user_input)

    prompt = f"""
    You are a UK motor insurance validator.

    Use the following policy document context:

    {context}

    Claim Details:
    {user_input}

    Based on policy context, respond in ONE short sentence.
    """

    return call_llm(prompt, max_tokens=60)
