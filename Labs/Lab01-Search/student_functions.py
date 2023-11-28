import numpy as np


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

    node = start
    visited.update({node: None})

    if node == end:
        path.append(node)
        return visited, path
    
    frontier = []
    frontier.append(node)
    while frontier:
        if not frontier:
            path.append(end) #?
            return visited, path
        
        node = frontier.pop(0)

        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 \
            and i not in visited \
            and i not in frontier:
                
                if i == end:
                    path.append(node)
                    break

                frontier.append(i)
                visited.update({i: node})
                path.append(frontier[0])
        

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

    node = start
    visited.update({node: None})

    if node == end:
        path.append(node)
        return visited, path
    
    frontier = []
    frontier.append(node)
    while frontier:
        if not frontier:
            path.append(end) #?
            return visited, path
        
        node = frontier.pop()

        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 \
            and i not in visited \
            and i not in frontier:
                
                if i == end:
                    path.append(node)
                    break

                frontier.append(i)
                visited.update({i: node})
                path.append(frontier[0])
        
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
    # TODO:  
    path=[]
    visited={}
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
    # TODO:  
    path=[]
    visited={}
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

