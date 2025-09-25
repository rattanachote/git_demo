from google import genai
import os
from dotenv import load_dotenv # 💡 Import the necessary function

# 1. Load the API key from the .env file into the environment
load_dotenv()

# 2. The client will automatically find the GEMINI_API_KEY environment variable.
client = genai.Client()

# 3. Your content generation call is correct
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)