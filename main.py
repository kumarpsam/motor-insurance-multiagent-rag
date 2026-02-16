from agents.planner import planner_agent
from agents.policy_agent import policy_agent
from agents.risk_agent import risk_agent
from agents.decision_agent import decision_agent

def main():
    user_input = input("Enter motor claim details: ")

    print("\n--- Planner Agent ---")
    plan = planner_agent(user_input)
    print(plan)

    policy_output = ""
    risk_output = ""

    if plan.get("validate_policy"):
        print("\n--- Policy Agent ---")
        policy_output = policy_agent(user_input)
        print(policy_output)

    if plan.get("assess_risk"):
        print("\n--- Risk Agent ---")
        risk_output = risk_agent(user_input)
        print(risk_output)

    print("\n--- Decision Agent ---")
    decision = decision_agent(policy_output, risk_output)
    print(decision)

if __name__ == "__main__":
    main()
