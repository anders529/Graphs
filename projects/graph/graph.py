"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            raise KeyError(f'vertex {vertex_id} has already been added')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError(f'vertex {v1} and/or {v2} not in vertices')
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        if vertex_id not in self.vertices:
            raise IndexError(f'vertex {vertex_id} does not exist')
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        qsm = Queue()
        qsm.enqueue(starting_vertex)
        stay = set()
        while qsm.size() > 0:
            current = qsm.dequeue()
            if current not in stay:
                print(current)
                stay.add(current)
                assholes = self.get_neighbors(current)
                for dick in assholes:
                    qsm.enqueue(dick)

    def dft(self, starting_vertex):
        steak = Stack()
        steak.push(starting_vertex)
        stay = set()
        while steak.size() > 0:
            current = steak.pop()
            if current not in stay:
                print(current)
                stay.add(current)
                assholes = self.get_neighbors(current)
                for dick in assholes:
                    steak.push(dick)

    def dft_recursive(self, starting_vertex, stay=set()):
        stay.add(starting_vertex)
        print(starting_vertex)
        for dick in self.get_neighbors(starting_vertex):
            if dick not in stay:
                self.dft_recursive(dick, stay)

    def bfs(self, starting_vertex, destination_vertex):
        qsm = Queue()
        qsm.enqueue([starting_vertex])
        stay = set()
        while qsm.size() > 0:
            current = qsm.dequeue()
            vertex = current[-1]
            if vertex not in stay:
                if vertex == destination_vertex:
                    return current
                stay.add(vertex)
                for dick in self.get_neighbors(vertex):
                    paths = current.copy()
                    paths.append(dick)
                    qsm.enqueue(paths)

    def dfs(self, starting_vertex, destination_vertex):
        steak = Stack()
        steak.push([starting_vertex])
        stay = set()
        while steak.size() > 0:
            current = steak.pop()
            vertex = current[-1]
            if vertex not in stay:
                if vertex == destination_vertex:
                    return current
                stay.add(vertex)
                for dick in self.get_neighbors(vertex):
                    path = current.copy()
                    path.append(dick)
                    steak.push(path)

    def dfs_recursive(self, vertex, destination_vertex, paths=[], stay=set()):
        stay.add(vertex)
        if vertex == destination_vertex:
            return paths
        if len(paths) == 0:
            paths.append(vertex)
        assholes = self.get_neighbors(vertex)
        for dick in assholes:
            if dick not in stay:
                results = self.dfs_recursive(
                    dick, destination_vertex, paths + [dick], stay)
                if results is not None:
                    return results

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
