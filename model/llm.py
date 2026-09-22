from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm_model=init_chat_model("gpt-4o-mini",model_provider="openai")

