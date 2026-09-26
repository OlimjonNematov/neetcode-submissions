class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let map = {}

        if(s.length!==t.length) return false;

        for(let letter of s){
            map[letter]= ( map[letter] || 0) + 1;
        }

        for(let letter of t){
            map[letter]= ( map[letter] || 0 ) -1;
            if(map[letter]==-1)
            return false;
        }

        return true;
    }
}
