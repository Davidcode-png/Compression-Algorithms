class Node:
    def __init__(self,symbol,prob) -> None:
        self.symbol = symbol
        self.prob = prob


node1 = Node('A', 0.22)
node2 = Node('B', 0.28)
node3 = Node('C', 0.15)
node4 = Node('D', 0.30)
node5 = Node('E', 0.05)

nodes = [node1, node2, node3, node4, node5]
def shannon(nodes):
    sort_nodes = sorted(nodes, key=lambda x: x.prob, reverse=True)
    nodes = [i.symbol for i in sort_nodes]
    print(nodes)
    result = get_partition(sort_nodes)
    print("The final result is", result)
    return result

def get_partition(nodes):
    if len(nodes) == 1:
        x = [[nodes[0].symbol]]
        print("What you get is", x)
        return x
    sum_of_nodes = sum([i.prob for i in nodes])
    new_partition = []
    count = 0
    for i in nodes:
        count += 1
        new_partition.append(i)
        if sum([i.prob for i in new_partition]) > (sum_of_nodes/2):
            data = [i.symbol for i in new_partition], [j.symbol for j in sorted(list(set(nodes) -  set(new_partition)), key=lambda x:x.prob, reverse=True)]
            print("Data is: ",data)
            nodes = nodes[len(new_partition):]
            break
    
    result = get_partition(new_partition)
    result.extend(get_partition(nodes))
    return result

shannon(nodes)
