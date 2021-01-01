// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const s = (line) => {
  let cObj = {
    a: 0,
    b: 0,
    c: 0,
    d: 0,
    e: 0,
    f: 0,
    g: 0,
    h: 0,
    i: 0,
    j: 0,
    k: 0,
    l: 0,
    m: 0,
    n: 0,
    o: 0,
    p: 0,
    q: 0,
    r: 0,
    s: 0,
    t: 0,
    u: 0,
    v: 0,
    w: 0,
    x: 0,
    y: 0,
    z: 0,
  };

  for (ch of line.toLowerCase()) {
    if (ch === " ") continue;
    cObj[ch] += 1;
  }

  for (item in cObj) {
    console.log(`${item} : ${cObj[item]}`);
  }
};

rl.on("line", function (line) {
  s(line);
  rl.close();
}).on("close", function () {
  process.exit();
});
