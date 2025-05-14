import tkinter as tk

class SimpleApp:
    def __init__(self):
        self.user_input = None

    def run(self):
        # Create the window
        self.root = tk.Tk()
        self.root.title("Simple Tkinter App")

        # Label
        label = tk.Label(self.root, text="Enter something:")
        label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack(pady=10)

        # Start the event loop
        self.root.mainloop()

        return self.user_input

    def submit(self):
        self.user_input = self.entry.get()
        self.root.destroy()

