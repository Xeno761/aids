# Graph Coloring (Greedy)
def graph_color(graph):
    colors = {}                         # store color of each node

    for node in graph:
        used = {colors[n] for n in graph[node] if n in colors}  # colors of neighbors

        color = 1
        while color in used:            # find smallest unused color
            color += 1

        colors[node] = color            # assign color

    return colors

graph = {
    0:[1,2], 1:[0,2], 2:[0,1,3], 3:[2]
}
print(graph_color(graph))
