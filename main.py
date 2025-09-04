from agents import Runner, set_tracing_disabled, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from my_agent.my_agents import hotel_assistant
# from my_agent.guardrail_agents import guardrail_agent


set_tracing_disabled(True)

try:
    res = Runner.run_sync(
        starting_agent=hotel_assistant,
        input="2+3=? ",
    )

    print(res.final_output)

except InputGuardrailTripwireTriggered as e:
    print(f"Trip Input \n {e}")

except OutputGuardrailTripwireTriggered as e:
    print(f"Trip output \n {e}")

