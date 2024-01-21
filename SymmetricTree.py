# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import SimpleQueue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            queue = SimpleQueue()
            queue.put(p)
            queue.put(q)

            while not queue.empty():
                first = queue.get()
                second = queue.get()

                if not first and not second:
                    continue
                elif not first or not second or first.val != second.val:
                    return False
                
                queue.put(first.left)
                queue.put(second.right)
                queue.put(first.right)
                queue.put(second.left)

            return True

        return isMirror(self,root,root)
