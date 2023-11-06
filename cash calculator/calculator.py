import tkinter as tk
from tkinter import ttk


def calculate_total():
    try:
        a = int(cash_5_entry.get())
        b = int(cash_10_entry.get())
        c = int(cash_20_entry.get())
        d = int(cash_50_entry.get())
        e = int(cash_100_entry.get())

        total = cash_5 * a + cash_10 * b + cash_20 * c + cash_50 * d + cash_100 * e
        result_label.config(text=f"Total: ${total}")
    except ValueError:
        result_label.config(
            text="Please enter valid integer values for notes.")


# Create the main window
root = tk.Tk()
root.title("Cash Calculator")

# Set the initial window size to be larger
root.geometry("400x300")

# Define cash values
cash_5 = 5
cash_10 = 10
cash_20 = 20
cash_50 = 50
cash_100 = 100

# Increase font size
large_font = ('Arial', 14)

# Create input fields and labels using the pack layout
cash_5_frame = ttk.Frame(root)
cash_5_frame.pack(fill=tk.X, padx=10, pady=5)
cash_5_label = ttk.Label(
    cash_5_frame, text="Number of $5 notes:", font=large_font)
cash_5_label.pack(side=tk.LEFT)
cash_5_entry = ttk.Entry(cash_5_frame, font=large_font)
cash_5_entry.pack(side=tk.RIGHT)
cash_5_entry.insert(0, "0")  # Prefill with 0

cash_10_frame = ttk.Frame(root)
cash_10_frame.pack(fill=tk.X, padx=10, pady=5)
cash_10_label = ttk.Label(
    cash_10_frame, text="Number of $10 notes:", font=large_font)
cash_10_label.pack(side=tk.LEFT)
cash_10_entry = ttk.Entry(cash_10_frame, font=large_font)
cash_10_entry.pack(side=tk.RIGHT)
cash_10_entry.insert(0, "0")  # Prefill with 0

cash_20_frame = ttk.Frame(root)
cash_20_frame.pack(fill=tk.X, padx=10, pady=5)
cash_20_label = ttk.Label(
    cash_20_frame, text="Number of $20 notes:", font=large_font)
cash_20_label.pack(side=tk.LEFT)
cash_20_entry = ttk.Entry(cash_20_frame, font=large_font)
cash_20_entry.pack(side=tk.RIGHT)
cash_20_entry.insert(0, "0")  # Prefill with 0

cash_50_frame = ttk.Frame(root)
cash_50_frame.pack(fill=tk.X, padx=10, pady=5)
cash_50_label = ttk.Label(
    cash_50_frame, text="Number of $50 notes:", font=large_font)
cash_50_label.pack(side=tk.LEFT)
cash_50_entry = ttk.Entry(cash_50_frame, font=large_font)
cash_50_entry.pack(side=tk.RIGHT)
cash_50_entry.insert(0, "0")  # Prefill with 0

cash_100_frame = ttk.Frame(root)
cash_100_frame.pack(fill=tk.X, padx=10, pady=5)
cash_100_label = ttk.Label(
    cash_100_frame, text="Number of $100 notes:", font=large_font)
cash_100_label.pack(side=tk.LEFT)
cash_100_entry = ttk.Entry(cash_100_frame, font=large_font)
cash_100_entry.pack(side=tk.RIGHT)
cash_100_entry.insert(0, "0")  # Prefill with 0

# Create a button to calculate the total
calculate_button = ttk.Button(
    root, text="Calculate Total", command=calculate_total)
calculate_button.pack(fill=tk.X, padx=10, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="", font=large_font)
result_label.pack(fill=tk.X, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
