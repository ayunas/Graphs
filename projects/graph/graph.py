"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from random import randint

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
        if v1 not in self.vertices or v2 not in self.vertices:
            # print('specified vertex does not exist in the graph')
            raise Exception('specified vertex does not exist in the graph')
            return (v1,v2)
        
        self.vertices[v1].add(v2)
        # self.vertices[v2].add(v1)
        # self.vertices[v1].add(v2) = v2
        # self.vertices[v2] = v1

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []

        for neighbor in self.vertices[vertex_id]:
           neighbors.append(neighbor)

        return neighbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        #1. add neighbors of starting_vertex to queue
        #2. mark starting node as explored:
        # visited = [False]*len(self.vertices)
        #3. While the queue has vertices
        #4. pop off (dequeue) oldest node from queue. which is the neighbor of starting_vertex.
        #5. check if vertex is visited. 
        #6. add vertex to visited array
        #7. get the neighbors of the current vertex and add them to the queue
        """
        q = Queue()
        neighbors = self.get_neighbors(starting_vertex)
        for n in neighbors:
            q.enqueue(n)

        visited = [starting_vertex]
       
        while q.size():
            vertex = q.dequeue()
            if vertex not in visited:
                visited.append(vertex)
                neighbors = self.get_neighbors(vertex)
                for n in neighbors:
                    q.enqueue(n)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        neighbors = self.get_neighbors(starting_vertex)
        
        for n in neighbors:
            s.push(n)
        
        visited = [starting_vertex]
        
        while s.size():
            v = s.pop()
            if v not in visited:
                visited.append(v)
                neighbors = self.get_neighbors(v)
                for n in neighbors:
                    s.push(n)
        return visited

    def dft_helper(self,v,visited):
        visited.append(v)

        for neighbor in self.vertices[v]:
            if neighbor not in visited:
                visited = self.dft_helper(neighbor,visited)

        return visited


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = []
        vis = self.dft_helper(starting_vertex,visited)

        return vis

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

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

    def __repr__(self):
        return str(self.vertices)


g = Graph()

# for i in range(50):
#     # vertex = str(randint(1,50))
#     g.add_vertex(i+1)

# for i in range(100):
#     v1 = randint(1,50)
#     v2 = randint(1,50)
#     g.add_edge(v1,v2)

# # print(g)
# breadth_first_traversal = g.bft(2)
# print('breadth first traversal', breadth_first_traversal)



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

    print(graph)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
    breadth = graph.bft(1)
    print('breadth: ', breadth)
#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
    depth = graph.dft(1)
    print('depth', depth)
    v = graph.dft_recursive(1)
    print('dft_recursive', v)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))
