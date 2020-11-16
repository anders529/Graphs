def earliest_ancestor(ancestors, starting_node):
    graph = make_graph(ancestors)
    steak = Stack()
    stay = set()
    longeset_path = []

    while steak.size() > 0:
        path = steak.pop()
        current_node = path[-1]
        
        if len(path) > len(longeset_path):
            longeset_path = path

        if current_node not in stay:
            stay.add(current_node)
            elders = graph.get_neigbors(current_node)

            for elder in elders:
                new_path = path+[elder]
                steak.push(new_path)
        if starting_node == longeset_path[-1]:
            return -1
        else:
            return longeset_path[-1]