/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    var pos = []
    var negs = []
    for(var n of nums) {
        if(n > 0) pos.push(n)
        if(n < 0) negs.push(n)
    }
    var ret = []
    for(var i = 0; i < pos.length; i++) {
        ret.push(pos[i])
        ret.push(negs[i])
    }
    return ret;
};