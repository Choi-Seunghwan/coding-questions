// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function solution(input){
	const splittedInput = input.split(' ');
	console.log(splittedInput[0] >> splittedInput[1]);
	console.log(splittedInput[0] << splittedInput[1]);
}

rl.on("line", function(line) {
	solution(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
