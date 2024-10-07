import itertools

def tsp(start, v, graph):
    # Store all vertices except the starting vertex.
    vertices = [i for i in range(v) if i != start]
    
    min_cost = float('inf')
    best_route = []

    # Generate all permutations of vertices.
    for permutation in itertools.permutations(vertices):
        current_cost = 0
        current_route = []

        k = start

        # Calculate the cost of the current permutation.
        for next_vertex in permutation:
            current_cost += graph[k][next_vertex][0]  # Add the edge weight
            current_route.append(graph[k][next_vertex][1])  # Add the edge name
            k = next_vertex

        # Add the cost to return to the starting node.
        current_cost += graph[k][start][0]
        current_route.append(graph[k][start][1])

        # Update the minimum cost and best route if a lower cost is found.
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = current_route

    print(f"Cost: {min_cost}")
    print("Route: " + ", ".join(map(str, best_route)))

if _name_ == "_main_":
    v = int(input())
    e = int(input())

    # Initialize the graph with infinite weights.
    graph = [[(float('inf'), -1) for _ in range(v)] for _ in range(v)]

    # Read edges and store in the graph.
    for _ in range(e):
        name, ver1, ver2, weight = map(int, input().split())
        ver1 -= 1  # Convert to zero-indexed
        ver2 -= 1  # Convert to zero-indexed

        # Update the graph with the minimum weight for each edge.
        if weight < graph[ver1][ver2][0]:
            graph[ver1][ver2] = (weight, name)
            graph[ver2][ver1] = (weight, name)

    # Solve the TSP starting from vertex 0 (which is node 1 in one-indexed input).
    tsp(0, v, graph)