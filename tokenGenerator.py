import hashlib
import secrets
import os
import time
import tkinter as tk
from tkinter import ttk
import sys

def generate_sha256_tokens(num_tokens=100):
    tokens = []
    for _ in range(num_tokens):
        # Generate random bytes
        random_bytes = secrets.token_bytes(32)
        # Create SHA512 hash

        sha512_hash = hashlib.sha512(random_bytes).hexdigest()[:30]
        tokens.append(sha512_hash)

    # Save tokens to file
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (exe)
        current_dir = os.path.dirname(sys.executable)
    else:
        # If the application is run from a Python interpreter
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
    tokens_dir = os.path.join(current_dir, 'tokens')
    os.makedirs(tokens_dir, exist_ok=True)
    output_file = os.path.join(tokens_dir, f'generated_tokens_{len(tokens)}.txt')

    timestamp = str(int(time.time()))
    with open(output_file.replace('.txt', f'_{timestamp}.txt'), 'w') as f:
        for token in tokens:
            f.write(f"{token}\n")
    return "Tokens have been generated and saved successfully!"

def create_ui():
    root = tk.Tk()
    root.title("Token Generator")
    root.geometry("400x200")

    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Number of tokens:").grid(row=0, column=0, padx=5, pady=5)
    token_count = ttk.Entry(frame, width=30)
    token_count.insert(0, "100")
    token_count.grid(row=0, column=1, padx=5, pady=5)

    result_label = ttk.Label(frame, text="")
    result_label.grid(row=2, column=0, columnspan=2, pady=20)

    def generate():
        try:
            num = int(token_count.get())
            result = generate_sha256_tokens(num)
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Please enter a valid number")

    ttk.Button(frame, text="Generate Tokens", command=generate).grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()