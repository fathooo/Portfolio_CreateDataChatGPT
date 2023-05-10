from decouple import config

openai_api_key = 'xxxx-xxxx-xxxx-xxxx'

#OPENAI CREDENTIALS
OPENAI_API_KEY = config('OPENAI_API_KEY', default=openai_api_key)
