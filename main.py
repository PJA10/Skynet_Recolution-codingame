import sys
import math
low_bar = float("inf")
def path_finding(i, nodes_connection_list, exit_nodes_list, si, num_of_steps, connection_to_choose):
    global low_bar
    if connection_to_choose == -1 and i != si:
        connection_to_choose = i
    print("i {}, si {}, num_of_steps {}, connection_to_choose {}, low_bar {}".format(i, si, num_of_steps, connection_to_choose, low_bar), file=sys.stderr)
    if num_of_steps > low_bar:
        return connection_to_choose, 10000
    options = []
    for connection in nodes_connection_list:
        if connection[0] == i:
            options.append(connection[1])
        elif connection[1] == i:
            options.append(connection[0])
    if i in exit_nodes_list:

        return connection_to_choose, num_of_steps
    if len(options) == 0:
        return connection_to_choose, 10000
    min_connection_to_choose = -1
    min_steps = float("Inf")
    for node in options:
        for connection in nodes_connection_list:
            if connection[0] == i:
                if connection[1] == node:
                    node_connection = connection
                    break
            elif connection[1] == i:
                if connection[0] == node:
                    node_connection = connection
                    break
        nodes_connection_list.remove(node_connection)
        next = path_finding(node, nodes_connection_list, exit_nodes_list, si, num_of_steps+1, connection_to_choose)
        if next[1] < min_steps:
            min_steps = next[1]
            min_connection_to_choose = next[0]
            low_bar = min(low_bar, min_steps)
        nodes_connection_list.append(node_connection)
    return  min_connection_to_choose, min_steps

exit_nodes_list = []
nodes_connection_list = []
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    nodes_connection_list.append((n1,n2))
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exit_nodes_list.append(ei)
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("n1: {}, n2: {}, n: {}, l: {}, e: {}, ei: {}".format(n1,n2,n,l,e,ei), file=sys.stderr)
    print("exit_nodes_list: {}, nodes_connection_list: {}".format(exit_nodes_list, nodes_connection_list), file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    node_to_choose = path_finding(si, nodes_connection_list, exit_nodes_list, si, 0, -1)
    print("node_to_choose: {}".format(node_to_choose), file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    ni = []
    choosen = -1
    for connaction in nodes_connection_list:
        if connaction[0] == si or connaction[1] == si:
           ni.append(connaction)
    for connaction in ni:
        if connaction[0] in exit_nodes_list or connaction[1] in exit_nodes_list:
            choosen = connaction
    if choosen == -1:
        choosen = ni[0]
    print("choosen: {}".format(choosen), file=sys.stderr)

    print("{} {}".format(choosen[0], choosen[1]))



