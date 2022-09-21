let arr = [-1, 2, 3];
let n = arr.length;
let curr_max = 0;
let max = 0;
for (i = 0; i < n; i++) {
  curr_max = curr_max + arr[i];
  console.log(curr_max);
  if (curr_max < 0) {
    curr_max = 0;
  }
  if (max < curr_max) {
    max = curr_max;
  }
  if (n == 1 && arr[i] < 0) {
    return 0;
  }
}

console.log("max= " + max);
