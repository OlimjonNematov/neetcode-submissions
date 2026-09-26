class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
       const uniqueElements = new Set(nums);
       return uniqueElements.size !== nums.length;
    }
}
