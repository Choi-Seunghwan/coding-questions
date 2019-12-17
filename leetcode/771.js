/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    let count = 0;
    
    for(const c of S)
        if(J.includes(c)) ++count;
    
    return count;
};
