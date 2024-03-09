/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    var mem = {}
    maxCnt = 0
    for(var n of nums) {
        mem[n] = (mem[n] ?? 0) + 1
        maxCnt = Math.max(maxCnt, mem[n])
    }
    // console.log(mem)
    return Object.values(mem).filter(v => v == maxCnt).length * maxCnt
};