// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function solution(input){
	const arr = input.split(' ');
	let count = 0;
	
	for(let i = 0; i < arr.length; i++){
		if(arr[i]) count++
	}
	console.log(count);
}

rl.on("line", function(line) {
	solution(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
