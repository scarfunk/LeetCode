/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isEvenOddTree = function(root) {
    var que = [root];
    var depth = 1;
    while(que.length > 0) {
        var tmp = [];
        var v = [];
        for(let node of que) {
            // node.val 들 체크.
            v.push(node.val)
            if(node.left) tmp.push(node.left);
            if(node.right) tmp.push(node.right);
            
        }
        // node.val 들 체크.
        if(depth % 2 === 0) { // 짝수면 desc
            for(let i = 1; i <= v.length; i++) {
                if(v[i-1] % 2 !== 0 || v[i-1] <= v[i]) return false
            }
            
        } else {
            for(let i = 1; i <= v.length; i++) { // 홀수면 asc

                if(v[i-1] % 2 === 0 || v[i-1] >= v[i]) return false
            }
        }

        // 모은것을 큐로 초기화
        que = tmp
        depth++;
    }
    return true;
    
}