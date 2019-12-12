// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function s(input){
	const mul = (a,b) => a * b;
	const arr = input.split(' ');
	const a = arr[0], b = arr[1], c = arr[2], d = arr[3];
	let result = 0;

	result = mul(mul(a, b), mul(c, d));
	console.log(result);
}

rl.on("line", function(line) {
	s(line);	
	rl.close();
}).on("close", function() {
	process.exit();
});
