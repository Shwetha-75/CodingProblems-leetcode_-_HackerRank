class Solution: 
          def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
              hash_map={}
              for index in range(len(connections)):
                  if connections[index][0] not in hash_map:
                      hash_map[connections[index][0]]=[[index],[connections[index][1]]]
                  else:
                      hash_map[connections[index][0]][0].append(index)
                      hash_map[connections[index][0]][1].append(connections[index][1])
                  if connections[index][1] not in hash_map:
                      hash_map[connections[index][1]]=[[index],[connections[index][0]]]
                  else:
                      hash_map[connections[index][1]][0].append(index)
                      hash_map[connections[index][1]][1].append(connections[index][0])
              for key,value in hash_map.items():
                  if len(value[1])==1:
                      return connections[value[0]]