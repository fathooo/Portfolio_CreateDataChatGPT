import openai
from app.config.environments import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
OPENAI = openai