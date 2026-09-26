class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let count = 0;
        
        const numSet = new Set(nums);

        for(let num of numSet){
            let length = 0;

            while(numSet.has(num+length)){
                length++;
            }
            count = Math.max(length, count);
        }

        return count;
    }
}
