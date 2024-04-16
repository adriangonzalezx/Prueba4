import heapq

def dijkstra(graph, start, end):
    # Inicializar el diccionario de distancias
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Inicializar el conjunto de nodos no visitados
    unvisited_nodes = [(0, start)]
    
    while unvisited_nodes:
        # Obtener el nodo con la distancia mínima
        current_distance, current_node = heapq.heappop(unvisited_nodes)
        
        # Si hemos alcanzado el nodo de destino, terminar
        if current_node == end:
            break
        
        # Si la distancia actual es mayor que la distancia almacenada, continuar
        if current_distance > distances[current_node]:
            continue
        
        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Actualizar la distancia si encontramos un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited_nodes, (distance, neighbor))
    
    # Reconstruir el camino más corto desde la ciudad de inicio a la ciudad de destino
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = min((neighbor for neighbor in graph[current_node] if distances[neighbor] == distances[current_node] - graph[current_node][neighbor]), key=lambda x: x)
    path.append(start)
    path.reverse()
    
    return path, distances[end]

# Ejemplo de uso
graph = {
    'Rivendell': {'Bree': 5, 'Lothlórien': 3},
    'Bree': {'Rivendell': 5, 'Minas Tirith': 8},
    'Lothlórien': {'Rivendell': 3, 'Minas Tirith': 7},
    'Minas Tirith': {'Bree': 8, 'Lothlórien': 7}
}
start_city = 'Rivendell'
end_city = 'Minas Tirith'
shortest_path, shortest_distance = dijkstra(graph, start_city, end_city)
print(f"La ruta más corta desde {start_city} a {end_city} es: {shortest_path}")
print(f"La distancia total es: {shortest_distance}")
