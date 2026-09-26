class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        if(s.length !== t.length)
            return false;

        let freq = new Array(26).fill(0);
    
        for(let char of s){
            let i = char.charCodeAt(0)-'a'.charCodeAt(0)
            console.log(i)
            freq[i]+=1;
        }

        for(let char of t){
            let i = char.charCodeAt(0)-'a'.charCodeAt(0)
            freq[i]-=1;
        }
    console.log(freq)
        for(let count of freq){
            if(count!==0){
                return false;
            }
        }

        return true;
    }

}
