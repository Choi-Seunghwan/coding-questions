const reverse = (str) => {
  const arr = [...str];
  let l = 0;
  let r = arr.length - 1;

  while (l < r) {
    let temp = arr[l];
    arr[l] = arr[r];
    arr[r] = temp;

    l += 1;
    r -= 1;
  }

  return arr.join("");
};

const reverse2 = (str) => {
  return str.split("").reverse().join("");
};

console.log(reverse2("hello"));
