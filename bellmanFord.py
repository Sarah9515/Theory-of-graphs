'''
0 4 0 0 0
0 0 -2 0 0
0 0 0 3 0
0 0 0 0 2
0 0 0 0 0

'''
import tkinter as tk

def bellman_ford(adjacency_matrix, start_node):
    n = len(adjacency_matrix)
    INF = float('inf')

    # Initialize distances 
    distances = [INF] * n
    distances[start_node] = 0
    

    # Relax edges repeatedly
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                weight = adjacency_matrix[u][v]
                if weight != 0 and distances[u] != INF and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    

    # Check for negative cycles
    for u in range(n):
        for v in range(n):
            weight = adjacency_matrix[u][v]
            if weight != 0 and distances[u] != INF and distances[u] + weight < distances[v]:
                return None, None

    return distances

def on_submit():
    adjacency_matrix = []
    lines = input_text.get("1.0", tk.END).strip().split("\n")

    for line in lines:
        row = [int(x) for x in line.split()]
        adjacency_matrix.append(row)

    start_node = int(start_entry.get())
    distances = bellman_ford(adjacency_matrix, start_node)

    if distances is None:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Cycle negative detecte. pas de plus courte distance.")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "La plus petite distance de {}:\n".format(start_node))
        for i, distance in enumerate(distances):
            result_text.insert(tk.END, "Noeud {}: {}\n".format(i, distance))

        
# Create the main window
window = tk.Tk()
window.title("Bellman-Ford Algorithm")
window.geometry("400x470")

# Create the input label and text box
input_label = tk.Label(window, text="Entrez la matrice d'adjacence :")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the start node label and entry
start_label = tk.Label(window, text="Entrez le noeud de depart :")
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Resultat de bellman ford:")
result_label.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
