import time


class Node(object):
    """节点对象"""

    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class LoopSingleLinkedList(object):

    def __init__(self, head=None):
        self.__head = head


    def is_empty(self):
         return self.__head == None

    def append(self, element):
        """尾插法"""
        cur = self.__head
        node = Node(element)
        # 如果链表为空的操作,只需要把node.next指向自己即可
        if self.is_empty():
            node.next = node
            self.__head = node
        # 如果非空，则把游标滑到尾部
        else:
            # 把游标划到尾部,cur.next指向新节点，新节点的next指向头
            while  cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head


    def add(self, item):
        """头插法"""
        # 上来先判断是否为空链表
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        # 如果不是空链表，那需要在头插入后，还需要在滑动到尾部，把尾部的next修改成新的__head
        else:
            # 在头插入node
            node.next = self.__head
            # 然后，滑动游标到尾部
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 滑动到尾部后，把尾部的next指向新的node
            self.__head = node
            cur.next = self.__head






    def traver(self):
        if self.__head is None:
            print ("")
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem)
                cur = cur.next
            # 遍历完成以后，处于尾部，也需要把尾部打印出来
            print(cur.elem)


    def lenth(self):
        """长度"""
        cur = self.__head
        count = 0
        # 判断链表是否为空
        if cur is None:
            return count
        # 判断cur.next是否为__head，如果是，则处于尾部
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        count += 1
        return count


    def search(self, item):
        """判断元素是否存在于此链表中"""
        cur = self.__head
        while cur.next != self.__head:
            if item == cur.elem:
                return True
            cur = cur.next
        # 滑动到尾部后，也需要对最后一个节点进行判断。
        if item == cur.elem:
            return True
        return False



    def insert(self, pos, item):
        """插入"""

        if (pos-1) < 0:
            # 如果位置为0，即头部插入
            self.add(item)
        elif (pos-1) >= self.lenth():
            # 位置大于或等于链表的最长长度，即尾部插入
            self.append(item)
        # 其他情况，就移动游标到pos-1的位置处进行插入
        else:
            pre = self.__head
            # count计数，用于移动游标
            count = 0
            # 每次count+1 一直加到count和pos位置相等位置然后才退出循环，退出循环后，就处于pos-1位置
            while count < (pos-1):
                count += 1
                pre = pre.next

            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """根据item删除链表"""
        cur = self.__head
        pre = None
        remove_ver = self.__head
        # 如果链表只有一个节点，则不会进入循环
        while cur.next != self.__head:
            # 如果条件成立，就意味着需要删除这个节点
            if cur.elem == item:
                # 如果是头部删除，需要在尾节点重新指向
                if cur == self.__head:
                    # 先滑动到尾部
                    while remove_ver.next != self.__head:
                        remove_ver = remove_ver.next
                    self.__head = cur.next
                    remove_ver.next = self.__head
                    cur.next = None
                    return cur.elem
                else:
                    pre.next = cur.next
                    cur.next = None
                    return cur.elem
            else:
                pre = cur
                cur = cur.next

        # 判断链表是否只有一个节点
        if cur == self.__head:
            if cur.elem == item:
                self.__head = None
                cur = None
                return cur.elem
        # 如果上面不成立，则需要判断尾部是否符合条件
        else:
            if cur.elem == item:
                pre.next = cur.next
                cur = None









if __name__ == "__main__":
    ss = LoopSingleLinkedList()


    ss.add(4)
    ss.append(6)
    ss.append(7)
    ss.append(8)
    ss.traver()
    ss.remove(8)
    ss.traver()
    ss.insert(6, 1)
    ss.traver()

