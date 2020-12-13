graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [8], 7: [3], 8: []}


def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            dfs(w, discovered)
    return discovered


print(dfs(1))