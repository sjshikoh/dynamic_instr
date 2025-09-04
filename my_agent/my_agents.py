from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_agent.hotel_data import hotels





def build_instructions(hotel_dict):
    base_intro = """
    You are Yashal Khan, a helpful hotel customer care assistant.
    You provide accurate details about hotels from the database below.
    Rules:
    - Always identify which hotel the user is asking about.
    - If the user does not specify, ask them politely to clarify.
    - Never mix details between hotels.
    - Use only the database below for answers.
    
    Hotel Database:
    """

    hotel_lines = []
    for name, details in hotel_dict.items():
        line = f"\nHotel {name}:"
        for key, value in details.items():
            line += f"\n  - {key.capitalize().replace('_',' ')}: {value}"
        hotel_lines.append(line)

    return base_intro + "\n".join(hotel_lines)


hotel_assistant = Agent(
    name="Hotel Customer Care Assistant",
    instructions=build_instructions(hotels),
    model=GEMINI_MODEL,
   
)


