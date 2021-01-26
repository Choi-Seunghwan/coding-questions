let count = 0;

function bf(arr, numbers, target) {
  const len = numbers.length;
  if (arr.length === len) {
    const sum = arr.reduce((acc, cur) => acc + cur);
    if (sum === target) count += 1;
    return;
  }

  bf([...arr, numbers[arr.length]], numbers, target);
  bf([...arr, numbers[arr.length] * -1], numbers, target);
}

function solution(numbers, target) {
  bf([], numbers, target);
  return count;
}
