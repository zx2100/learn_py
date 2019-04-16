# coding: utf-8

class Node(object):

    def __init__(self, item):
        self.elem = item
        # 左子树
        self.l_child = None
        # 右子树
        self.r_child = None




class BinaryTree(object):

    def __init__(self):
        self.root = None


    def add(self, item):
        """使用广度遍历挂载数据"""
        node = Node(item)
        # 上来先判断树根是否为None
        if self.root is None:
            self.root = node
            return
        # 如果不是，则广度遍历，寻找可挂载节点
        # 使用一个列表辅助
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            # 遍历左子树
            if cur.l_child is None:
                cur.l_child = node
                return
            else:
                queue.append(cur.l_child)

            # 遍历右子树
            if cur.r_child is None:
                cur.r_child = node
                return
            else:
                queue.append(cur.r_child)


    def traversal(self):
        """遍历整棵树"""
        if self.root is None:
            return ""

        queue = [self.root]

        while queue:
            cur = queue.pop(0)
            # 打印当前节点
            print(cur.elem,end="")
            # 遍历左子树
            if cur.l_child:
                queue.append(cur.l_child)

            if cur.r_child:
                queue.append(cur.r_child)


    def pre_traversal(self, node):
        if node is None:
            return ""

        print(node.elem, end="")
        self.pre_traversal(node.l_child)
        self.pre_traversal(node.r_child)

    def in_traversal(self, node):
        if node is None:
            return ""
        self.in_traversal(node.l_child)
        print(node.elem, end="")
        self.in_traversal(node.r_child)


    def post_traversal(self, node):
        if node is None:
            return ""
        self.post_traversal(node.l_child)
        # print(node.elem, end="")
        self.post_traversal(node.r_child)
        print(node.elem, end="")




if __name__ == "__main__":

    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.traversal()
    print("")
    tree.pre_traversal(tree.root)
    print("")
    tree.in_traversal(tree.root)
    print("")
    tree.post_traversal(tree.root)