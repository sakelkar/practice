#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return true if you can finish all courses. Otherwise, return false.
#
#Example 1:
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take.
#To take course 1 you should have finished course 0. So it is possible.
#
#Example 2:
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take.
#To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#Constraints:
#    1 <= numCourses <= 2000
#    0 <= prerequisites.length <= 5000
#    prerequisites[i].length == 2
#    0 <= ai, bi < numCourses
#    All the pairs prerequisites[i] are unique.
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #so in this case each single course can have multiple dependancies
        #so for example lets say you can have something like beloe
        #[5,1], [5,2], [5,3], [5,4] etc so basically we need to know create a data structure which will
        #help us traverse the dependancies very well

        #also to be able to tell whether we can do numCourses correctly or not, we have to make sure
        #that all the courses in that range can be done or not

        #create the adjancy list for every course which will be like a list as value for the course as key
        adj = defaultdict(list)
        courses = prerequisites
        for a, b in prerequisites:
            adj[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        #check whether the course can be taken.
        #detect cycle
        def dfs(node):
            if states[node] == VISITED: return True
            elif states[node] == VISITING: return False

            states[node] = VISITING
            #now visit all the nodes in the adjancencies of this node
            for nei in adj[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True

        for course in courses:
            if not dfs(course):
                return False

        return True

