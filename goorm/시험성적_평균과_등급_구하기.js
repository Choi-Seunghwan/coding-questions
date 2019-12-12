// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const s = input => {
	const arr = input.split(' ').map( el => Number(el));
	const avg = ((arr[0]+arr[1]+arr[2])/3).toFixed(2);
	let grade = '';
	if(avg >= 90) grade = 'A';
	else if(avg >= 80) grade = 'B';
	else if(avg >= 70) grade = 'C';
	else if(avg >= 60) grade = 'D';
	else grade = 'F';
	
	console.log(avg, grade);
}

rl.on("line", function(line) {
	s(line);
	rl.close();
}).on("close", function() {
	process.exit();
});
