class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        
        l,r = 0, len(heights)-1

        while l<r:
            # get area
            area = min(heights[l],heights[r])*(r-l)

            # evaluate if area is larger
            most = max(area,most)

            # move shorter pointer (shorter pointer is limiting factor)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return most