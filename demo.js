// arry=[4,7,9,10,7,14,12,4,7,27]
// count=0
// value=7

// for(let i=0; i<arry.length; i++){
//     if(value===arry[i]){
//         count++
//     }
// }
// console.log(count);


let array1 = [11, 1, 13, 21, 3, 7];
let array2 = [6, 8, 9, -1, 14, 8, -3, 6];
function hasNegativeNumbers(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            return "Yes";
        }
    }
    return "No";
}
console.log(hasNegativeNumbers(array1));  // Output: No
console.log(hasNegativeNumbers(array2));  // Output: Yes
