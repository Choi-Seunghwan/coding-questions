/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function (arr) {
  const resultArr = [...arr];

  for (let i = 0; i < arr.length - 1; i++) {
    resultArr[i] = Math.max(...arr.slice(i + 1));
  }

  resultArr[resultArr.length - 1] = -1;
  return resultArr;
};
