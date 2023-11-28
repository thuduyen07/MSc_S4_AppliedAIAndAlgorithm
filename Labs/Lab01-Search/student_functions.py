import numpy as np

from collections import defaultdict, deque


def BFS(matrix, start, end):
    # Khởi tạo hàng đợi và từ điển để theo dõi các đỉnh đã thăm
    queue = deque([start])
    visited = {start: None}

    while queue:
        current_node = queue.popleft()

        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for neighbor, has_edge in enumerate(matrix[current_node]):
            if has_edge and neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = current_node
    print(visited)
    # Xây dựng đường đi từ điểm đích đến điểm bắt đầu
    path = build_path(start, end, visited)
    
    print(path)
    return visited, path

def build_path(start, end, visited):
    # Xây dựng đường đi từ điểm đích đến điểm bắt đầu sử dụng thông tin đã thăm
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = visited[current_node]

    # Đảo ngược đường đi để có thứ tự đúng
    path.reverse()

    return path

def DFS(matrix, start, end):
    # TODO:  
    path=[]
    visited={}
    
    stack = deque([(start, 0)])  # Stack chứa cặp (đỉnh, chi phí)

    while stack:
        current, cost = stack.pop()

        if current not in visited:
            visited[current] = cost
            path.append(current)

            if current == end:
                break  # Đã đến đích, kết thúc thuật toán

            neighbors = np.nonzero(matrix[current])[0]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, cost + matrix[current, neighbor]))

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
    
    node = start
    visited.update({node: None})

    if node == end:
        path.append(node)
        return visited, path
    
    frontier = []
    frontier.append(node)
    frontier.sort()

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
                frontier.sort()
                visited.update({i: node})
                path.append(frontier[0])
        
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

