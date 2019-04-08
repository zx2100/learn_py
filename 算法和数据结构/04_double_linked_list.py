import time


class Node(object):
    """节点对象"""

    def __init__(self, elem, _next=None, _prev=None):
        self.elem = elem
        self.next = _next
        self.prev = _prev

class DoubleLinkedList(object):

    def __init__(self, head=None):
        self.__head = head



    def is_empty(self):
         return self.__head is None

    def append(self, element):
        """尾插法"""
        node = Node(element)
        # 先判断当前链表是否为空
        if self.is_empty():
            node.prev = None
            node.next = None
            self.__head = node
            return
        cur = self.__head
        # 移动cur到尾部
        while cur.next is not None:
            cur = cur.next
        # 到达尾部后，执行插入操作
        node.prev = cur
        node.next = cur.next
        cur.next = node



    def add(self, item):
        """头插法"""
        node = Node(item)

        node.next = self.__head
        node.prev = None
        self.__head = node


    def traver(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def lenth(self):
        """长度"""
        cur = self.__head
        count = 0
        # 注意，不是判断cur.next ，因为如果这样判断的话，最后一个元素就不符合条件，会导致少一个
        # 所以直接判断cul会好点，因为最后一个next是空，让cur=None是没问题的
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        """判断元素是否存在于此链表中"""
        cur = self.__head
        while cur != None:
            if item == cur.elem:
                return True
            cur = cur.next
        return False


    def insert(self, pos, item):
        """插入"""
        # 判断是否首部插入
        if pos <= 0:
            self.add(item)
            return
        # 判断是否尾部插入
        elif (pos-1) >= self.lenth():
            self.append(item)
            return

        # 其他就是中间插入了
        else:
            node = Node(item)
            cur = self.__head
            # 判断是否是空链表
            if cur == None:
                self.add(item)
                return
            # 移动游标，到指定位置的前1个
            count = 0
            while count < (pos-1):
                cur = cur.next
                count += 1
            # 循环退出，cur指向指定位置的前一个
            # 判断链表是否只有一个元素。如果只有一个元素，那经过上面的循环后，cur和self.__self还是相等的
            if cur == self.__head:
                node.prev = None
                node.next = cur
                self.__head = node
            else:
                node.next = cur.next
                node.prev = cur
                cur.next = node



    def remove(self, item):
        """根据item删除链表"""
        # 先判断链表是否为空
        if self.is_empty():
            return ""
        else:
            cur = self.__head
            # 移动节点到需要删除的位置上
            while cur is not None:
                # 如果和需要删除的元素相等，则需要把它删除
                if cur.elem == item:
                    # 首先如果是第一个节点，则把self.__head 指向cur.next即可，perv= None
                    if cur == self.__head:
                        self.__head = cur.next
                        # 然后判断整个链表是否只有一个节点,只有不为none，才去运行里面的语句
                        if cur.next:
                            cur.next.perv = None
                            cur.next = None
                        return cur.elem
                    else:
                        cur.prev.next = cur.next
                        # 如果是尾部，cur.next则为none.所以，需要这这里做一个判断。
                        if cur.next:
                            cur.next.perv = cur.prev
                        return cur.elem
                # 否则把游标移动到下一个位置。
                cur = cur.next

            return ""









if __name__ == "__main__":


    dl = DoubleLinkedList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.append(4)

    dl.insert(2, 5)
    dl.traver()
    print(dl.remove(2))
    print("-----")
    dl.traver()