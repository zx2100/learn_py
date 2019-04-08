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
        # cur None时，执行else
        if cur:
            # 把游标划到尾部
            while  cur.next != None:
                cur = cur.next
            # 在尾部加入新元素
            node = Node(element)
            # 把当前节点的Next连接到新的节点上
            cur.next = node
        else:
            # 插入新元素
            node = Node(element)
            # 把链表的__head，指向此节点
            self.__head = node

    def add(self, item):
        """头插法"""
        # 上来先判断是否为空链表
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        # 如果不是空链表，那需要在头插入后，还需要在滑动到尾部，把尾部的next修改成新的__head
        else:
            node.next = self.__head
            # self.__head = node
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 判断链表是否只有一个节点，如果是，经过上面的循环后，cur和__head还是相等的
            if cur == self.__head:

            cur.next = self.__head



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

        if (pos-1) <= 0:
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
            # 每次count+1 一直加到count和pos位置相等位置
            while count < (pos-1):
                count += 1
                pre = pre.next

            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """根据item删除链表"""
        pre = None
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                pre.next = cur.next
                cur.next = None
                return cur.elem
            pre = cur
            cur = cur.next
        return ""







if __name__ == "__main__":
    ss = SingleLinkedList()

    start_time = time.time()


    for i in range(10000):
        ss.append(i)


    end_time = time.time()

    print("总花费%d时间"%(end_time - start_time))
    #ss.traver()



    print(ss.search(9990))
    #ss.traver()

