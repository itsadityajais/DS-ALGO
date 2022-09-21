let arr = [3.5, 7, 2, 8, 6];
let n = arr.length;
let k = 5;
function bubblesort(arr) {
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log("Sorted array=" + arr);
}
bubblesort(arr);

let small = arr[0] + k;
let big = arr[n - 1] - k;
if (n == 1) {
  console.log("Enter atleast 2 elements to fix the difference");
  return 0;
}
if (small > big) {
  let temp = small;
  small = big;
  big = temp;
}
let ans = big - small;
console.log("Min Diff b/w heights= " + ans);

// if (small>big){
//     let temp=small;
//     small=big;
//     big=temp;
// }
// console.log("big= "+big,"small= "+small)

// for (let i = 1; i < n-1; i ++)
//     {
//         let subtract = arr[i] - k;
//         let add = arr[i] + k;
// if(big-subtract<=add-small)
//    small=subtract;
// else
//    big=add;

// console.log(ans)

// let min,max;
// let k=2;
// let ans = arr[n-1] - arr[0];
// console.log(ans);

//     for(let i=1;i<=n-1;i++){
//         if(arr[i] >= k){
//             max=arr[n-1]-k;
//             min=arr[i]-k;
//             ans =(max- min);
//         }
//     }
//     console.log("ans= "+ans)
