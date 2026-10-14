"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):t
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones={}
        def flow(cur):
            if cur in clones:
                return clones[cur]
            clone=Node(cur.val)
            clones[cur]=clone
            for nei in cur.neighbors:
                clone.neighbors.append(flow(nei))
            return clone
        return flow(node)
        