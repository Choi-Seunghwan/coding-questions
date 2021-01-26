function isOverlap(rectA, rectB) {
  if (
    rectA[0] < rectB[2] &&
    rectB[0] < rectA[2] &&
    rectA[1] < rectB[3] &&
    rectB[1] < rectA[3]
  ) {
    return true;
  }

  return false;
}

function solution(boxes) {
  const answer = [];
  const paintedBoxes = [];

  for (let i = 0; i < boxes.length; i++) {
    let flag = true;

    for (const paintedBox of paintedBoxes) {
      if (isOverlap(boxes[i], paintedBox)) {
        flag = false;
        break;
      }
    }
    if (flag) {
      paintedBoxes.push(boxes[i]);
      answer.push(i);
    }
  }

  return answer;
}
