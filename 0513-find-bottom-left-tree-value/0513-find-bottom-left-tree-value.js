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
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    var max_dep = 0;
    var result = root.val;
    var dfs = function(node, depth, isleft) {
        if(!node) return;
        if(depth > max_dep) {
            max_dep = depth
            // if(isleft) result = node.val
            result = node.val
        }
        dfs(node.left, depth + 1, true)
        dfs(node.right, depth + 1, false)
    }
    dfs(root, 0, true)
    return result;
};