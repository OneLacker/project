class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def deleteNode(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        else:
            # Узел с одним потомком или без потомков
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Узел с двумя потомками
            else:
                root.data = self.getMin(root.right).data
                root.right = self.deleteNode(root.right, root.data)
                
        return root
    
    def getMin(self, root):
        while root.left is not None:
            root = root.left
        return root

    def inOrder(self, root):
        # Левый узел, данные, правый узел
        result = []
        if root:
            result = self.inOrder(root.left)
            result.append(root.data)
            result += self.inOrder(root.right)
        return result

    def preOrder(self, root):
        # Данные, левый узел, правый узел
        result = []
        if root:
            result.append(root.data)
            result += self.preOrder(root.left)
            result += self.preOrder(root.right)
        return result

    def postOrder(self, root):
        # Левый узел, правый узел, данные
        result = []
        if root:
            result = self.postOrder(root.left)
            result += self.postOrder(root.right)
            result.append(root.data)
        return result

if __name__ == "__main__":
    btree = BinaryTree()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(9)

    print("In-order traversal:", btree.inOrder(root))
    print("Pre-order traversal:", btree.preOrder(root))
    print("Post-order traversal:", btree.postOrder(root))

    root = btree.deleteNode(root, 3)
    print("In-order after deleting 3:", btree.inOrder(root))