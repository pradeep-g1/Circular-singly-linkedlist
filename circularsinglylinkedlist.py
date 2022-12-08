class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self):
        if self.head is None:
            print("the circular singly linked list is empty :")
        else:
            node=self.head
            while node:
                print(node.data,"->",end=" ")
                node=node.next
                if node == self.tail.next:
                    break
    def insertion(self,item,location):
        newnode=Node(item)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode
            elif location==1:
                newnode.next=self.tail.next
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                currnode=self.head
                while index<location-1:
                    currnode=currnode.next
                    index+=1
                nextnode=currnode.next
                currentnode.next=newnode
                newnode.next=nextnode
    def searching(self,itemvalue):
        if self.head is None:
            print("the linkedlist is empty: ")
        else:
            node=self.head
            while node:
                if node.data==itemvalue:
                    print("Yes the value found ")
                node=node.next
    def deletion(self,location):
        if self.head is None:
            print("Linked list is empty: ")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            if location == 0:
                self.head=self.head.next
                self.tail.next=self.head
            elif location == 1:
                node=self.head
                while node:
                    if node.next==self.tail:
                        break
                    node=node.next
                node.next=self.head
                self.tail=node
            else:
                index=0
                currnode=self.head
                while index<location-1:
                    currnode=currnode.next
                    index+=1
                nextnode=currnode.next
                currnode.next=nextnode
csll=linkedlist()
num=list(map(int,input("enter the numbers: ").split(" ")))
for i in num:
    csll.insertion(i,1)
csll.traversal()
print()
ele=int(input("enter the ele: "))
csll.searching(ele)
dele=int(input("enter the ele for deleting location: "))
csll.deletion(dele)
csll.traversal()
print()

        