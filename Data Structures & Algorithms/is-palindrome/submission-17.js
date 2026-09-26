class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let p1 = 0;
        let p2 = s.length-1;

        const isAlphaNum=(c)=>{
            return (c >= 'A' && c <= 'Z')||(c >= 'a' && c <= 'z')||(c >= '0' && c <= '9');
        }

        while(p1<p2){
            while(!isAlphaNum(s.charAt(p1)) && p1<p2){
                p1++;
            }

            while(!isAlphaNum(s.charAt(p2)) && p1<p2){
                p2--;
            }

            if (s.charAt(p1).toLowerCase()!==s.charAt(p2).toLowerCase()){
                return false;
            }
            p1++;
            p2--;
        }

        return true;
    }
}
