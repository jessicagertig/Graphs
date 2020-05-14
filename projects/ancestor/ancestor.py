from graph import Graph
from util import Stack, Queue 

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    
    ##begin a graph
    family = Graph()
    ##add the nodes
    for each in ancestors:
        family.add_vertex(each[0])
        family.add_vertex(each[1])
        ##define the edges which will go up only from child up to parent
        family.add_edge(each[1], each[0])

    ##use the graph to search for oldest ancestor (furthest away)
    ##if there are 2 eldest ancestors choose the one with the lower numeric value
    ##if there are no ancestors return -1
    
    ##use a queue to keep track of paths
    q = Queue()
    ##intiate a path with beginning node
    q.enqueue([starting_node])
    ##we will need to find all possible paths
    ## create an array to store paths
    paths = []
    while q.size() > 0:
        ##deqeue first path and store as variable
        p = q.dequeue()
        parents = family.get_neighbors(p[-1])
        if len(parents) == 0:
            ##account for case with no parents
            if len(p) == 1 and p[0] == starting_node:
                return -1
            ##append completed path to array paths
            else:
                paths.append(p)
        elif len(parents) == 2:
            ##if 2 parents neither parent has parents check for smaller parent value to append
            list_parents = list(parents)
            parent1_parents = family.get_neighbors(list_parents[0])
            parent2_parents = family.get_neighbors(list_parents[1])
            if len(parent1_parents) == 0 and len(parent2_parents) == 0:
                ##make one copy of current path
                copy = p.copy()
                ##find smaller numeric value of two parents and append the smaller
                if list_parents[0] < list_parents[1]:
                    copy.append(list_parents[0])
                    q.enqueue(copy)
                else:
                    copy.append(list_parents[1])
                    q.enqueue(copy)
            else:##business as usual
                for parent in parents:
                    copy = p.copy()
                    copy.append(parent)
                    q.enqueue(copy)
        ###is there a way to consolidate repeated code?
        else:##appending new parents to list
            for parent in parents:
                copy = p.copy()
                copy.append(parent)
                q.enqueue(copy)
    ##find the longest path = contains eldest ancestor
    longest = paths[0]
    for path in paths:
        if len(path) > len(longest):
            longest = path
    ##return last element in path, which will be the eldest ancestor
    return longest[-1]    

    





    


print(earliest_ancestor(test_ancestors, 2))