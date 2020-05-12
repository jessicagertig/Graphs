"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        ## add edge from v1 to v2

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not have exist in graph.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    
    """START OF TRAVERSALS"""

    """BREADTH FIRST TRAVERSAL"""    
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        ##KEEP TRACK OF VISITED NODES
        visited = set()

        ##REPEAT UNTIL QUEUE IS EMPTY
        while q.size() > 0:

            #DEQUEUE FIRST VERTEX
            v = q.dequeue()

            ##IF IT'S NOT VISITED
            if v not in visited:
                print(v)

            ##MARK AS VISITED
            visited.add(v)

            ##ENQUEUE ITS NEIGHBORS
            for next_vert in self.get_neighbors(v):
                ##Don't get stuck in the 3 & 5 weird loop in this tree
                if next_vert not in visited:
                    q.enqueue(next_vert)

    """DEPTH FIRST TRAVERSAL"""
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        ##KEEP TRACK OF VISITED NODES
        visited = set()

        ##REPEAT UNTIL STACK IS EMPTY
        while s.size() > 0:

            #POP MOST RECENT VERTEX
            v = s.pop()

            ##IF IT'S NOT VISITED
            if v not in visited:
                print(v)

            ##MARK AS VISITED
            visited.add(v)

            ##PUSH ITS NEIGHBORS
            for next_vert in self.get_neighbors(v):
                ##Don't get stuck in the 3 & 5 weird loop in this tree
                if next_vert not in visited:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        if visited == None:
            visited = set()


        if s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
            visited.add(v)
            if len(self.vertices) == len(visited):
                return
            else:
                for next_vert in self.get_neighbors(v):
                    if next_vert not in visited:
                ##Don't get stuck in the 3 & 5 weird loop in this tree
                        s.push(next_vert)
                return self.dft_recursive(next_vert, visited)

    """BEGINNING OF SEARCHES"""

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print('BFT:')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT:')
    graph.dft(1)
    print('DFT Recursive:')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
