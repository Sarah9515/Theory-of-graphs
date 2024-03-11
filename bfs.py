'''
A B C
B D E
C F
D G
E H
F
G
H

'''
import tkinter as tk
from collections import deque

def bfs(list_adjacence, start_noeud):
    visite = set()
    queue = deque([start_noeud])
    traverse = []

    while queue:
        noeud = queue.popleft()
        if noeud not in visite:
            visite.add(noeud)
            traverse.append(noeud)
            voisines = list_adjacence.get(noeud, [])
            queue.extend(voisines)

    return traverse

def on_submit():
    list_adjacence = {}
    lines = input_text.get("1.0", tk.END).strip().split("\n")
    
    for line in lines: 
        noeud, *voisines = line.split()
        list_adjacence[noeud] = voisines
    
    start_noeud = start_entry.get()
    result = bfs(list_adjacence, start_noeud)
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("BFS Algorithm")
window.geometry("400x400")

# Create the input label and text box
input_label = tk.Label(window, text="Entrez la liste d'adjacence :")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the start node label and entry
start_label = tk.Label(window, text="Entez le noeud de depart :")
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Le resultat de BFS :")
result_label.pack()

result_text = tk.Text(window, height=5, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
