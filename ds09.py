from collections import deque

def BFS(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        vertex = queue.popleft()
        for ne in graph[vertex]:
            if ne not in visited:
                visited.add(ne)
                queue.append(ne)
    return visited

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for ne in graph[start]:
        if ne not in visited:
            DFS(graph, ne, visited)
    return visited

def selection_sort(A):
    B = []
    A_copy = A[:]
    while A_copy:
        minimum = min(A_copy)
        B.append(minimum)
        A_copy.remove(minimum)
    return B

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):  # optimization: last i elements are already sorted
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
