// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  const kw = Number(line);
  let reulst;

  if (kw >= 300) {
    result = kw * 0.01;
  } else if (kw >= 200) {
    result = kw * 0.009;
  } else if (kw >= 100) {
    result = kw * 0.007;
  } else {
    result = kw * 0.005;
  }
  console.log(result.toFixed(2));
  rl.close();
}).on("close", function () {
  process.exit();
});
