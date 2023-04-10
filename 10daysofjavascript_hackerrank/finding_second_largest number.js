function getSecondLargest(nums) {
    // we are removing duplicates 
    let new_nums = [...new Set(nums)];
    // sort in descending order 
    new_nums.sort(function(a, b) {return b- a}); 

    if(new_nums.length < 2 ) {
        return null;
    }else {
        return new_nums[1]; // returns the second largest number 
    }
}

let new_nums = [ 2, 3, 6, 6, 5];
let SecondLargest = getSecondLargest(nums);
console.log(SecondLargest);