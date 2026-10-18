/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        
        TreeNode invertedLeft = invertTree(root.left);
        TreeNode invertedRight = invertTree(root.right);

        root.left = invertedRight;
        root.right = invertedLeft;

        return root;
    }
}

// SECOND SOLUTION
// class Solution {
//     public TreeNode invertTree(TreeNode root) {
//         if (root == null) return root;
//         Queue<TreeNode> q = new LinkedList<>();
//         q.offer(root);
        
//         while (!q.isEmpty()) {
//             TreeNode currentNode = q.poll();
//             TreeNode temp = currentNode.left;
//             currentNode.left = currentNode.right;
//             currentNode.right = temp;

//             if (currentNode.left != null) {
//                 q.offer(currentNode.left);
//             }

//             if (currentNode.right != null) {
//                 q.offer(currentNode.right);
//             }
//         }
        
//         return root;
//     }
// }
