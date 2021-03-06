import double_linked_list



class Queue(object):
    """使用双向链表保存数据"""

    def __init__(self):
        self.__link = double_linked_list.DoubleLinkedList()


    def push(self, item):
        """压栈操作"""
        self.__link.add(item)

    def pop(self):
        """弹栈"""
        return self.__link.pop(-1)

    def traver(self):
        self.__link.traver()


if __name__ == "__main__":
    stack = Queue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

