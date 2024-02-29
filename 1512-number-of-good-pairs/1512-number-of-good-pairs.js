/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    var mem = {}

    for(let i = 0; i < nums.length; i++) {
        mem[nums[i]] = (mem[nums[i]] || 0) + 1;
    }
    let sum = 0;
    console.log(mem)
    for(let n of Object.values(mem)) {
        console.log(n)
        sum += n * (n-1) / 2
    }
    return sum;
};