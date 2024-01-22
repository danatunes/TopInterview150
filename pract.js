  // Javascript code for
    // O(n) solution for finding
    // maximum sum of a subarray
    // of size k
    // function maxSum(arr, n, k) {
    //     let max = 0;
    //     let sum = 0;
    //     // find initial sum of first k elements
    //     for (let i = 0; i < k; i++) {
    //         sum += arr[i];
    //         max = sum;
    //     }
    //     // iterate the array once
    //     // and increment the right edge
    //     for (let i = k; i < n; i++) {
    //         sum += arr[i] - arr[i - k];
    //          console.log(arr[i - k]);
    //          console.log(arr[i]);
    //         // compare if sum is more than max,
    //         // if yes then replace
    //         // max with new sum value
    //         if (sum > max) {
    //             max = sum;
    //         }
    //     }
    //     return max;
    // }
 
// Driver code
// let arr = [8, 4, 2, 10, 2, 3, 1, 0, 20];
// let k = 4;
// let n = arr.length;
// console.log(maxSum(arr, n, k));

//[2,3,1,1,4]

// var jump = function(nums) {
//     let maxMove = 0;
//     let oldMove = 0;
//     let jump = 0;

//     for(let i = 0; i < nums.length-1; i++){
//         // Keeping track of the max jump
//         console.log(nums[i] + " nums[i] ");
//         maxMove = Math.max(maxMove, i + nums[i])
//         console.log(maxMove + "  maxMove");

//         // When we get to the index where we had our previous max jump, we increase our jump count by 1
//         console.log(i + " " + oldMove)
//         if(i == oldMove){
//             console.log('oldMove');
//             jump++
//             oldMove = maxMove
//         }
//     }

//     return jump;
// };


// console.log(jump([2,3,1,1,4]))




// function func() {
// 	let arr = ["shift", "splice", "filter", "pop"];

// 	// Removing the specified element from the array
// 	let spliced = arr.splice(2, 1);
// 	console.log("Removed element: " + spliced);
// 	console.log("Remaining elements: " + arr);
// }
// func();

// var productExceptSelf = function(nums) {
//   const n = nums.length;
//   const result = new Array(n).fill(1);
//   let leftProduct = 1;
//   let rightProduct = 1;

//   for (let i = 0; i < n; i++) {
//       result[i] *= leftProduct;
//       result[n - 1 - i] *= rightProduct;
//       leftProduct *= nums[i];
//       rightProduct *= nums[n - 1 - i];
//     }

//   return result;
// };

// productExceptSelf([1,2,3,4])


// var reverseWords = function(s) {
//   const arraySplitedArray = s.trim().split(" ");
//   const array = arraySplitedArray.filter((item) => item);
//   const length = array.length;
//   while(length){
    
//   }
//   return array;
// };

// console.log(reverseWords("blue is sky the"));

