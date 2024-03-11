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

def dfs(list_adjacence, start_noeud):
    visite = set()
    traverse = []

    def dfs_helper(noeud):
        visite.add(noeud)
        traverse.append(noeud)

        neighbors = list_adjacence.get(noeud, [])
        for neighbor in neighbors:
            if neighbor not in visite:
                dfs_helper(neighbor)

    dfs_helper(start_noeud)
    return traverse

def on_submit():
    list_adjacence = {}
    lines = input_text.get("1.0", tk.END).strip().split("\n")

    for line in lines:
        noeud, *voisins = line.split()
        list_adjacence[noeud] = voisins

    start_noeud = start_entry.get()
    result = dfs(list_adjacence, start_noeud)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END,result)

# Create the main window
window = tk.Tk()
window.title("DFS Algorithm")
window.geometry("400x400")

# Create the input label and text box
input_label = tk.Label(window, text="Enter la liste d'adjacence:")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the start node label and entry
start_label = tk.Label(window, text="Enter le noeud de depart:")
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Resultat de DFS:")
result_label.pack()

result_text = tk.Text(window, height=5, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
