# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {}

        stack = [node]

        clones[node] = Node(node.val)

        while stack:
            curr_node = stack.pop()

            for neighbour in curr_node.neighbors:
                if neighbour not in clones:
                    clones[neighbour] = Node(neighbour.val)
                    stack.append(neighbour)

                clones[curr_node].neighbors.append(clones[neighbour])

        return clones[node]
    
    # def print_graph(self, node, visited=None):
    #     if visited is None:
    #         visited = set()
    #     if node in visited:
    #         return
    #     visited.add(node)
    #     print(f"Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
    #     for neighbor in node.neighbors:
    #         self.print_graph(neighbor, visited)
        

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)

nodeA.neighbors = [nodeB, nodeD]
nodeB.neighbors = [nodeA, nodeC]
nodeC.neighbors = [nodeB]
nodeD.neighbors = [nodeA]

sol = Solution()
cloned_graph = sol.cloneGraph(nodeA)
# sol.print_graph(cloned_graph)

