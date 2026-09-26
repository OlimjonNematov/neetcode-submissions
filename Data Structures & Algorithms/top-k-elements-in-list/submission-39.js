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

        // convert to array and sort by frequency
        const sorted = [...freq.entries()].sort((a, b) => b[1] - a[1]);
    console.log(sorted)
        // take top k
        return sorted.slice(0, k).map(([num, _]) => num);
    }
}
