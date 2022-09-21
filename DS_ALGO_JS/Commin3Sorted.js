let arr1 = [1, 2, 3];
let arr2 = [1, 2, 3, 4];
let arr3 = [1, 2, 3, 4, 5];
let n1 = arr1.length;
let n2 = arr2.length;
let n3 = arr3.length;
let i = 0,
  j = 0,
  k = 0;

while (i < n1 && j < n2 && k < n3) {
  if (arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
    console.log(arr1[i]);
    i++;
    j++;
    k++;
  } else if (arr1[i] < arr2[j]) {
    i++;
  } else if (arr2[j] < arr3[k]) {
    j++;
  } else {
    k++;
  }
}
