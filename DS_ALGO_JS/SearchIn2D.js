let a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
let m = 3,
  n = 3; //n x m = size of matrix (3x3)
let i = 0,
  j = n - 1; //j=2 which is last element of 1st row
let t = 19;
let found = 0;

while (i < n && j >= 0) {
  if (t == a[i][j]) {
    console.log("Found");
    found = 1;
    return;
  } else {
    if (t < a[i][j]) {
      j--;
    } else {
      i++;
    }
  }
}
if (found == 0) {
  console.log("Not Found");
}
