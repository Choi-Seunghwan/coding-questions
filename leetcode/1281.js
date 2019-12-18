/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(x) {
    let mulResult = 1;
    let sumResult = 0;
    let temp;
    while(x > 0){
        temp = x % 10;
        mulResult *= temp;
        sumResult += temp;
        x = parseInt(x/10);
    }
    return mulResult - sumResult;
};
