class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertices(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
    def get_neighbors(self, vertex):
        return self.vertices[vertex]
def make_graph(ancestors):
    graph = Graph()
    for elder, child in ancestors:
        graph.add_vertices(elder)
        graph.add_vertices(child)
        graph.add_edge(child, elder)
    return graph
def earliest_ancestor(ancestors, starting_node):
    graph = make_graph(ancestors)
    steak = Stack()
    stay = set()
    steak.push([starting_node])
    longest_path = []
    while steak.size() > 0:
        path = steak.pop()
        current_node = path[-1]
        if len(path) > len(longest_path):
            longest_path = path
        if current_node not in stay:
            stay.add(current_node)
            elders = graph.get_neighbors(current_node)
            for e in elders:
                new_path = path+[e]
                steak.push(new_path)
    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]