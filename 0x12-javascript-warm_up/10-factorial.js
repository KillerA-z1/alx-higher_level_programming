#!/usr/bin/node

// script that computes and prints a factorial

function factorial (n) {
  if (!n || isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(Number(process.argv[2])));
