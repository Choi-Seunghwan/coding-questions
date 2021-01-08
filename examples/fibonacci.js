const mem = {};

const fibo = (N) => {
  if (N <= 2) return 1;

  if (mem[N]) return mem[N];

  mem[N] = fibo(N - 2) + fibo(N - 1);
  return mem[N];
};

const result = fibo(10);
console.log(result);
