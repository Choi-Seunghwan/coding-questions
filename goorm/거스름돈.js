// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const s = input => {
	let result = 1000 - Number(input);
	let c1, c2, c3, c4;
	
	c1 = parseInt(result/500);
	result %= 500;
	c2 = parseInt(result/100);
	result %= 100;
	c3 = parseInt(result/50);
	result %= 50;
	c4 = parseInt(result/10);
	result %= 10;
		
	console.log(`${c1} ${c2} ${c3} ${c4} `);
}

rl.on("line", function(line) {
	s(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
