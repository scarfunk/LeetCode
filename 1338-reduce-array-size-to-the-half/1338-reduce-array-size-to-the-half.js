/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    var half = Math.floor(arr.length / 2);
    if(half === 0) return 1;
    var mem = {}
    for(var n of arr) {
        mem[n] = (mem[n] ?? 0) + 1
    }
    var cnt = 0;
    var sortarr = []
    for(var k in mem) {
        sortarr.push(mem[k])
    }
    sortarr.sort((a,b)=>b-a);
    for(let i = 0; i < sortarr.length; i++) {
        half -= sortarr[i]
        if(half <= 0) return i+1;
    }

    return -1

};