// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function s(input){
	let count1 = 0; // 1
	let count2 = 0; // I
	let count3 = 0; // l
	let count4 = 0; // |
	
	for(let i = 0; i < input.length; i++){
		switch(input[i]){
			case '1':
				++count1;
				break;
			case 'I':
				++count2;
				break;
			case 'l':
				++count3;
				break;
			case '|':
				++count4;
				break;
			default:
				break;
		}
	}
	console.log(`${count1}\n${count2}\n${count3}\n${count4}`);
}

rl.on("line", function(line) {
	s(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
