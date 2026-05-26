def compare(concept1: str, concept2: str) -> str:
    concept1 = concept1.lower().strip()
    concept2 = concept2.lower().strip()

    pairs = {
        ("dijkstra", "bellman-ford"): (
            "Dijkstra\n"
            "+ Faster\n"
            "+ Positive weights\n"
            "Complexity: O((V+E)logV)\n\n"
            "Bellman-Ford\n"
            "+ Negative weights\n"
            "+ Detects negative cycles\n"
            "Complexity: O(VE)"
        ),
        ("laplace transform", "fourier transform"): (
            "Laplace\n"
            "+ Handles transient signals\n"
            "+ Control systems\n\n"
            "Fourier\n"
            "+ Frequency analysis\n"
            "+ Steady-state systems"
        ),
        ("dfs", "bfs"): (
            "DFS\n"
            "+ Less memory\n"
            "+ Backtracking\n\n"
            "BFS\n"
            "+ Shortest path\n"
            "+ Level traversal"
        ),
    }

    key = (concept1, concept2)
    reverse = (concept2, concept1)

    return pairs.get(key) or pairs.get(reverse, "No comparison found")