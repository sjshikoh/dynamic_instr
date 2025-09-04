from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

key = config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")


#gemimin_client = model_provider and model are needed for configuration at runner level
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

#model 
GEMINI_MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)