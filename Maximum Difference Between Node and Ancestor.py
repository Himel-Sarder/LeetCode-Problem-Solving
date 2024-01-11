class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, minval, maxval):
            if not root:
                return [minval, maxval]
            lmin, lmax = dfs(root.left,min(root.val,minval), max(root.val, maxval))
            rmin, rmax = dfs(root.right,min(root.val,minval), max(root.val, maxval))
            if abs(lmax - lmin) > abs(rmax - rmin):
                return [lmin, lmax]
            else:
                return [rmin, rmax]
        min1, max1 = dfs(root.left,root.val, root.val)
        min2, max2 = dfs(root.right, root.val, root.val)
        return max(abs(max1 - min1), abs(max2 - min2))
