class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {c : 0 for c in range(numCourses) }
        adj = {c : [] for c in range(numCourses)}

        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)

        ready = deque()

        for course, count in indegree.items():
            if count == 0:
                ready.append(course)

        finished = 0

        while ready:
            course = ready.popleft()
            finished +=1

            for c in adj[course]:
                indegree[c]-=1
                if indegree[c] == 0:
                    ready.append(c)

        return finished == numCourses