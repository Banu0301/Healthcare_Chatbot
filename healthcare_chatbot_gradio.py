from autogen import AssistantAgent, UserProxyAgent

# Your OpenAI API key
OPENAI_API_KEY = ""

# Config for GPT-4
config_list = [
    {
        "model": "gpt-4",
        "api_key": OPENAI_API_KEY
    }
]

# Agent 1: Healthcare assistant
healthcare_bot = AssistantAgent(
    name="HealthcareBot",
    system_message=(
        "You are a friendly virtual healthcare assistant. "
        "Provide general advice about symptoms and home care. "
        "Suggest seeing a doctor if symptoms are serious."
    ),
    llm_config={"config_list": config_list, "temperature": 0.5},
)

# Agent 2: Fact checker to verify medical info
fact_checker_bot = AssistantAgent(
    name="FactCheckerBot",
    system_message=(
        "You fact-check medical and healthcare information. "
        "Verify that the healthcare assistant’s responses are accurate and safe."
    ),
    llm_config={"config_list": config_list, "temperature": 0},
)

# User agent
user = UserProxyAgent(
    name="User",
    human_input_mode="TERMINAL"
)

# Simulate conversation between agents and user
def multi_agent_chat():
    # User initiates conversation
    user_msg = "I have a sore throat and fever. Should I take antibiotics?"
    print(f"User: {user_msg}")

    # HealthcareBot responds
    healthcare_reply = healthcare_bot.generate_reply(
        messages=[{"role": "user", "content": user_msg}]
    )
    print(f"HealthcareBot: {healthcare_reply}")

    # FactCheckerBot verifies HealthcareBot's response
    fact_check_reply = fact_checker_bot.generate_reply(
        messages=[
            {"role": "system", "content": "Fact-check the following response:"},
            {"role": "assistant", "content": healthcare_reply}
        ]
    )
    print(f"FactCheckerBot: {fact_check_reply}")

if __name__ == "__main__":
    multi_agent_chat()
