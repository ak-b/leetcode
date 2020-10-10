'''
rialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Example:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Approach 1: Depth First Search (DFS)
The serialization of a Binary Search Tree is essentially to encode its values and more importantly its structure. One can traverse the tree 
to accomplish the above task. And it is well know that we have two general strategies to do so:

Breadth First Search (BFS)
We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher level would be visited 
before the ones with lower levels.

Depth First Search (DFS)
In this strategy, we adopt the depth as the priority, so that one would start from a root and reach all the way down to certain leaf, 
and then back to root to reach another branch.The DFS strategy can further be distinguished as preorder, inorder, and postorder depending on
the relative order among the root node, left node and right node.

In this task, however, the DFS strategy is more adapted for our needs, since the linkage among the adjacent nodes is naturally encoded
in the order, which is rather helpful for the later task of deserialization.
'''
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
       
'''
The preorder DFS traverse follows recursively the order of
root -> left subtree -> right subtree.
'''
# Serialization 
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

# Deserialization 
class Codec:

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
  
'''
Complexity Analysis

Time complexity : in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is O(N), 
where N is the number of nodes, i.e. the size of tree.
Space complexity : in both serialization and deserialization functions, we keep the entire tree, either at the beginning or at the end, 
therefore, the space complexity is O(N).

'''
