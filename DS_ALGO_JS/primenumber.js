let num = 5;
let isPrime = true;
if (num == 1) {
  console.log("1 is neither prime nor composite.");
} else if (num > 1) {
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      isPrime = false;
    }
  }
  if (isPrime) {
    console.log(`${num} is prime number`);
  } else {
    console.log(`${num} is a not prime number`);
  }
} else {
  console.log("invalid no");
}
