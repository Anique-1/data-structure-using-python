#create dict
# graph={
#     "A":["B","C"],
#     "B":["D","E"],
#     "C":["F","G"],
#     "D":[],
#     "E":[],
#     "G":[],
#     "F":[],
# }
graph={
    "5":["3","7"],
    "3":["2","4"],
    "7":["8"],
    "2":[],
    "4":["8"],
    "8":[]
}

visited=[]  #list of visited nodes
stack=[] #initial queue

def dfs (visited, graph,node):
    visited.append(node)
    stack.append(node)
    
    while stack:
        m=stack.pop(-1)
        print(m, end=' ')
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
                
print("following is the breadth first search")
print(f'stack is empty {stack}')
dfs(visited,graph,"5")