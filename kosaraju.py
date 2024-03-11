'''
0 1 1 0 0
0 0 0 1 0
0 0 0 0 1
0 0 0 0 0
0 1 0 0 0

'''
import tkinter as tk
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited, stack)

        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)

        for v in self.graph:
            for neighbor in self.graph[v]:
                g.add_edge(neighbor, v)

        return g

    def print_scc(self, scc):
        result_text.insert(tk.END, "Les composants fortement connectés :\n")
        for component in scc:
            result_text.insert(tk.END, str(component) + "\n")

    def kosaraju(self):
        visited = [False] * self.V
        stack = []

        for v in range(self.V):
            if not visited[v]:
                self.DFS(v, visited, stack)

        transpose = self.get_transpose()

        visited = [False] * self.V
        strongly_connected_components = []

        while stack:
            v = stack.pop()

            if not visited[v]:
                scc = []
                transpose.DFS(v, visited, scc)
                strongly_connected_components.append(scc)

        self.print_scc(strongly_connected_components)

def on_submit():
    adjacency_matrix = []
    lines = input_text.get("1.0", tk.END).strip().split("\n")

    for line in lines:
        row = [int(x) for x in line.split()]
        adjacency_matrix.append(row)

    num_nodes = len(adjacency_matrix)
    g = Graph(num_nodes)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                g.add_edge(i, j)

    g.kosaraju()

# Create the main window
window = tk.Tk()
window.title("Kosaraju's Algorithm")
window.geometry("400x420")

# Create the input label and text box
input_label = tk.Label(window, text="Entrez la matrice d'adjacence :")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Resultat de kosaraju:")
result_label.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
