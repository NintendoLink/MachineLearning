# python 3.6.4
# encoding: utf-8

class Node():
    def __init__(self):
        self.hash = None
        self.key = None
        self.val = None
        self.next = None


class MyHashMap():

    def __init__(self):
        self.size_ = 0
        self.virTable = None
        self.table_ = [None for i in range(2)]

    def put(self,key,val):

        if self.size_ == len(self.table_):
            self.resize_()

        index =  self.indexFor(key,table_length = len(self.table_))
        node = self.table_[index]
        if node is not None:

            # exist and override
            while(node is not None):
                if (node.key == key):
                    node.val = val
                    node.hash = self.hash_(key)
                    return
                node = node.next

            # exist and join
            node = self.table_[index]

            while(node.next is not None):
                node = node.next
            temp = Node
            temp.hash = self.hash_(key)
            temp.key = key
            temp.val = val
            temp.next = None

            node.next = temp
            self.size_ += 1
            return

        else:
            # not exist
            temp = Node()
            temp.hash = self.hash_(key)
            temp.key = key
            temp.val = val
            temp.next = None
            self.table_[index] = temp
            self.size_ +=1
            return

    def get(self,key):

        index = self.indexFor(key,len(self.table_))
        if self.table_[index] is None:
            return -1
        node = self.table_[index]
        while(node is not None):
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self,key):
        index = self.indexFor(key,len(self.table_))

        # index = None and key not exist
        if self.table_[index] is None:
            return False

        node = self.table_[index]

        # first node’s key =key ,remove
        if(node.key == key):
            self.table_[index] = None
            self.size_ -= 1
            return True
        # other
        while(node.next is not None):
            if node.next.key == key:
                node.next = node.next.next
                self.size_ -= 1
                return True

            node = node.next
        return False


    def indexFor(self,key,table_length):
        return  self.hash_(key) & (table_length -1)

    def hash_(self,key):
        return (key>>16) ^ key

    def resize_(self):

        newTable = [None for i in range(2 * len(self.table_))]
        for i in range(len(self.table_)):

            node = self.table_[i]
            while(node is not None):
                temp = node
                index = self.indexFor(temp.hash,table_length= len(newTable))

                if(newTable[index] is not None):
                    # exist
                    newNode = newTable[index]
                    while(newNode.next is not None):
                        newNode = newNode.next
                    tempNode = Node()
                    tempNode.hash = node.hash
                    tempNode.key = node.key
                    tempNode.val = node.val
                    tempNode.next = None

                    newNode.next = tempNode

                else:
                    # not exist
                    tempNode = Node()
                    tempNode.hash = node.hash
                    tempNode.key = node.key
                    tempNode.val = node.val
                    tempNode.next = None

                    newTable[index] = tempNode
                node = node.next
        self.table_ = newTable

if __name__ == '__main__':
    map = MyHashMap()
    map.put(19,20)
    map.put(20, 20)
    map.remove(20)
    map.put(20, 20)



