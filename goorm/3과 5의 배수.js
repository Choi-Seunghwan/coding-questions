// Run by Node.js
function solution(args) {
  const N = Number(args[0]);
  let sum = 0;

  for (let i = 1; i <= N; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }

  console.log(sum);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  solution([line]);

  rl.close();
}).on("close", function () {
  process.exit();
});
