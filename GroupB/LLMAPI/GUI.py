import tkinter
from dotenv import load_dotenv
from google import genai

load_dotenv()

root = tkinter.Tk()

root.title("Class")
root.geometry('500x500')

entry1 = tkinter.Entry(root, width=80)
entry1.pack()

def ask_gemini():
    client = genai.Client()
    response = client.models.generate_content(
        model="gemma-3-4b-it",
        contents=entry1.get()
    )
    window1.insert(tkinter.END,response.text)


button1 = tkinter.Button(root, text="Prompt", command=ask_gemini)
button1.pack()
window1 = tkinter.Text(root)
window1.pack()


root.mainloop()



