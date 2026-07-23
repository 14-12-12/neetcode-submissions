class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adjList = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[pre].append(course)
            in_degree[course] += 1
        
        def bfs(adjList, numCourses, in_degree) -> bool:
            queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
            count = 0
            while queue:
                curr = queue.popleft()
                count += 1
                for neighbor in adjList[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return count == numCourses

        return bfs(adjList, numCourses, in_degree)