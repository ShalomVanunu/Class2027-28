from google import genai
from google.genai import types
#import dotenv
from dotenv import load_dotenv


load_dotenv()

with open("images.jpg", 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        'discribe the this image.'
    ]
)

print(response.text)