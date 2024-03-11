'''
0 2 0 1 0
2 0 4 8 0
0 4 0 3 5
1 8 3 0 6
0 0 5 6 0

'''
import tkinter as tk

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

def on_submit():
    adjacency_matrix = []
    lines = input_text.get("1.0", tk.END).strip().split("\n")

    for line in lines:
        row = [int(x) for x in line.split()]
        adjacency_matrix.append(row)

    g = Graph(len(adjacency_matrix))

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0:
                g.add_edge(i, j, adjacency_matrix[i][j])

    result = g.kruskal()

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Arbre couvrant minimum :\n")
    for u, v, w in result:
        result_text.insert(tk.END, "Arc: {}-{}, Poids: {}\n".format(u, v, w))

# Create the main window
window = tk.Tk()
window.title("Kruskal's Algorithm")
window.geometry("400x420")

# Create the input label and text box
input_label = tk.Label(window, text="Entez la matrice d'adjacence :")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Resultat:")
result_label.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
