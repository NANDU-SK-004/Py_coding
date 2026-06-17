def inorder(root, result):
    if not root:
        return
    # Explore left
    inorder(root.left, result)
    # Visit the root
    result.append(root.val)
    # Explore right
    inorder(root.right, result)

res = []
inorder(root, res)
print(res)  # [4, 2, 5, 1, 3, 6]
