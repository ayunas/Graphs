# The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
# Example input
'''
  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1

  6
Example output
  10
'''
#ancestors = [(parent,child),(,),(,),...]

from utils import Graph


def earliest_ancestor(parents_children, start_vert):

    graph = Graph()

    for pair in parents_children:
        graph.add_vert(pair)
    
    parents = {p for p,c in parents_children}
    children = {c for p,c in parents_children}
    
    paths = []
    for p in parents:
        route = graph.dfs(start_vert, p)
        paths.append(route)

    valid_paths = [p for p in paths if p != None and len(p) > 1]
    # valid_paths = list(filter(lambda p: p != None, paths))
    
    if len(valid_paths) == 0:
        return -1

    longest_path = max(valid_paths, key=len)
    
    return longest_path[-1]

    # bft = graph.bft(6)
    # dft = graph.dft(6)
    # dfs = graph.dfs()
    # bfs = graph.bfs(6,2)
    # print(dfs)
    # return ['bft', bft, 'dft',dft, 'dfs',dfs, 'bfs',bfs]

parents_children = [(1,3),(2,3),(3,6),(5, 6),(5 ,7),(4, 5),(4 ,8),(8 ,9),(11 ,8),(10, 1)]
l = earliest_ancestor(parents_children,2)

print(l)
