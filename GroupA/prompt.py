

from dotenv import load_dotenv
from google import genai
load_dotenv()

## model = gemma-3-1b-it
## model = gemma-3-4b-it
## model = gemma-3-12b-it
## model = gemma-3-27b-it

def ask_gemini(prompt):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemma-3-1b-it",
        contents=prompt
    )
    print(response.text)

while True:
    prompt = input("what do you want to know? (Q fo Quit) ")
    if prompt.upper()=="Q":
        break
    ask_gemini(prompt)


