class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {c: 0 for c in range(numCourses)} # how many courses does it depend on
        adj = {c:[] for c in range(numCourses)} # how many courses depend on it

        finished = 0
        completed = deque()

        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)
        
        for course, count in indegree.items():
            if count == 0:
                completed.append(course)

        while completed:
            curr = completed.popleft()
            finished += 1

            for course in adj[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    completed.append(course)

        return finished == numCourses