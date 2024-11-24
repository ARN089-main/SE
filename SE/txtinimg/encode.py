from stegano import lsb
from tkinter import *
from tkinter import filedialog, messagebox
import os

def hide_text():
    """Hide text in an image."""
    image_file = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
    if not image_file:
        messagebox.showerror("Error", "No image selected!")
        return

    text_to_hide = text_input.get("1.0", END).strip()
    if not text_to_hide:
        messagebox.showerror("Error", "No text to hide!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not save_path:
        return

    try:
        hidden_img = lsb.hide(image_file, text_to_hide)
        hidden_img.save(save_path)
        messagebox.showinfo("Success", f"Text hidden successfully in {os.path.basename(save_path)}!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to hide text: {e}")

def reveal_text():
    """Reveal text from an image."""
    image_file = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
    if not image_file:
        messagebox.showerror("Error", "No image selected!")
        return

    try:
        revealed_text = lsb.reveal(image_file)
        if revealed_text:
            text_output.delete("1.0", END)
            text_output.insert("1.0", revealed_text)
        else:
            messagebox.showinfo("No Hidden Text", "No hidden text found in the selected image.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reveal text: {e}")

# GUI Setup
app = Tk()
app.title("Steganography Project")
app.geometry("500x400")
app.resizable(False, False)

Label(app, text="Steganography - Hide & Reveal Text in Images", font=("Arial", 16, "bold")).pack(pady=10)

# Input Frame
frame = Frame(app)
frame.pack(pady=20)

Label(frame, text="Enter Text to Hide:", font=("Arial", 12)).grid(row=0, column=0, padx=10, sticky="w")
text_input = Text(frame, height=5, width=40, wrap=WORD)
text_input.grid(row=1, column=0, padx=10, pady=5)

Button(frame, text="Hide Text", command=hide_text, bg="green", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=10)

# Output Frame
Label(app, text="Revealed Text:", font=("Arial", 12)).pack(pady=5)
text_output = Text(app, height=5, width=50, wrap=WORD, bg="#f4f4f4", state="normal")
text_output.pack(pady=5)

# Decode Button
Button(app, text="Reveal Text", command=reveal_text, bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)

app.mainloop()
