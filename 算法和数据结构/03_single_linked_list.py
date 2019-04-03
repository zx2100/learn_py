class Node(object):
    """节点对象"""

    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class SingleLinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
         return self.head == None

    def append(self, element):
        """在尾部插入元素"""
        cur = self.head
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
            # 把链表的head，指向此节点
            self.head = node

    def traver(self):
        cur = self.head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def lenth(self):
        """长度"""
        cur = self.head
        count = 0
        # 注意，不是判断cur.next ，因为如果这样判断的话，最后一个元素就不符合条件，会导致少一个
        # 所以直接判断cul会好点，因为最后一个next是空，让cur=None是没问题的
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        """判断元素是否存在于此链表中"""
        cur = self.head
        while cur != None:
            if item == cur.elem:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    ss = SingleLinkedList()
    ss.append(1)
    ss.append(2)
    ss.append(3)
    ss.append([1, 2, 3, 4])
    ss.traver()
    #print(ss.lenth())
    print(ss.search("1234"))

