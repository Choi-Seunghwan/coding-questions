// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function solution(input){
	const splittedInput = input.split(' ').map( el => Number(el));
	console.log(Math.min(...splittedInput));	
}

rl.on("line", function(line) {
	solution(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
