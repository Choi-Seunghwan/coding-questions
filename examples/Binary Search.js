// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const bs = (arr, l, r, target) => {
  const m = parseInt((l + r) / 2);

  if (l <= r) {
    if (arr[m] === target) {
      return m + 1;
    } else if (arr[m] < target) {
      return bs(arr, m + 1, r, target);
    } else if (arr[m] > target) {
      return bs(arr, l, m - 1, target);
    }
  } else {
    return false;
  }
};

const solution = (nums, target) => {
  const arr = nums.split(" ").map((i) => Number(i));

  const result = bs(arr, 0, arr.length - 1, target);

  if (result) console.log(result);
  else console.log("X");
};

let lineCount = 0;
let nums;

rl.on("line", function (line) {
  switch (lineCount) {
    case 0:
      break;
    case 1:
      nums = line;
      break;
    case 2:
      solution(nums, Number(line));
      rl.close();
  }
  ++lineCount;
}).on("close", function () {
  process.exit();
});
