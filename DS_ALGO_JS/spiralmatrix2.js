let a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
let i,
  r = 0,
  c = 0,
  row = 2,
  col = 2;
let count = 0;
while (count < 9) {
  for (i = c; i <= col; i++) {
    console.log(a[r][i]);
    count++;
  }
  r++;
  //count=3
  for (i = r; i <= row; i++) {
    console.log(a[i][col]);
    count++;
  }
  col--;
  //count=5
  for (i = col; i >= c; i--) {
    console.log(a[row][i]);
    count++;
  }
  row--;
  //count=7

  for (i = row; i >= r; i--) {
    console.log(a[i][c]);
    count++;
  }
  c++;
  //count=8
}
