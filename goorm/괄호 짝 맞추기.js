// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (line) => {
  const s = [];
  let flag = true;

  for (ch of line) {
    if (ch === "{" || ch === "[" || ch === "(") {
      s.push(ch);
    } else {
      if (s.length < 1) {
        flag = false;
        break;
      }

      const item = s.pop();
      if (
        (item === "{" && ch !== "}") ||
        (item === "[" && ch !== "]") ||
        (item === "(" && ch !== ")")
      ) {
        flag = false;
        break;
      }
    }
  }

  if (s.length > 0) flag = false;

  if (flag) console.log("True");
  else console.log("False");
};

rl.on("line", function (line) {
  solution(line);
  rl.close();
}).on("close", function () {
  process.exit();
});
