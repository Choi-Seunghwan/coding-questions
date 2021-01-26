let landSize = 0;

function search(i, j, bitmap) {
  if (
    i < 0 ||
    i >= bitmap.length ||
    j < 0 ||
    j >= bitmap[0].length ||
    bitmap[i][j] !== 1
  )
    return;

  landSize += 1;
  bitmap[i][j] = 0;

  search(i + 1, j, bitmap);
  search(i - 1, j, bitmap);
  search(i, j + 1, bitmap);
  search(i, j - 1, bitmap);
}

function solution(bitmap) {
  const answer = [];

  for (let i = 0; i < bitmap.length; i++) {
    for (let j = 0; j < bitmap[0].length; j++) {
      if (bitmap[i][j] === 1) {
        search(i, j, bitmap);
        answer.push(landSize);
        landSize = 0;
      }
    }
  }
  answer.sort((a, b) => a - b);
  return answer;
}
