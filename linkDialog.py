import tkinter as tk

from platformdirs import user_music_dir

from beat import downloadYTMusic


class SimpleApp:
    def __init__(self):
        self.user_input = None

    def run(self):
        # Create the window
        self.root = tk.Tk()
        self.root.title("Simple Tkinter App")

        # Label
        label = tk.Label(self.root, text="Enter YT LINK:")
        label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack(pady=5)

        # Custom button
        mojsej = tk.Button(self.root, text="Use brano mojsej", command=self.use_custom("./songs/Fernet Cez Internet [AlGVdv7uD98].mp3"))
        axelf = tk.Button(self.root, text="Use axel f", command=self.use_custom("https://www.youtube.com/watch?v=k85mRPqvMbE"))
        rasputin = tk.Button(self.root, text="Use rasputin", command=self.use_custom("https://www.youtube.com/watch?v=16y1AkoZkmQ"))
        mojsej.pack(pady=0)
        axelf.pack(pady=0)
        rasputin.pack(pady=0)

        # Start the event loop
        self.root.mainloop()
        if self.user_input.startswith("https://"):
            return downloadYTMusic(self.user_input)
        return self.user_input

    def submit(self):
        self.user_input = self.entry.get()
        self.root.destroy()

    def use_custom(self,link):
        def internal():
            self.user_input = link
            self.root.destroy()
        return internal
