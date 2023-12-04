import math
import numpy as np
from collections import deque
from queue import LifoQueue, PriorityQueue

def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """

    path=[]
    visited={}
    queue = deque([start])
    visited.update({start: None})
    explored = []
    
    while queue:

        current_node = queue.popleft()
        explored.append(current_node)

        if current_node == end:
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            path.reverse()
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited and neighbor not in explored:

                visited.update({neighbor: current_node})

                if neighbor == end:
                    path.append(neighbor)
                    while current_node is not None:
                        path.append(current_node)
                        current_node = visited[current_node]
                    path.reverse()

                    print("Final Visited: ", visited)
                    print("Final Path: ", path)
                    return visited, path
                
                queue.append(neighbor)

    print("Final Visited: ", visited)
    print("Final Path: ", path)
    return visited, path

def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    path=[]
    visited={}
    stack = LifoQueue(maxsize=max(matrix.shape))
    stack.put(start)
    visited.update({start: None})
    explored = []

    while stack:

        current_node = stack.get()
        explored.append(current_node)

        if current_node == end:
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            path.reverse()
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited and neighbor not in explored:

                visited.update({neighbor: current_node})

                if neighbor == end:
                    path.append(neighbor)
                    while current_node is not None:
                        path.append(current_node)
                        current_node = visited[current_node]
                    path.reverse()

                    print("Final Visited: ", visited)
                    print("Final Path: ", path)
                    return visited, path
                
                stack.put(neighbor)
                print("stack: ", stack.queue)
            
    print("Final Visited: ", visited)
    print("Final Path: ", path)
    return visited, path

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    path=[]
    visited={}

    priorityQueue = PriorityQueue()
    priorityQueue.put((0, start))

    visited[start] = None

    while priorityQueue.qsize() > 0:
        print(priorityQueue.queue)
        current_priority, current_node = priorityQueue.get()

        if current_node == end:
            while current_node is not None:
                path.insert(0, current_node)
                current_node = visited[current_node]
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected: 

                if neighbor not in visited:
                    visited[neighbor] = current_node

                neighbor_priority = current_priority + matrix[current_node][neighbor]

                # check if neighbor is in queue and has smaller priority then delete it before update
                if neighbor in [node for (_, node) in priorityQueue.queue]:
                    for i, (priority, node) in enumerate(priorityQueue.queue):
                        if node == neighbor:
                            if priority > neighbor_priority:
                                del priorityQueue.queue[i]
                                priorityQueue.put((neighbor_priority, neighbor))
                            break
                else:
                    priorityQueue.put((neighbor_priority, neighbor))

    print("Visited: ", visited)
    print("Path: ", path)
    return visited, path

def IDS(matrix, start, end):
    """
    Iterative deepening search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    path=[]
    visited={}

    depth_limit = 0
    max_depth = len(matrix)  

    while depth_limit <= max_depth:
        visited, path = DFS_limit(matrix, start, end, depth_limit)
        if end in visited:
            break
        depth_limit += 1

    print("Visited: ", visited)
    print("Path: ", path)
    return visited, path

def DFS_limit(matrix, start, end, depth_limit):
    """
    Depth-limited depth-first search algorithm
    """
    path=[]
    visited={}
    stack = LifoQueue(maxsize=max(matrix.shape))
    stack.put(start)
    visited.update({start: None})
    explored = []

    current_depth = 0
    while stack and current_depth <= depth_limit:

        current_node = stack.get()
        explored.append(current_node)

        if current_node == end:
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            path.reverse()
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited and neighbor not in explored:

                visited.update({neighbor: current_node})

                if neighbor == end:
                    path.append(neighbor)
                    while current_node is not None:
                        path.append(current_node)
                        current_node = visited[current_node]
                    path.reverse()

                    print("Final Visited: ", visited)
                    print("Final Path: ", path)
                    return visited, path
                
                stack.put(neighbor)
                print("stack: ", stack.queue)
        current_depth += 1
            
    print("Final Visited: ", visited)
    print("Final Path: ", path)
    return visited, path

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm 
    heuristic : edge weights
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    path=[]
    visited={}

    # assume: heuristic = current_priority

    heuristic = 10
    priorityQueue = PriorityQueue()
    priorityQueue.put((heuristic, start))

    visited[start] = None

    while priorityQueue.qsize() > 0:
        print(priorityQueue.queue)
        heuristic, current_node = priorityQueue.get()
        if current_node == end:
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected: 
                if neighbor not in visited:
                    visited[neighbor] = current_node

                neighbor_heuristic = matrix[current_node][neighbor]

                # check if neighbor is in queue and has smaller heuristic then delete it before update
                if neighbor in [node for (_, node) in priorityQueue.queue]:
                    for i, (heuristic, node) in enumerate(priorityQueue.queue):
                        if node == neighbor:
                            if heuristic > neighbor_heuristic:
                                del priorityQueue.queue[i]
                                priorityQueue.put((neighbor_heuristic, neighbor))
                            break
                else:
                    priorityQueue.put((neighbor_heuristic, neighbor))

    path.reverse()
    print("Visited: ", visited)
    print("Path: ", path)
    return visited, path

"""
References:
- https://www.redblobgames.com/pathfinding/a-star/implementation.html
- https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
"""

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
    heuristic: eclid distance based positions parameter
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    path=[]
    visited={}

    # assume: heuristic = current_priority + math.dist(pos[current_node]), pos[end])

    explored = []
    priority_queue = PriorityQueue()
    current_h = math.dist(pos[start], pos[end])
    visited[start] = None
    current_f = current_h
    current_g = 0
    priority_queue.put((current_f, start))

    while priority_queue.qsize() > 0:
        print("priorityQueue: ", priority_queue.queue)
        print("visited: ", visited)
        current_cost, current_node = priority_queue.get()
        current_g += current_cost

        if current_node == end:
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            break

        for neighbor, is_connected in enumerate(matrix[current_node]):
            if is_connected: 
                current_neighbor_w = math.dist(pos[current_node], pos[neighbor])
                neighbor_current_cost = current_g + current_neighbor_w
                neighbor_g = current_g + matrix[current_node][neighbor]
                if neighbor in visited:
                    if neighbor_g <= neighbor_current_cost:
                        continue
                elif neighbor in explored:
                    if neighbor_g < neighbor_current_cost:
                        continue
                    explored.remove(neighbor)
                    visited[neighbor] = current_node
                    neighbor_h = math.dist(pos[neighbor], pos[end])
                    neighbor_f = neighbor_g + neighbor_h
                    priority_queue.put((neighbor_f, neighbor))
                else:
                    visited[neighbor] = current_node
                    neighbor_h = math.dist(pos[neighbor], pos[end])
                    neighbor_f = neighbor_g + neighbor_h
                    priority_queue.put((neighbor_f, neighbor))

        explored.append(current_node)
    
    path.reverse()
    print("Visited: ", visited)
    print("Path: ", path)
    return visited, path

