def postorder(root, result):
    if not root:
        return
    # Explore left
    postorder(root.left, result)
    # Explore right
    postorder(root.right, result)
    # Visit the root
    result.append(root.val)

res = []
postorder(root, res)
print(res)  # [4, 5, 2, 6, 3, 1]
