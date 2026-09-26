class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = new Map();

        // count frequencies
        for (let num of nums) {
            freq.set(num, (freq.get(num) || 0) + 1);
        }

        let holders = Array(nums.length+1).fill(null).map(()=>[])
        for(let [value,count] of freq.entries()){
            holders[count].push(value);
        }
        
        const res = [];
        for (let i = holders.length - 1; i >= 0 && res.length < k; i--) {
            if (holders[i].length > 0) {
                res.push(...holders[i]);
            }
        }

        return res;
    }
}
