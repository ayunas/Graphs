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


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    for pair in ancestors:
        graph.add_vert(pair)
    print(graph)

ancestors = [(1,3),(2,3),(3,6),(5, 6),(5 ,7),(4, 5),(4 ,8),(8 ,9),(11 ,8),(10, 1)]
  
earliest_ancestor(ancestors,6)
