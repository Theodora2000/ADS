# Inspired by:
# https://www.youtube.com/watch?v=kaBX2s3pYO4
# https://www.youtube.com/watch?v=eTaWFhPXPz4
# https://www.youtube.com/watch?v=Ub-fJ-KoBQM


# Define a function to find the parent node of a vertex
def find_parent(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find_parent(parent, parent[vertex])


# Define a function to join two sets of vertices
def union(parent, rank, vertex1, vertex2):
    parent1 = find_parent(parent, vertex1)
    parent2 = find_parent(parent, vertex2)

    if rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    elif rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    else:
        parent[parent2] = parent1
        rank[parent1] += 1


# Define Kruskal's algorithm function
def kruskal(graph):
    edges = []
    minimum_spanning_tree = []

    # Create a set for each vertex
    parent = {vertex: vertex for vertex in graph.keys()}
    rank = {vertex: 0 for vertex in graph.keys()}

    # Convert the graph to a list of edges
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((weight, vertex, neighbor))

    # Sort the edges by weight
    edges.sort()

    # Add edges to the minimum spanning tree, avoiding cycles
    for edge in edges:
        weight, vertex1, vertex2 = edge

        if find_parent(parent, vertex1) != find_parent(parent, vertex2):
            minimum_spanning_tree.append(edge)
            union(parent, rank, vertex1, vertex2)

    return minimum_spanning_tree


graph_matrix = []

file1 = open("data_kruskal.txt", "r")
Lines = file1.readlines()

for line in Lines:
    list_of_strings = line.split(" ")
    list_of_integers = list(map(int, list_of_strings))
    graph_matrix.append(list_of_integers)

graph = {}

for i in range(len(graph_matrix)):
    for j in range(len(graph_matrix[i])):
        if graph_matrix[i][j] != 0:
            if i not in graph:
                graph[i] = {}
            graph[i][j] = graph_matrix[i][j]

minimum_spanning_tree = kruskal(graph)

print(minimum_spanning_tree)
