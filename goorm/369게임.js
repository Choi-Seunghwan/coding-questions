// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function solution(input){
	const times = parseInt(input)
	let count = 0;
	
	for(let i = 1; i <= times; i++ ){
		let temp = String(i);
		for(let j = 0; j < temp.length; j++){
			switch(temp[j]){
				case '3':
				case '6':
				case '9':
					count++;
					break;
			}
		}	
	}
	return count;
}

rl.on("line", function(line) {
	console.log(solution(line));
	rl.close();
}).on("close", function() {
	process.exit();
});
