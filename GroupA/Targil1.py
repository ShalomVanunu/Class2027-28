
import os
import tkinter as tk
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
client  = genai.Client(api_key=api_key)

def send_to_gemini(prompt_text):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_text
        )
        return response.text
    except Exception as e:
        return f'שגיאה: {str(e)}'

def create_app():
    window = tk.Tk()
    window.title('Chat with Gemini AI')
    window.geometry('700x500')
    window.configure(bg='#f0f0f0')

    tk.Label(window, text='הכניסו את השאלה שלכם:',
             font=('Arial', 14), bg='#f0f0f0').pack(pady=(20, 5))

    entry = tk.Entry(window, width=60, font=('Arial', 13))
    entry.pack(pady=5)

    output_text = tk.Text(window, height=12, width=75,
                          font=('Arial', 12), wrap=tk.WORD,
                          state='disabled', bg='white')
    output_text.pack(pady=10, padx=20)

    def on_submit():
        prompt = entry.get()
        if not prompt.strip():
            return
        output_text.config(state='normal')
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, '⏳ ממתין לתשובה...')
        output_text.config(state='disabled')
        window.update()
        result = send_to_gemini(prompt)
        output_text.config(state='normal')
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state='disabled')

    tk.Button(window, text='שלח לGemini 🚀',
              font=('Arial', 13, 'bold'), command=on_submit,
              bg='#1A73E8', fg='white', padx=20, pady=8).pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    create_app()

