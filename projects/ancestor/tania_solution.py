ancestors_data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    ancestor_tree = Graph()
    # Iterate through ancestors
    for (parent, child) in ancestors:  
        # Add vertices to ancestor_tree
        ancestor_tree.add_vertex(parent)
        ancestor_tree.add_vertex(child)
    # print("ancestor tree", ancestor_tree.vertices)
    for (parent, child) in ancestors:
        # Add edges
        ancestor_tree.add_edge(parent, child)
    # print("neighbors", ancestor_tree.get_neighbors(5))
    # print("ancestor tree", ancestor_tree.vertices)

    longest_path = 1  # Keep track of # ancestors; highest means most ancestors
    earliest_ancestor = 0 # Store last node (as an integer)

    for i in ancestor_tree.vertices:
        # print("i", i)  # Print vertices
        # Call dfs function from Graph class
        path = ancestor_tree.dfs(i, starting_node)  # i is each vertex/node in graph
        # print("ancestor dfs", ancestor_tree.dfs(starting_node, i))
        print('path', path)
        if path:  # If there are items in list
            if len(path) > longest_path:  # If list length is greater than longest path
                longest_path = len(path)  # Set longest path equal to list length
                earliest_ancestor = i  # Set earliest_ancestor equal to current node/vertex
        elif not path and longest_path == 1:  # If path is 'None' and 'longest_path' is our default of 1   
            earliest_ancestor = -1
    print("earliest ancestor", earliest_ancestor)
    return earliest_ancestor
print('earliest ancestor', earliest_ancestor(ancestors_data, 8))



def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create stack 
        stack = Stack()  # Stack imported above
        # Put the starting point in it
        # 'enstack' a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in stack
        while stack.size() > 0:
            # Pop first item
            path = stack.pop()  # Path is first item in stack
            vertex = path[-1]  # Vertex is last item in path
            # If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # DO THE THING! 
                    return path  # Return path we've built so far
                # Add to visited
                visited.add(vertex)
                # Get neighbors for each edge in item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid 'pass by reference' bug
                    new_path = list(path)  # Makes copy rather than reference
                    new_path.append(next_vert)  # Add new vertex to copy
                    stack.push(new_path) 