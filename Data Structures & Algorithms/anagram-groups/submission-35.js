class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        let res = new Map();

        for(let str of strs){
            let signature = new Array(26).fill(0)

            for(let c of str){
                signature[c.charCodeAt(0)-'a'.charCodeAt(0)]+=1;   
            }
            
            const key = signature.join(',')

            if(!res.get(key)) res.set(key, [])
            
            res.get(key).push(str)
        }
        return(Array.from(res.values()))
    }
}
