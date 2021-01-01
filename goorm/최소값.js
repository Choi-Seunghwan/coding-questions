// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let lineCount = 0;
let n = 0;
function solution(input) {
  input = input.split(" ").map((e) => {
    return Number(e);
  });
  console.log(Math.min(...input));
}

rl.on("line", function (line) {
  lineCount++;
  switch (lineCount) {
    case 1:
      n = Number(line);
      break;
    case 2:
      solution(line);
      rl.close();
      break;
    default:
      rl.close();
      break;
  }
}).on("close", function () {
  process.exit();
});

///////////////

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let lineCount = 0;

rl.on("line", function (line) {
  if (lineCount === 0) {
    lineCount += 1;
    return;
  }
  const temp = line.split(" ").map((item) => parseFloat(item));
  console.log(Math.min(...temp));

  rl.close();
}).on("close", function () {
  process.exit();
});
