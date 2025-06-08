'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

 

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n

'''

class Solution:
        def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
            hash_map_node1={node1:0}
            hash_map_node2={node2:0}
            count=0 
            index=node1 
            while index!=-1:
                  index=edges[index]
                  count+=1
                  if index==-1 or index in hash_map_node1:
                      break
                  hash_map_node1[index]=count 
            index=node2 
            count=0
            while index!=-1:
                  index=edges[index]
                  count+=1
                  if index==-1 or index in hash_map_node2:
                      break
                  hash_map_node2[index]=count 
            common_node={}
            for key,value in hash_map_node1.items():
                if key in hash_map_node2:
                    common_node[key]=max(value,hash_map_node2[key])
            min_distance=float('inf')
            node=-1
            for key,value in common_node.items():
                if value<min_distance:
                    min_distance=value
                    node=key 
                elif value==min_distance:
                     node=min(node,key)
            return node
class TestApp:
      def testing_case_one(self):
          assert Solution().closestMeetingNode([2,2,3,-1],0,1)==2
      def testing_case_two(self):
          assert Solution().closestMeetingNode([1,2,-1],0,2)==2
      def testing_case_three(self):
          assert Solution().closestMeetingNode([2,0,0],2,0)==0         

              