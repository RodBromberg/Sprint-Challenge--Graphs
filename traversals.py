class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """

    queue = Queue()
    visited_vertices = set()

    queue.enqueue({
        'current_vertex': starting_vertex,
        'path': [starting_vertex]
    })

    while queue.size() > 0:

        current_obj = queue.dequeue()
        current_path = current_obj['path']
        current_vertex = current_obj['current_vertex']
        if current_vertex not in visited_vertices:

            if current_vertex == destination_vertex:
                return current_path

            visited_vertices.add(current_vertex)

            for neighbor_vertex in self.get_neighbors(current_vertex):

                new_path = list(current_path)
                new_path.append(neighbor_vertex)

                queue.enqueue({
                    'current_vertex': neighbor_vertex,
                    'path': new_path
                })
    return None
