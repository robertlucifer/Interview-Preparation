class Node:
    def __init__(self, data = None, next = None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None

    def insertation_at_begining(self, data):
        node = Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("The linked list is empty")
            return

        itr=self.head
        listtr = ''
        while itr is not None:
            listtr +=str(itr.data) +  '-->'
            itr=itr.next

        print(listtr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,Values):
        self.head=None
        for x in Values:
            self.insert_at_end(x)
    def get_len(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception("This is a invalid index")

        if index==0:
            self.head=self.head.next

        itr=self.head
        count=0
        while itr is not None:
            if count == index -1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self,value,index):
        if index<0 or index>self.get_len():
            raise Exception("Enter a valid index")
            return

        if index==0:
            self.insertation_at_begining(value)
            return

        itr=self.head
        count=0
        while itr:
            if count == index-1:
                itr.next=Node(value,itr.next)
            itr=itr.next
            count+=1


linkedlist=Linked_list()
linkedlist.insert_values([1,2,3,4,5,6])
linkedlist.print()
print (linkedlist.get_len())
linkedlist.remove_at(4)
linkedlist.print()
linkedlist.insert_at(5,4)
linkedlist.print()
