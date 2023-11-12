class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        preq=[[] for _ in range(numCourses+1)]
        # make an n*m array for all the preq course needed for course n
        for course, preqs in prerequisites:
            preq[course].append(preqs)
        
        taken=[0 for _ in range(numCourses+1)]
        # 0: not yet thinking about
        # 1: taken
        # -1: needed to take
        def findConflict(course):
            # return True (no conflict)  if course taken
            if taken[course]==1: return True
            # return False if course needed to take and needed again
            if taken[course]==-1: return False

            # mark to needed if not yet thinking about
            taken[course] = -1
            # trace through the preq
            for i in preq[course]:
                if findConflict(i)==False:
                    return False
            # if preq is good, markas taken
            taken[course] = 1
            return True

        for i in range(numCourses+1):
            if findConflict(i)==False:
                return False
        
        return True
        

            
