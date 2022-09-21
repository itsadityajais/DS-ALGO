function union(arr1, arr2, m, n) {
  let i = 0,
    j = 0;
  while (i < m && j < n) {
    if (arr1[i] < arr2[j]) {
      console.log(arr1[i]);
      i++;
    } else if (arr2[j] < arr1[i]) {
      console.log(arr2[j]);
      j++;
    } else {
      console.log(arr2[j]);
      i++;
      j++;
    }
  }
  while (i < m) {
    console.log(arr1[i]);
    i++;
  }

  while (j < n) {
    console.log(arr2[j]);
    j++;
  }
  return 0;
}

let arr1 = [1, 3, 4, 5, 6];
let arr2 = [1, 2, 4, 5, 7];
let m = arr1.length;
let n = arr2.length;
union(arr1, arr2, m, n);
