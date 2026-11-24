class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for source, dest in prerequisites:
            indegree[dest] +=1
            adj[source].append(dest)

        q = deque()
        for num in range(numCourses):
            if indegree[num] == 0:
                q.append(num)
        
        finished = 0

        while q:
            curr = q.popleft()
            finished+=1

            for course in adj[curr]:
                indegree[course] -=1
                if indegree[course] ==0:
                    q.append(course)

        return finished == numCourses