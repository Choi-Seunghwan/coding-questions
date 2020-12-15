// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  let numStr = "";
  const N = Number(line);
  for (let i = 1; i <= N; i++) if (N % i === 0) numStr += `${i} `;

  console.log(numStr);
  rl.close();
}).on("close", function () {
  process.exit();
});
