// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
// 정규표현식이 편할 듯... -ㅁ-;;
const getDate = input => {
	
}

const s = lines => {
	let dateList = [];
	
	for(let i = 0; i < lines.length; i++){
		dateList.push( getDate(lines[i]));
		
	}
	
}

let lineCount = 0;
let lines = [];
rl.on("line", function(line) {
	s(line);
	switch(lineCount){
		case 0:
		case 1:
			lines.push(line);
			break;
		case 2:
			lines.push(line);
			s(lines);
			break;
		default:
			break;
			rl.close();
	}
}).on("close", function() {
	process.exit();
});
