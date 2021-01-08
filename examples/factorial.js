const factorial = (N) => {
  if (N <= 1) return 1;
  return N * factorial(N - 1);
};

const result = factorial(5);
console.log(result);
