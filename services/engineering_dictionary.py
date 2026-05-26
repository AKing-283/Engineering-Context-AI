ENGINEERING_TERMS = {

    "djikstra":
    "Dijkstra",

    "djikstra's algorithm":
    "Dijkstra's Algorithm",

    "bellmanford":
    "Bellman-Ford",

    "bellman ford":
    "Bellman-Ford",

    "dfs":
    "Depth First Search",

    "bfs":
    "Breadth First Search",

    "kcl":
    "Kirchhoff Current Law",

    "kvl":
    "Kirchhoff Voltage Law"

}


def normalize_term(text):

    if not text:

        return text

    lower = text.lower()

    for wrong,correct in ENGINEERING_TERMS.items():

        if wrong in lower:

            return correct

    return text