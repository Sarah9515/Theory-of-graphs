'''
0 1 1 0
0 0 0 1
0 0 0 0
1 0 1 0

'''
import tkinter as tk

def warshall(adjacency_matrix):
    n = len(adjacency_matrix)

    # Create a copy of the adjacency matrix
    transitive_closure = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transitive_closure[i][j] = adjacency_matrix[i][j]

    # Perform Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j])

    return transitive_closure

def on_submit():
    adjacency_matrix = []
    lines = input_text.get("1.0", tk.END).strip().split("\n")

    for line in lines:
        row = [int(x) for x in line.split()]
        adjacency_matrix.append(row)

    result = warshall(adjacency_matrix)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Transitive Closure:\n")
    for row in result:
        result_text.insert(tk.END, " ".join(str(x) for x in row) + "\n")

# Create the main window
window = tk.Tk()
window.title("Warshall's Algorithm")
window.geometry("400x430")

# Create the input label and text box
input_label = tk.Label(window, text="Entez la matrice d'incidence :")
input_label.pack()

input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# Create the submit button
submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="Fermeture transitive:")
result_label.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# Run the Tkinter event loop
window.mainloop()
