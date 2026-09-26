class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        
        # iterate through heights
        for i,a in enumerate(heights):
            j = i+1

            while j < len(heights):

                curr_most = min(a, heights[j]) * (j-i)

                most = max(curr_most, most)

                j += 1
                
            # compute max ( min between 2 pairs * distance) 

        return most