const getP = (N) => {
  let n = N;
  divVal = 2;

  while (n > 1) {
    if (n % divVal === 0) {
      n /= divVal;
      console.log(divVal);
    } else {
      divVal++;
    }
  }
};

getP(120);
