def preorder(root, result):
    if not root:
        return
    # Visit the root
    result.append(root.val)
    # Explore left
    preorder(root.left, result)
    # Explore right
    preorder(root.right, result)

res = []
preorder(root, res)
print(res)  # [1, 2, 4, 5, 3, 6]
