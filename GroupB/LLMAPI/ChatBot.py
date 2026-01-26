from dotenv import load_dotenv
from google import genai

load_dotenv()

context = ""

def all_prompt(prompt, context):
    return f""" user : {prompt}
    context : {context} 
      
      """


def ask_gemini(prompt):
    global context
    client = genai.Client()
    response = client.models.generate_content(
        model="gemma-3-4b-it",
        contents=prompt
    )
    context += "\n"+response.text
    return response.text

while True:
    prompt = input("Enter prompt [Q]- Quit \n")
    if prompt == "Q":
        break
    print(ask_gemini(all_prompt(prompt,context)))











