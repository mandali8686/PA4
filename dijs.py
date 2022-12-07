import heapq
import configparser

config = configparser.ConfigParser()
config.read('ip.ini')

def dijkstra(graph, start, end):
  distances = {vertex: float('inf') for vertex in graph}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_distance, current_vertex = heapq.heappop(queue)

    if current_vertex == end:
      break

    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(queue, [distance, neighbor])

  path = [end]
  while end != start:
    for neighbor, weight in graph[end].items():
      if distances[neighbor] == distances[end] - weight:
        path.append(neighbor)
        end = neighbor
        break

  return path[::-1]
  
graph = {
  'Client': {'Router1': 1, 'Router2': 1, 'Router3': 1},
  'Router1': {'Router2': 1, 'Router4': 1, 'Client': 1},
  'Router2': {'Client': 1, 'Server': 1,'Router1': 1, 'Router3': 1},
  'Router3': {'Client': 1, 'Router2': 1, 'Router5': 1},
  'Router4': {'Router1': 1, 'Server': 1},
  'Router5': {'Router3': 1, 'Server': 1},
  'Server':{'Router2': 1, 'Router4': 1, 'Router5': 1},
}

path1=dijkstra(graph,'Client','Server')
print("Routing shortest path without delay:",path1)

delay_graph = {
  'Client': {'Router1': 10, 'Router2': 100, 'Router3': 20},
  'Router1': {'Router2': 10, 'Router4': 10, 'Client': 10},
  'Router2': {'Client': 100, 'Server': 100,'Router1': 10, 'Router3': 10},
  'Router3': {'Client': 20, 'Router2': 10, 'Router5': 10},
  'Router4': {'Router1': 10, 'Server': 10},
  'Router5': {'Router3': 10, 'Server': 10},
  'Server':{'Router2': 100, 'Router4': 10, 'Router5': 10},
}
path2=dijkstra(delay_graph,'Client','Server')
print('Routing shortest path with delay',path2)

        
