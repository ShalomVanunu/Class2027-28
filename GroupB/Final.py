import tkinter as tk
from tkinter import filedialog, messagebox
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# 1. Load API Credentials
load_dotenv()
# Note: Ensure your GOOGLE_API_KEY is in your .env file
client = genai.Client()


def process_image():
    # Step A: User chooses the picture
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.webp"), ("All files", "*.*"))
    )

    if not file_path:
        return

    # Update UI to show processing status
    entry_var.set(f"Processing: {os.path.basename(file_path)}...")
    text_form.delete("1.0", tk.END)
    text_form.insert(tk.END, "Analyzing image, please wait...")
    root.update_idletasks()  # Refresh the window so the message shows up

    try:
        # Step B: Read the selected file
        with open(file_path, 'rb') as f:
            image_bytes = f.read()

        # Step C: Send to Gemini API
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type='image/jpeg',  # Works for most standard formats
                ),
                'Describe this image.'
            ]
        )

        # Step D: Show the result in the text form
        text_form.delete("1.0", tk.END)
        text_form.insert(tk.END, response.text)
        entry_var.set(f"Selected: {os.path.basename(file_path)}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to describe image: {str(e)}")
        text_form.delete("1.0", tk.END)


# --- 2. GUI Setup ---
root = tk.Tk()
root.title("Gemini Image Describer")
root.geometry("600x500")

# Header
header = tk.Label(root, text="AI Image Description Tool", font=("Arial", 14, "bold"), pady=10)
header.pack()

# File Selection Area
upload_frame = tk.Frame(root, pady=10)
upload_frame.pack()

btn_upload = tk.Button(
    upload_frame,
    text="Choose Image & Describe",
    command=process_image,
    bg="#0275d8",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=20,
    pady=5
)
btn_upload.pack()

entry_var = tk.StringVar()
entry_var.set("No file selected")
lbl_file_path = tk.Label(root, textvariable=entry_var, fg="grey", font=("Arial", 9, "italic"))
lbl_file_path.pack()

# Results Area
form_label = tk.Label(root, text="Description Result:", font=("Arial", 10, "bold"))
form_label.pack(pady=(20, 0))

# Adding a scrollbar to the text form
text_frame = tk.Frame(root)
text_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_form = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 10))
text_form.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=text_form.yview)

root.mainloop()