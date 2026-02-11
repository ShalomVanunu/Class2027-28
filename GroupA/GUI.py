import tkinter as tk
from tkinter import filedialog, messagebox
import os
from dotenv import load_dotenv
from google import genai
from PIL import Image  # Add this back just for the API transfer

load_dotenv()


def ask_gemini(image_path):
    try:
        client = genai.Client()

        # Open the image using PIL (The SDK handles PIL objects perfectly)
        raw_image = Image.open(image_path)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[
                "Analyze this image and describe what is happening in detail.",
                raw_image
            ]
        )
        return response.text
    except Exception as e:
        return f"Error during analysis: {str(e)}"


def run_analysis():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )

    if file_path:
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, f"Selected: {os.path.basename(file_path)}\n")
        text_display.insert(tk.END, "Analyzing content... please wait...\n" + ("-" * 30) + "\n\n")
        root.update_idletasks()

        analysis_result = ask_gemini(file_path)

        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, analysis_result)


# --- UI Setup ---
root = tk.Tk()
root.title("Gemma-3 Image Analyzer")
root.geometry("500x450")

header = tk.Label(root, text="AI Image Processor", font=("Arial", 14, "bold"))
header.pack(pady=10)

analyze_btn = tk.Button(
    root,
    text="Select Image to Analyze",
    command=run_analysis,
    bg="#1a73e8",
    fg="white",
    padx=20,
    pady=10,
    font=("Arial", 10, "bold")
)
analyze_btn.pack(pady=10)

text_display = tk.Text(root, height=15, width=55, wrap=tk.WORD, padx=10, pady=10)
text_display.pack(pady=15, padx=20)

root.mainloop()