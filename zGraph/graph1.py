graph = [
    [1,1,1,1,0,0],
    [1,1,0,0,0,0],
    [1,0,1,0,0,1],
    [1,0,0,1,1,0],
    [0,0,0,1,1,0],
    [0,0,1,0,0,1]
    ]
start = 0
qqq=0

def recurse(graph,start,visited,answer):
    global qqq
    visited[start] = 1
    answer.append(start)
    for i in range(len(graph[start])):
        
        if graph[start][i] ==1 and visited[i]==0 and start != i:
            qqq= qqq +1
            visited[i] = 1
            answer.append(i)
    
    if qqq ==0:
        qqq=qqq+1
        
    recurse(graph,answer[len(answer)-qqq],visited,answer)

    
               
def recurse_dfs(graph,input_start):
    visited = [0] * len(graph)
    answer=[]
    recurse(graph,input_start,visited, answer)
    return answer


print( recurse_dfs(graph,start))

# graph = {
#     'A':["B","C"],
#     'B':["A","D","E"],
#     'C':["A","F"],
#     'D':["B"],
#     'E':["B","F"],
#     'F':["C","E"]
#     }

# start = 'A'

# def adlist(graph,now_value,answer):
#     answer.append(now_value)
#     for i in range(len(graph[now_value])):
#         if graph[now_value][i] not in answer:
#             adlist(graph,graph[now_value][i],answer)
            

# def dfs_adlisr(graph,start):
#     answer=[]
#     adlist(graph,start, answer)
#     return answer

# print(dfs_adlisr(graph,start))