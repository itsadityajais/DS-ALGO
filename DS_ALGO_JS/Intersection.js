function unntersectionion(arr1, arr2, m, n) {
  let i = 0,
    j = 0;
  while (i < m && j < n) {
    if (arr1[i] < arr2[j]) {
      i++;
    } else if (arr2[j] < arr1[i]) {
      j++;
    } else {
      console.log(arr2[j]);
      i++;
      j++;
    }
  }
}

let arr1 = [1, 3, 4, 5, 6];
let arr2 = [1, 2, 4, 5, 7];
let m = arr1.length;
let n = arr2.length;
intersection(arr1, arr2, m, n);
