class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {c:0 for c in range(numCourses)}
        adj = {c:[] for c in range(numCourses)}

        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)
        
        # populate ready courses that do not have sources
        finished = 0
        ready = deque()

        for course, count in indegree.items():
            if count == 0:
                ready.append(course)
        
        # run loop to detect courses that can be marked as ready
        while ready:
            course = ready.popleft()
            finished+=1
            # detect courses that had dep on course
            for c in adj[course]:
                indegree[c] -=1
                if indegree[c] == 0:
                    ready.append(c)

        return finished == numCourses