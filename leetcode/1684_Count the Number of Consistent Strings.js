var countConsistentStrings = function (allowed, words) {
  let count = 0;
  for (word of words) {
    let flag = true;

    for (ch of word) {
      if (!allowed.includes(ch)) {
        flag = false;
        break;
      }
    }
    if (flag) count += 1;
  }

  return count;
};
