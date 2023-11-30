import numpy as np
from collections import deque
from queue import PriorityQueue

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
    visited[start] = None

    while queue:
        current_node = queue.popleft()

        if current_node == end:
            while current_node is not None:
                path.insert(0, current_node)
                current_node = visited[current_node]
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited:
                visited[neighbor] = current_node
                queue.append(neighbor)
        
    print("Visited: ", visited)
    print("Path: ", path)

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
    stack = deque([start])
    visited[start] = None

    while stack:
        current_node = stack.pop()

        if current_node == end:
            while current_node is not None:
                path.insert(0, current_node)
                current_node = visited[current_node]
            break

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited:
                visited[neighbor] = current_node
                stack.append(neighbor)
        
    print("Visited: ", visited)
    print("Path: ", path)
    
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
            if isConnected and neighbor not in visited:
                visited[neighbor] = current_node
                neighbor_priority = current_priority + matrix[current_node][neighbor]
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
    path = []
    visited = {}
    stack = deque([(start, 0)])
    visited[start] = None

    while stack:
        current_node, current_depth = stack.pop()

        if current_depth > depth_limit:
            continue

        if current_node == end:
            while current_node is not None:
                path.insert(0, current_node)
                current_node = visited[current_node]
            return visited, path

        for neighbor, isConnected in enumerate(matrix[current_node]):
            if isConnected and neighbor not in visited:
                visited[neighbor] = current_node
                stack.append((neighbor, current_depth + 1))

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
    # TODO: 
    path=[]
    visited={}
    return visited, path

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
    # TODO: 

    path=[]
    visited={}
    return visited, path

