'''
There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.
 
 '''
 from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u, v in relations: 
            graph[u].append(v) 		# Build Graph. 
            indegree[v] += 1        # Count Indegree of v for u -> v.
        
        q = deque([(1, i) for i in range(1, N+1) if indegree[i] == 0]) # Put all (level, vertex) in Q, whose indegree is 0. level = 1 
        visited = set()
        answer = 0
        
        while q:
            level, u = q.popleft()
            next_ = []
            visited.add(u)  # Keep track of levels.
            answer = max(level, answer) # Since answer we are looking is maximum levels to complete all the courses.
            for v in graph[u]:
                if indegree[v] > 0:
                    indegree[v] -= 1
                if indegree[v] == 0:
                    q.append((level+1, v)) # If Indegree of a vertex v is 0, put (level+1, v) in the q.

        return answer if len(visited) == N else -1 # Return answer only if we can complete all courses, else -1
