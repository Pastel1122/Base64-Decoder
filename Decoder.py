import base64
from tkinter import Tk, Label, Text, Button, END, messagebox

def decode_base64():
    try:
        encoded_message = input_text.get("1.0", END).strip()
        if not encoded_message:
            messagebox.showwarning("Warning", "Please paste the Base64 encoded message.")
            return
        decoded_message = base64.b64decode(encoded_message).decode('utf-8')
        output_text.delete("1.0", END)
        output_text.insert(END, decoded_message)
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed: {e}")

# Initialize the main window
root = Tk()
root.title("Base64 Decoder - Developed by Frank")
root.geometry("500x400")
root.config(bg="black")

# Heading label
heading = Label(root, text="Base64 Decoder", font=("Helvetica", 16, "bold"), fg="green", bg="black")
heading.pack(pady=10)

# Input label and text area
input_label = Label(root, text="Paste your Base64 encoded message:", font=("Helvetica", 12), fg="white", bg="black")
input_label.pack(anchor="w", padx=10)
input_text = Text(root, height=10, width=60, wrap="word", bg="white", fg="black")
input_text.pack(padx=10, pady=5)

# Decode button
decode_button = Button(root, text="Decode", font=("Helvetica", 12), bg="green", fg="white", command=decode_base64)
decode_button.pack(pady=10)

# Output label and text area
output_label = Label(root, text="Decoded message:", font=("Helvetica", 12), fg="white", bg="black")
output_label.pack(anchor="w", padx=10)
output_text = Text(root, height=10, width=60, wrap="word", bg="white", fg="black")
output_text.pack(padx=10, pady=5)

# Run the application
root.mainloop()
