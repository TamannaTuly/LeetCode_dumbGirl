class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSumProperty(node):

    left_data = 0
    right_data = 0


    if ((node == None) or (node.left == None and node.right == None)) :
        return 1
    else:

        # If left child is not present then
        # 0 is used as data of left child
        if (node.left != None):
            left_data = node.left.data

        # If right child is not present then
        # 0 is used as data of right child
        if (node.right != None):
            right_data = node.right.data

        # if the node and both of its children
        # satisfy the property return 1 else 0
        if ((node.data == left_data + right_data) and
                isSumProperty(node.left) and
                isSumProperty(node.right)):
            return 1
        else:
            return 0


# Driver Code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(8)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(2)
    if (isSumProperty(root)):
        print("The given tree satisfies the",
              "children sum property ")
    else:
        print("The given tree does not satisfy",
              "the children sum property ")

# This code is contributed by PranchalK
