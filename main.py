import os

from util import *


def main():
    print("1. graphin-c1")
    print("2. graphin-c2")
    print("3. graphin-DAG")
    print("4. Custom File (Must be in Input folder!)")
    while True:
        try:
            execType = int(input("Which graph to use? (1-3)"))
            if 4 >= execType > 0:
                break
        except:
            print("Please type an integer (1-3)")

    if execType == 1:
        file = "input/graphin-c1.txt"
    elif execType == 2:
        file = "input/graphin-c2.txt"
    elif execType == 3:
        file = "input/graphin-DAG.txt"
    elif execType == 4:
        file = str(input("Type custom filename:"))
        file = "input/" + file

    if os.path.isfile(file):
        graph = Util.read_in_graph(file)
        back_edges = is_acyclic(graph)
        if len(back_edges) > 0:
            print("NOT ACYCLIC!")
            print("Back Edges: ")
            print(back_edges)
        else:
            print("DIRECT ACYCLIC GRAPH!")
            sort = topological_sort(graph)
            print("Topological Sort: ")
            print(sort)
    else:
        print("Path is not a file!")


def is_acyclic(graph):
    # creating an array to return back edges
    back_edges = []
    # creating a list of bools for visited, index 0 is null because we're starting at 1
    visited = [False] * (graph.vertices + 1)
    visited[0] = None
    # creating a recursion stack to detect for cycle 0 is null because we're starting at 1
    recursion_stack = [False] * (graph.vertices + 1)
    recursion_stack[0] = None

    # looping through the graph data object
    for vert in range(1, graph.vertices + 1):
        # check if it's been visited
        if not visited[vert]:
            # if not, check for cycle, if cycle return true
            is_acyclic_recursion(graph, vert, visited, recursion_stack, back_edges)
    # else return false, no cycle, only DAG should return a cycle
    # return back-edges if empty, no cycles, if not empty, cycles.
    return back_edges


def is_acyclic_recursion(graph, vert, visited, recursion_stack, back_edges):
    # marking vertex as being visited.
    visited[int(vert)] = True
    # marking the recursion stack as true, will change if false.
    recursion_stack[int(vert)] = True

    # checking all other vertex neighbors, if a node gets checked twice, then there's
    # a cycle
    for x in graph.graph[str(vert)]:
        if not visited[int(x)]:
            if is_acyclic_recursion(graph, x, visited, recursion_stack, back_edges):
                return True
        elif recursion_stack[int(x)]:
            back_edges.append([vert, x])
            return True

    # No cycle detected, return false
    recursion_stack[int(vert)] = False
    return False


def topological_sort(graph):
    # creating a list of bools for visited, index 0 is null because we're starting at 1
    visited = [False] * (graph.vertices + 1)
    visited[0] = None
    # creating a recursion stack to detect for cycle 0 is null because we're starting at 1
    top_list = []

    # go through the graph and run topological sort
    for x in range(1, graph.vertices + 1):
        if not visited[x]:
            topological_sort_recursion(graph, x, visited, top_list)

    return top_list


def topological_sort_recursion(graph, vert, visited, top_list):
    # marking vertex as being visited.
    visited[int(vert)] = True

    # checking all other vertex neighbors
    for x in graph.graph[str(vert)]:
        # if the vertex hasn't been visited add search it
        if not visited[int(x)]:
            topological_sort_recursion(graph, x, visited, top_list)

    # add it to the list
    top_list.insert(0, vert)


if __name__ == '__main__':
    main()
