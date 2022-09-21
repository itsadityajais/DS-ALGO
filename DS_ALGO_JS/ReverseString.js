function reverseString(str) {
  let newString = "";
  for (let i = str.length - 1; i >= 0; i--) {
    newString = newString + str[i];
  }
  return newString;
}

let string = "ADITYA";
let result = reverseString(string);
console.log(result);
