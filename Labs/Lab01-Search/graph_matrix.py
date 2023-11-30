import numpy as np

# Example graph matrix
graph_matrix = np.array([[0, 1, 1, 0, 0],
                         [1, 0, 1, 1, 0],
                         [1, 1, 0, 0, 1],
                         [0, 1, 0, 0, 1],
                         [0, 0, 1, 1, 0]])

# Save the graph_matrix to a text file
np.savetxt('graph_matrix.txt', graph_matrix, fmt='%d', delimiter=' ')

# Print a message indicating successful saving
print("Graph matrix saved to 'graph_matrix.txt'")
