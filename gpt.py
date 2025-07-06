import openai
from config import openai_api_key

openai.api_key = openai_api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Hello Akshat, how are you?"}]
)

print("AI Response:", response['choices'][0]['message']['content'])
