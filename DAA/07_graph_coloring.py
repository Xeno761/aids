def graph_coloring(graph, num_vertices):
    """
    Graph Coloring using Greedy Method: Assign minimum colors to vertices
    Time Complexity: O(V² + E) | Space Complexity: O(V)
    Greedy doesn't guarantee chromatic number but gives practical solution
    """
    # Initialize color array with -1 (uncolored)
    colors = [-1] * num_vertices
    
    # Assign first color to first vertex
    colors[0] = 0
    
    # Track available colors for each vertex
    available_colors = [False] * num_vertices
    
    # Assign colors to remaining vertices
    for vertex in range(1, num_vertices):
        # Reset available colors
        available_colors = [False] * num_vertices
        
        # Mark colors of adjacent vertices as unavailable
        for adjacent in range(num_vertices):
            if graph[vertex][adjacent] and colors[adjacent] != -1:
                available_colors[colors[adjacent]] = True
        
        # Find first available color
        color = 0
        while color < len(available_colors):
            if not available_colors[color]:
                break
            color += 1
        
        # Assign color to current vertex
        colors[vertex] = color
    
    return colors

def print_graph_coloring(colors):
    """Helper: Display coloring result"""
    print("Vertex -> Color Assignment:")
    for vertex in range(len(colors)):
        print(f"Vertex {vertex} -> Color {colors[vertex]}")

# Driver code
if __name__ == "__main__":
    # Adjacency matrix representation of graph
    graph = [
        [False, True, True, True],      # Vertex 0: connected to 1,2,3
        [True, False, True, False],     # Vertex 1: connected to 0,2
        [True, True, False, True],      # Vertex 2: connected to 0,1,3
        [True, False, True, False]      # Vertex 3: connected to 0,2
    ]
    
    num_vertices = 4
    colors = graph_coloring(graph, num_vertices)
    print_graph_coloring(colors)
    print(f"Chromatic Number (colors used): {max(colors) + 1}")
