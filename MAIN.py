import tkinter as tk
from tkinter import ttk
import subprocess

class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Choisir votre algorithme!", font=("Arial", 16))
        self.label.pack(pady=20)

        # Create a frame for the radiobuttons
        self.radio_frame = tk.Frame(self)
        self.radio_frame.pack(pady=10)

        # Create radiobuttons for each page
        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="BFS", value=1, command=lambda: self.open_page("bfs.py"))
        self.page1_radio.pack(side="left", padx=10)

        self.page2_radio = ttk.Radiobutton(self.radio_frame, text="DFS", value=2, command=lambda: self.open_page("dfs.py"))
        self.page2_radio.pack(side="left", padx=10)

        self.page3_radio = ttk.Radiobutton(self.radio_frame, text="WARSHALL", value=3, command=lambda: self.open_page("warshall.py"))
        self.page3_radio.pack(side="left", padx=10)

        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="PRIM", value=1, command=lambda: self.open_page("prim.py"))
        self.page1_radio.pack(side="left", padx=10)

        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="KRUSKAL", value=1, command=lambda: self.open_page("kruskal.py"))
        self.page1_radio.pack(side="left", padx=10)

        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="KUSURAJU", value=1, command=lambda: self.open_page("kosaraju.py"))
        self.page1_radio.pack(side="left", padx=10)

        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="DIJKSTRA", value=1, command=lambda: self.open_page("dijkstra.py"))
        self.page1_radio.pack(side="left", padx=10)

        self.page1_radio = ttk.Radiobutton(self.radio_frame, text="BELLMAN-FORD", value=1, command=lambda: self.open_page("bellmanFord.py"))
        self.page1_radio.pack(side="left", padx=10)

        
    def open_page(self, filename):
        # Run the file in a subprocess
        subprocess.run(["python", filename])

root = tk.Tk()
root.title("Graph Algorithm")
app = MainPage(master=root)
app.mainloop()
