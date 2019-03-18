import itertools
import sys
import time

from graph import *


# Using Spinner written for Project 1 (cs340).
class Util:
    go = True

    def __init__(self):
        pass

    @classmethod
    def spinning_cursor(cls):
        spinner = itertools.cycle(['-Doing Algo Stuff. ', '/Doing Algo Stuff.. ',
                                   '|Doing Algo Stuff... ', '\\Doing Algo Stuff.... '])
        while Util.go:
            sys.stdout.write(next(spinner))  # write the next character
            sys.stdout.flush()  # flush stdout buffer (actual character display)
            time.sleep(.25)
            sys.stdout.write('\r')  # erase the last written char

    @classmethod
    def read_in_graph(cls, file):
        file = open(file).readlines()
        vert_count = len(file)
        graph = Graph(vert_count)

        for x in range(0, len(file)):
            file[x] = file[x].strip('\n')
        for i in range(0, len(file)):
            split = file[i].split(':')
            vert = split[0]
            edges = split[1]
            edges = edges.split(' ')
            for k in range(0, len(edges)):
                graph.graph[vert].append(edges[k])

        for x in range(1, vert_count + 1):
            graph.graph[str(x)] = list(filter(None, graph.graph[str(x)]))

        return graph
