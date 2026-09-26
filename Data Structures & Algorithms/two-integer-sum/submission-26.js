class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        for(let num of nums){
            const indexOfNum=nums.indexOf(num)

            nums[indexOfNum] = null // prevet using the current

            if(nums.includes(target-num)){
                return [indexOfNum, nums.indexOf(target-num)]
            }
        }

        return false;

    }

}
