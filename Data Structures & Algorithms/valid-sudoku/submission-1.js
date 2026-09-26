class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let seenInRow = new Map();
        let seenInColumn= new Map();
        let seenInBox = new Map();

        for(let r =0; r<9; r++){
            for(let c = 0; c<9; c++){
                const boxIndex = `${Math.floor(r/3)},${Math.floor(c/3)}`; 
                const value = board[r][c];
                if(value === '.') continue;

                // check for doups
                if(seenInRow.get(r) && seenInRow.get(r).has(value)){ //check if it exists in row
                    return false
                }else if(seenInColumn.get(c) && seenInColumn.get(c).has(value)){ // check if exists in cols
                    return false
                }else if(seenInBox.get(boxIndex) && seenInBox.get(boxIndex).has(value)){
                    return false
                }

                // init sets
                if(!seenInRow.has(r)){                   
                    seenInRow.set(r, new Set());
                }

                if(!seenInColumn.has(c)){
                    seenInColumn.set(c, new Set())
                }
                
                if(!seenInBox.has(boxIndex)){
                    seenInBox.set(boxIndex, new Set())
                }

                // Put data inside each of the sets
                seenInRow.get(r).add(value);
                seenInColumn.get(c).add(value);
                seenInBox.get(boxIndex).add(value);
            }
        }
        return true;
    }
}
