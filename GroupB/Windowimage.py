import tkinter as tk
from tkinter import filedialog, messagebox


def upload_file():
    # Opens the file explorer and returns the path of the selected file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    if file_path:
        # Clear the current text in the form and insert the file path
        # (Or you could read the file content and put it in the text box!)
        entry_var.set(file_path)
        print(f"File selected: {file_path}")


# 1. Setup the main Window
root = tk.Tk()
root.title("File Uploader & Text Form")
root.geometry("500x400")

# 2. File Upload Section
upload_frame = tk.Frame(root, pady=20)
upload_frame.pack()

btn_upload = tk.Button(upload_frame, text="Upload File", command=upload_file, bg="#4CAF50", fg="white", padx=10)
btn_upload.pack(side=tk.LEFT, padx=10)

entry_var = tk.StringVar()
entry_var.set("No file selected")
lbl_file_path = tk.Label(upload_frame, textvariable=entry_var, fg="grey", font=("Arial", 9, "italic"))
lbl_file_path.pack(side=tk.LEFT)

# 3. Text Form Section
form_label = tk.Label(root, text="Enter your comments or data below:", font=("Arial", 10, "bold"))
form_label.pack(pady=(10, 0))

text_form = tk.Text(root, height=10, width=50, padx=10, pady=10)
text_form.pack(pady=10)


# 4. Submit Button (Optional - just to show functionality)
def submit_data():
    content = text_form.get("1.0", tk.END)
    messagebox.showinfo("Success", "Data submitted successfully!")
    print("Form Content:", content)


btn_submit = tk.Button(root, text="Submit Form", command=submit_data)
btn_submit.pack()

root.mainloop()