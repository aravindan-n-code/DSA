class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = deque([(root, 0)])

        while(queue):
            node, level = queue.popleft()
            if len(ans) <= level:
                ans.append(deque())

            if level%2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].appendleft(node.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        return [list(d) for d in ans]
